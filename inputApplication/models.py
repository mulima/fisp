from django.db import models

class InputApplication(models.Model):
    farmer_id = models.IntegerField()
    application_date = models.DateField()
    camp_id = models.IntegerField()
    block_id = models.IntegerField()
    district_id = models.IntegerField()
    zone_id = models.IntegerField()
    farmer_organization_id = models.IntegerField()
    farmer_organization_approved = models.IntegerField()
    farmer_organization_approved_date = models.DateField()
    farmer_organization_approved_by = models.IntegerField()
    CAC_approved = models.IntegerField()
    CAC_approved_by = models.IntegerField()
    CAC_approved_date = models.DateField()
    DAC_approved = models.IntegerField()
    DAC_approved_by = models.IntegerField()
    DAC_approved_date = models.DateField()

    def __str__(self):
        return self.farmer_id

    class Meta:
        db_table = 'input_application'

# Create your models here.
