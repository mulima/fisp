from django.db import models
class block(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table ='block'
# Create your models here.