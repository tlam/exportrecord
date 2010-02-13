import locale

from django.conf import settings
from django.core.urlresolvers import reverse
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
    order_confirm = models.CharField(max_length=100, null=True, blank=True)
    payment_term = models.CharField(max_length=4, choices=PAYMENT_CHOICES, verbose_name='P.Term')
    currency = models.ForeignKey(Currency, verbose_name='CURR')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    country = models.ForeignKey(Country)
    shipment_date = models.DateField(null=True, blank=True)
    buyer = models.ForeignKey(Buyer)
    forwarder = models.ForeignKey(Forwarder, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    proforma_invoice_file = models.FileField(upload_to='proforma_invoice', null=True, blank=True)

    class Meta:
        ordering = ['file_no']

    def __unicode__(self):
        return u'%s - %s' % (self.date, self.supplier)

    def amount_format(self):
        return locale.format('%.2f', self.amount, grouping=True)
    amount_format.short_description = 'Amount'

    def container_quantity(self):
        return self.container.all()
    container_quantity.short_description = 'TC.Qty'
