import locale
import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from clients.models import Client
from utils.amount import decimal_separator

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

    def total(self):
        records = self.record_set.all()
        currency = ''
        total_amount = 0

        for record in records:
            currency = record.currency
            total_amount += record.amount
        return '%s %s' % (currency, decimal_separator(total_amount))

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
        return u'%ix%s' % (self.quantity, self.type)

class Forwarder(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Record(models.Model):

    PAYMENT_CHOICES = (
        ('LS', 'L/C ST'),
        ('L30', 'L/C 30'),
        ('L60', 'L/C 60'),
        ('L90', 'L/C 90'),
        ('L120', 'L/C 120'),
        ('TT', 'TT'),
    )

    date = models.DateField()
    file_no = models.IntegerField()
    supplier = models.ForeignKey(Supplier)
    proforma_invoice = models.CharField(max_length=100)  # proforma invoice number
    container = models.ManyToManyField(Container)
    order_confirm = models.CharField(max_length=100, blank=True)
    payment_term = models.CharField(max_length=4, choices=PAYMENT_CHOICES, verbose_name='P.Term')
    currency = models.ForeignKey(Currency, verbose_name='CURR')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    country = models.ForeignKey(Country)
    shipment_date = models.DateField(null=True, blank=True)
    buyer = models.ForeignKey(Buyer)
    forwarder = models.ForeignKey(Forwarder, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['file_no']

    def __unicode__(self):
        return u'%s - %s' % (self.date, self.supplier)

    def amount_format(self):
        return decimal_separator(self.amount)
    amount_format.short_description = 'Amount'

    def container_quantity(self):
        return self.container.all()
    container_quantity.short_description = 'TC.Qty'

def invoice_file_name(instance, filename):
    ''' Upload file to under a folder with the record id '''
    return os.path.join('proforma_invoice', str(instance.record_id), filename)

class ProformaInvoiceFile(models.Model):
    file = models.FileField(upload_to=invoice_file_name, null=True, blank=True)
    record = models.ForeignKey(Record)

    def __unicode__(self):
        if self.file:
            return os.path.basename(self.file.path)
        else:
            return 'nothing'
