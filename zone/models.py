from django.db import models

class zone(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        db_table = 'zone'
# Create your models here.
# Create your models here.
