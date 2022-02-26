from django.db import models

class CreationModificationDatabase(models.Model):
    
    pass

class MetaTagsBase(models.Model):
    pass

class UrlBase(models.Model):

    class Meta:
        abstract = True
        def get_url(self):
            if 