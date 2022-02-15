from django.contrib import admin
from django import forms 

from .models import NewsArticle

from .app_settings import ARTICLE_THEME_CHOICES

class NewsArtclesModelForm(forms.ModelForm):
    theme = forms.ChoiceField(
        label=NewsArticle._meta.get_field('theme').verbose_name,
        choices = ARTICLE_THEME_CHOICES,
        required=not NewsArticle._meta.get_field("theme").blank,
    )

    class Meta:
        fields = "__all__"

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    form = NewsArtclesModelForm

#admin.site.register(NewsArticle)