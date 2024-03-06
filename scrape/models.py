from django.db import models

# Create your models here.


class link(models.Model):
    link_name = models.CharField(
        max_length=1000, null=True, blank=True, default="no name provided")
    link_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        if self.link_name == None:
            return "NAME IS NULL"
        return self.link_name
