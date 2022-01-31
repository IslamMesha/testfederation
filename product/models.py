from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
