from django.db import models

from utils.amount import decimal_separator

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(help_text='The slug is filled automatically from the name')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % self.name

    def total(self):
        records = self.record_set.all()
        currency = ''
        total_amount = 0

        for record in records:
            currency = record.currency
            total_amount += record.amount
        #return '%s %s' % (currency, decimal_separator(total_amount))
        return {
            'currency': currency, 
            'amount': decimal_separator(total_amount)
        }
