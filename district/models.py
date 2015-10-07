from django.db import models

class district(models.Model):
     district_name = models.CharField(max_length=255)
     province_id = models.IntegerField()

     def __str__(self):
         return self.district_name, self.province_id
     class Meta:
         db_table = 'district'


# Create your models here.
