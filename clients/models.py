from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(help_text='The slug is filled automatically from the name')

    def __unicode__(self):
        return u'%s' % self.name
