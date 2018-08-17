from django.db import models


# Create your models here.
class ContactContent(models.Model):
    content = models.CharField(max_length=100000, null=True, blank=True)
