from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields


class Country(TranslatableModel):
    """
    Country database model.
    """

    country_code = models.CharField(_("Country code"), unique=True, db_index=True, max_length=16)

    translations = TranslatedFields(
        name = models.CharField(_("Name"), max_length=200),
        url = models.URLField(_("Webpage"), max_length=200, blank=True)
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")