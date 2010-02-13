from django.contrib import admin
from export.models import Buyer, Container, Country, Currency, Forwarder, Record, Supplier

class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'file_no', 'supplier', 'proforma_invoice', 'container_quantity', 'order_confirm', 'payment_term', 'currency', 'amount_format', 'country', 'shipment_date', 'buyer', 'forwarder', 'note',)
    search_fields = ['supplier__name', 'proforma_invoice', 'order_confirm', 'buyer__name']
    filter_horizontal = ('container', )

admin.site.register(Buyer)
admin.site.register(Container)
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Forwarder)
admin.site.register(Record, RecordAdmin)
admin.site.register(Supplier)
