from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from myproject.apps.core.models import (
    CreationModificationDatabase,
    MetaTagsBase,
    UrlBase,
)

class Idea(CreationModificationDatabase, MetaTagsBase, UrlBase):
    title = models.CharField(
        -("Title"),
        max_length=200,
    )
    content = models.TextField(
        -("Content"),
    )
    # other fields........

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")
        

class NewsArticle(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add = True)
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    theme = models.CharField(_("Theme"), max_length= 20)

    class Meta:
        verbose_name=_("News Article")
        verbose_name_plural = _("News Articles")

    def __str__(self):
        return str(self.title)