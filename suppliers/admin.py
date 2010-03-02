from django.contrib import admin

from suppliers.models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Supplier, SupplierAdmin)
