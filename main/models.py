from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture_url = models.URLField(max_length=500)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

