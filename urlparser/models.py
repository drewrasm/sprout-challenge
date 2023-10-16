from django.db import models

class ShortenedURL(models.Model):
    url = models.URLField(max_length=2000, unique=True)
    short_url = models.CharField(max_length=2000, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.short_url} -> {self.url}'

    class Meta:
        verbose_name = "Shortened URL"
        verbose_name_plural = "Shortened URLs"


