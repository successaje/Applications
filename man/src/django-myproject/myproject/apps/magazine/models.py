from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    top_name = models.CharField(max_length= 264, unique = True)

    def __str__(self):
        return str(self.top_name)