from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=128),
        summary = models.TextField(_('Summary'), null=True, blank=True)
    )
    slug = models.SlugField(_('Slug'), unique=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def post_count(self):
        return self.category_posts.all().count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 
    
    class Meta:
        ordering = ('translations__title',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

def upload_post_image(instance, filename):
    filebase, extension = filename.split(".")
    return "{}/{}.{}".format("blog", instance.slug, extension)

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

class Post(TranslatableModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_posts",
        verbose_name=_('Author')
    )

    status = models.PositiveSmallIntegerField(_("Status"), choices=STATUS, default=0)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="category_posts",
        null=True,
        verbose_name=_('Category')
    )

    # Multi-Langugage
    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=255),
        content = models.TextField(_('Content'), null=True, blank=True)
    )

    slug = models.SlugField(_('Slug'), unique=True, blank=True)

    # image
    image = models.ImageField(
        _("Image"),
        upload_to=upload_post_image,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg"])],
        null=True,
        blank=True,
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("academy:university-detail", kwargs={"university_id": self.university_id})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)  
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')