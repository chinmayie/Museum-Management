from django import forms
from django . forms import ModelChoiceField
from . models import Items,Staff,Exhibition,Visitors,Divisions
import datetime

#class Visitors(forms.ModelForm):
#  class Meta:
#    model= Visitors
#    fields= ["visitdate", "adult_ticket", "child_ticket"]
class Exhibitions(forms.ModelForm):
  class Meta:
    model= Exhibition
    fields= ["eid","etype","startdate","enddate"]
class Visitor(forms.ModelForm):

   class Meta:
    model= Visitors
    fields= ["visitdate", "adult_ticket", "child_ticket"]

class Division(forms.ModelForm):
  class Meta:
    model= Divisions
    fields= ["divid","type", "floorno", "hallno"]
  
class Item(forms.ModelForm):
  class Meta:
    model= Items
    fields= ["itemid", "date_acq", "description","divid"]

class employee(forms.ModelForm):
  class Meta:
    model=Staff
    fields= ["sid","sname","divid","salary","job","eid"]

