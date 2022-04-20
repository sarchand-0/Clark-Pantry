import django_filters
from django_filters import CharFilter
from .models import *

class ItemFilter(django_filters.FilterSet):
	name= CharFilter(field_name='name')
	class Meta:
		model=Item
		fields= ['tags']

