from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import(
    CreationModificationDatabase,
    MetaTagsBase,
    UrlBase,
)

class Idea()