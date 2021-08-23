from django.contrib import admin
from .models import Stays,landlord ,tenant
# Register your models here.

class StayAdmin(admin.ModelAdmin):
    list_display = ('name','pincode', 'rating' , 'cost' ,'isFeatured')
    search_fields = ('name','pincode')
    list_filter = ('cost','rating','isFeatured')
    list_editable = ('isFeatured',)

class landlordAdmin(admin.ModelAdmin):
    list_display = ('name','phone')
    search_fields = ('name','phone','email')

class tenantAdmin(admin.ModelAdmin):
    list_display = ('name','phone')
    search_fields = ('name','phone','email')

admin.site.register(Stays,StayAdmin)
admin.site.register(landlord,landlordAdmin)
admin.site.register(tenant,tenantAdmin)
