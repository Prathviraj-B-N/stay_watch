from django.contrib import admin
from .models import Stays,landlord ,tenant
# Register your models here.

class StayAdmin(admin.ModelAdmin):
    list_display = ('name','pincode', 'rating' , 'cost' ,'isFeatured')
    search_fields = ('name','pincode')
    list_filter = ('cost','rating','isFeatured')
    list_editable = ('isFeatured',)

admin.site.register(Stays,StayAdmin)
admin.site.register(landlord)
admin.site.register(tenant)
