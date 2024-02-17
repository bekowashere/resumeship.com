from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import FileExtensionValidator

def upload_profile_image(instance, filename):
    filebase, extension = filename.rsplit(".")
    return f"user/profile/{instance.email}.{extension}"


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with given email and password
        """

        if not email:
            raise ValueError(_('You must provide an email address'))

        if not password:
            raise ValueError(_('User must have a password'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(email, password=password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        user = self._create_user(email, password=password, **extra_fields)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('Username'),
        max_length=128,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        help_text=_('Required. 50 characters or fewer. Example: john.doe@gmail.com'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff User'), default=False)
    is_superuser = models.BooleanField(_('Superuser'), default=False)


    # Information
    first_name = models.CharField(_('First Name'), max_length=32, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=32, blank=True)
    headline = models.CharField(
        _('Headline'),
        max_length=128,
        null=True,
        blank=True
    )
    profile_image = models.ImageField(
        _('Profile Picture'),
        upload_to=upload_profile_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=32,
        null=True,
        blank=True
    )

    # seçmeli yapabiliriz, data elimizde toplanır
    # country
    # state
    # city

    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_username()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


"""
+ Work Experience
+ Education
+ Skill
+ Language
- Interest
- Certificate
- Awards
- Organization
- Project
- Course
- Publication
- Reference
"""

class UserSummary(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_summary'
    )
    description = models.TextField(_('Summary'), null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} Summary'
    
    class Meta:
        verbose_name = _('User Summary')
        verbose_name_plural = _('User Summaries')

class UserPosition(models.Model):
    """
    Position means that Work Experience
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_positions'
    )
    title = models.CharField(
        _('Title'),
        max_length=128,
        help_text=_('Backend Developer'),
        null=True,
        blank=True
    )
    company_name = models.CharField(
        _('Company Name'),
        max_length=255,
        help_text=_('ArtnCode'),
        null=True,
        blank=True
    )
    company_url = models.CharField(
        _('Company Website'),
        max_length=128,
        null=True,
        blank=True
    )
    description = models.TextField(_('Description'), null=True, blank=True)
    
    start_date = models.CharField(
        _('Start Date'),
        max_length=16,
        help_text='01/02/2022',
        null=True,
        blank=True
    )

    end_date = models.CharField(
        _('End Date'),
        max_length=16,
        help_text='01/02/2023',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} - {self.company_name}'

    class Meta:
        verbose_name = _('User Position')
        verbose_name_plural = _('User Positions')

class UserDegree(models.Model):
    """
    Degree means that Education
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_degrees'
    )
    title = models.CharField(
        _('Degree'),
        max_length=128,
        help_text=_('Management Information System'),
        null=True,
        blank=True
    )
    organization_name = models.CharField(
        _('Organization Name'),
        max_length=255,
        help_text=_('Istanbul Bilgi University'),
        null=True,
        blank=True
    )
    organization_url = models.CharField(
        _('School Website'),
        max_length=128,
        null=True,
        blank=True
    )
    description = models.TextField(_('Description'), null=True, blank=True)
    
    start_date = models.CharField(
        _('Start Date'),
        max_length=16,
        help_text='24/06/2016',
        null=True,
        blank=True
    )

    end_date = models.CharField(
        _('End Date'),
        max_length=16,
        help_text='24/06/2023',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} - {self.organization_name}'

    class Meta:
        verbose_name = _('User Degree')
        verbose_name_plural = _('User Degrees')

class UserStrength(models.Model):
    """
    Strength means that Skill
    """
    class StrengthChoices(models.IntegerChoices):
        ONE = 1, _("Novice")
        TWO = 2, _("Beginner")
        THREE = 3, _("Skillful")
        FOUR = 4, _("Experienced")
        FIVE = 5, _("Expert")
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_strengths'
    )

    name = models.CharField(
        _('Skill Name'),
        max_length=255,
        null=True,
        blank=True
    )
    description = models.TextField(_('Description'), null=True, blank=True)

    level = models.IntegerField(
        _('Level'),
        choices=StrengthChoices.choices,
        default=StrengthChoices.FIVE,
    )

    def __str__(self):
        return f'{self.name} --> {self.level}'

    class Meta:
        verbose_name = _('User Strength')
        verbose_name_plural = _('User Strengths')

class UserLanguage(models.Model):
    class LanguageChoices(models.IntegerChoices):
        A1 = 1, _("Beginner")
        A2 = 2, _("Elementary ")
        B1 = 3, _("Intermediate ")
        B2 = 4, _("Upper Intermediate")
        C1 = 5, _("Advanced ")
        C2 = 6, _("Proficient ")
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_languages'
    )

    name = models.CharField(
        _('Language'),
        max_length=255,
        null=True,
        blank=True
    )
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
        help_text="TOEFL, IELTS, C2 e.g..."
    )

    level = models.IntegerField(
        _('Level'),
        choices=LanguageChoices.choices,
        default=LanguageChoices.A1,
    )

    def __str__(self):
        return f'{self.name} --> {self.level}'

    class Meta:
        verbose_name = _('User Language')
        verbose_name_plural = _('User Languages')