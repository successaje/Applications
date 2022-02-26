from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import(
    CreationModificationDatabase,
    MetaTagsBase,
    UrlBase,
)

class Idea(CreationModificationDatabase, MetaTagsBase, UrlBase):
    title = models.CharField(
        _("Title"),
        max_length=200,
    )

    content = models.TextField(
        _("Content"),
    )

    class Meta:
        verbose_name= _("Idea")