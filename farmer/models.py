from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib import admin


class farmer(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Othername = models.CharField(max_length=200)
    DOB = models.DateTimeField('date born')
    Gender = models.CharField(max_length=8)
    IdType = models.CharField(max_length=200)
    IdNumber = models.CharField(max_length=200)
    FarmArea = models.CharField(max_length=200)
    FarmAreaDimensions = models.CharField(max_length=200)
    ZoneId = models.CharField(max_length=200)
    BlockId = models.CharField(max_length=200)
    CampId = models.CharField(max_length=200)
    DistrictId = models.CharField(max_length=200)
    FarmAreaId = models.CharField(max_length=200)


    def __str__(self):  # __unicode__ on Python 2
        return self.Firstname, self.Lastname, self.Othername, self.DOB, self.Gender, self.IdType, self.IdNumber, self.FarmArea, self.FarmAreaDimensions, self.ZoneId, self.BlockId, self.CampId, self.DistrictId, self.FarmAreaId
    class Meta:
        db_table = 'farmer'


