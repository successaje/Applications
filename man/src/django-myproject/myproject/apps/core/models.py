from django.db import models


class CreationModificationDatabase(models.Model):
    
    pass

class MetaTagsBase(models.Model):
    pass

class UrlBase(models.Model):

    class Meta:
        abstract = True
        def get_url(self):
            if hasattr(self.get_url_path, "dont recurse"):
                raise NotImplementedError
            
            try:
                path = self.get_url_path()
            except NotImplementedError:
                raise
            return settings.WEBSITE_URL + path
        get_url.dont_recurse = True

