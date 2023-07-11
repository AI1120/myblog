from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
# Register your models here.

def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')

change_rating.short_description = "Mark Selected Products as Excellent"

class ProductA(admin.ModelAdmin):
    list_display = ('name', 'description', 'mfg_date', 'rating')
    list_filter = ('mfg_date',)
    actions = [change_rating]

admin.site.register(Product, ProductA)
admin.site.unregister(Group)

admin.site.site_header = "welcome to my django practise"