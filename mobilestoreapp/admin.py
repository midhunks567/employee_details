from django.contrib import admin
from .models import Brand_nm,product

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('brand_name',)}
admin.site.register(Brand_nm,BrandAdmin)

class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,ProdAdmin)
