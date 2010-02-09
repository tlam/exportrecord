import locale

from django.conf import settings
from django.db import models

locale.setlocale(locale.LC_ALL, '')

class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Currency(models.Model):
    code = models.CharField(max_length=5)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ['code']

    def __unicode__(self):
        return self.code

class Buyer(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Container(models.Model):
    CONTAINER_CHOICES = (
        ('20', '20 ft'),
        ('40', '40 ft'),
        ('40HC', '40 ft High Cube'),
        ('LCL', 'LCL'),
    )

    type = models.CharField(max_length=4, choices=CONTAINER_CHOICES)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['type', 'quantity']

    def __unicode__(self):
        return '%i x %s' % (self.quantity, self.type)

class Record(models.Model):

    PAYMENT_CHOICES = (
        ('LS', 'L/C at Sight'),
        ('L30', 'L/C at 30 days'),
        ('L60', 'L/C at 60 days'),
        ('L90', 'L/C at 90 days'),
        ('L120', 'L/C at 120 days'),
        ('TT', 'T/T'),
    )

    date = models.DateField()
    file_no = models.IntegerField()
    supplier = models.ForeignKey(Supplier)
    proforma_invoice = models.CharField(max_length=100)  # proforma invoice number
    container = models.ManyToManyField(Container)
    order_confirm = models.CharField(max_length=100, null=True, blank=True)
    payment_term = models.CharField(max_length=4, choices=PAYMENT_CHOICES)
    currency = models.ForeignKey(Currency)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    country = models.ForeignKey(Country)
    shipment_date = models.DateField(null=True, blank=True)
    buyer = models.ForeignKey(Buyer)
    note = models.TextField(null=True, blank=True)
    proforma_invoice_file = models.FileField(upload_to='proforma_invoice', null=True, blank=True)

    class Meta:
        ordering = ['file_no']

    def __unicode__(self):
        return '%s - %s' % (self.date, self.supplier)

    def container_quantity(self):
        return self.container.all()

    def amount_format(self):
        return locale.format('%.2f', self.amount, grouping=True)
    amount_format.short_description = 'Amount'
