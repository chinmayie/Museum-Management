# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
TYPE=[ ('art', 'art'),
    ('Archealogy', 'Archealogy'),
    ('Science', 'Science'),
    ('zoology', 'zoology'),]

class Visitors(models.Model):
    visitdate = models.DateField(blank=True, null=True)
    adult_ticket = models.PositiveIntegerField(blank=True, null=True,validators=[MaxValueValidator(10)])
    child_ticket = models.PositiveIntegerField(blank=True, null=True,validators=[MaxValueValidator(10)])
    tran_no = models.AutoField(primary_key=True)
    cost = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    def __str__(self):
        return str(self.adult_ticket)
    
    
class Divisions(models.Model):
    divid = models.PositiveIntegerField(primary_key=True,validators=[MinValueValidator(1)])
    type = models.CharField(max_length=20, blank=True, null=True,choices = TYPE)
    floorno = models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(1)])
    hallno = models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(1)])
    def __str__(self):
        return str(self.divid)

    
class Items(models.Model):
    itemid = models.PositiveIntegerField(primary_key=True,validators=[MinValueValidator(1)])
    date_acq = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    divid = models.ForeignKey('Divisions',null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.divid)

class Exhibition(models.Model):
    eid = models.PositiveIntegerField(primary_key=True,validators=[MinValueValidator(1)])
    etype = models.CharField(max_length=20, blank=True, null=True,choices= TYPE)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.etype
    
class Staff(models.Model):
    sid = models.PositiveIntegerField(primary_key=True,validators=[MinValueValidator(1)])
    sname = models.CharField(max_length=30, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    divid = models.ForeignKey('Divisions',null=True,on_delete=models.SET_NULL)
    eid = models.ForeignKey('Exhibition',null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.sname
