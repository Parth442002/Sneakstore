from django.contrib import admin
from .models import Product,Category,Company
# Register your models here.
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)




