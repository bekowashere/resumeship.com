from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import (
    User,
    UserSummary,
    UserPosition,
    UserDegree,
    UserStrength,
    UserLanguage
)
from account.forms import CustomUserCreationForm

@admin.register(User)
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        (_('Login Information'), {'fields': ('email', 'username', 'password')}),
        (_('Profile Information'), {
            'fields': (
                'first_name',
                'last_name',
                'headline',
                'profile_image',
                'phone_number'
            )
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Dates'), {'fields': ('last_login', 'date_joined')})
    )

    # ADD USER FIELD
    add_fieldsets = (
        (_('Login Information'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    list_display = ['email', 'username', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username', 'first_name', 'last_name', 'headline__icontains']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['date_joined']
    filter_horizontal = ['groups', 'user_permissions']

@admin.register(UserSummary)
class UserSummaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Description'), {'fields': ('description',)})
    )

    list_display = ['user']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name'
    ]

@admin.register(UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Position Information'), {'fields': ('title', 'company_name', 'company_url', 'description')}),
        (_('Date'), {'fields': ('start_date', 'end_date')})
    )

    list_display = ['user', 'title', 'company_name']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
        'company_name'
    ]

@admin.register(UserDegree)
class UserDegreeAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Position Information'), {'fields': ('title', 'organization_name', 'organization_url', 'description')}),
        (_('Date'), {'fields': ('start_date', 'end_date')})
    )

    list_display = ['user', 'title', 'organization_name']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
        'organization_name'
    ]

@admin.register(UserStrength)
class UserStrengthAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Position Information'), {'fields': ('name', 'description', 'level')})
    )

    list_display = ['user', 'name', 'level']
    list_filter = ['level']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'name__icontains'
    ]

@admin.register(UserLanguage)
class UserLanguageAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Position Information'), {'fields': ('name', 'description', 'level')})
    )

    list_display = ['user', 'name', 'level']
    list_filter = ['level']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'name__icontains'
    ]