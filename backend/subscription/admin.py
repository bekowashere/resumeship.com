from django.contrib import admin
from subscription.models import Plan, Subscription
from django.utils.translation import gettext_lazy as _

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Informations'), {'fields': ('id', 'name', 'slug', 'price')}),
        (None , {'fields': ('total_subscriptions_count', 'total_earnings')}),
        (_('Description'), {'fields': ('description',)}),
    )
    list_display = ('name', 'slug', 'price', 'total_earnings')
    search_fields = ('name', 'slug')
    ordering = ('price',)
    readonly_fields = ('id', 'total_subscriptions_count', 'total_earnings')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Informations'), {'fields': ('id', 'user', 'plan', 'paid_amount', 'is_active')}),
        (_('Period'), {'fields': ('period_type', 'period_duration')}),
        (_('Date'), {'fields': ('start_date', 'expiry_date')}),
    )
    list_display = ('user', 'plan', 'period_type', 'start_date', 'expiry_date', 'is_active')
    list_filter = ('period_type', 'is_active')
    search_fields = ('user__email', 'plan__name')
    ordering = ('start_date',)
    readonly_fields = ('id',)
