from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User
from datetime import date, timedelta

"""
Plan: Free - Basic - Pro
Plan Feature?
Subscription
"""
class Plan(models.Model):
    name = models.CharField(_('Plan Name'), max_length=48)
    description = models.TextField(_('Description'), null=True, blank=True)
    slug = models.SlugField(_('Slug'), unique=True)
    price = models.DecimalField(
        _('Price'),
        max_digits=9,
        decimal_places=2
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

class Subscription(models.Model):
    class PeriodChoices(models.IntegerChoices):
        M = 0, _("Monthly")
        Y = 1, _("Yearly ")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_subscriptions",
        verbose_name=_('User')
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="plan_subscriptions",
        verbose_name=_('Plan')
    )

    period_type = models.IntegerField(
        _('Period Type'),
        choices=PeriodChoices.choices,
        default=PeriodChoices.M,
    )
    period_duration = models.PositiveSmallIntegerField(
        _('Period Duration'),
        help_text=_('The default value is 30 because a month has 30 days. expiry_date = start_date + period_duration'),
        default=30
    )

    start_date = models.DateField(_('Start Date'), default=date.today())
    expiry_date = models.DateField(_('Expiry Date'), null=True, blank=True)

    paid_amount = models.DecimalField(
        _('Paid Amount'),
        max_digits=9,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.plan.name}"

    def save(self, *args, **kwargs):
        if self.period_type == self.PeriodChoices.M:
            self.period_duration = 30
        elif self.period_type == self.PeriodChoices.Y:
            self.period_duration = 365
        self.expiry_date = self.start_date + timedelta(days=self.period_duration)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')