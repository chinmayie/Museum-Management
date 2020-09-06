from .models import Exhibition,Visitors,Staff,Divisions,Items
import django_filters


class UserFilter1(django_filters.FilterSet):
    class Meta:
        model = Exhibition
        fields = ['etype' ]
class UserFilter2(django_filters.FilterSet):
    class Meta:
        model = Visitors
        fields = ['visitdate']
class UserFilter3(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['sid', 'sname', 'job']
class UserFilter4(django_filters.FilterSet):
    class Meta:
        model = Divisions
        fields = ['divid', 'type', 'floorno', 'hallno' ]
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Items
        fields = ['itemid']
