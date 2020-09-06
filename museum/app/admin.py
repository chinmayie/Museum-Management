# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Visitors,Divisions,Items,Staff,Exhibition
admin.site.register(Visitors)
admin.site.register(Divisions)
admin.site.register(Items)
admin.site.register(Staff)
admin.site.register(Exhibition)
