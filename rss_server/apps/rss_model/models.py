import datetime
from datetime import timedelta

import pytz
from django.db import models


class RssManager(models.Manager):
    def exists(self, link, email):
        return self.filter(link=link, email=email).exists()




class RssChannelManager(models.Manager):
    def exists(self, link):
        return self.filter(link=link).exists()

    def create_or_get(self, link, title, description):
        if self.exists(link):
            return self.get(link=link)
        else:
            return self.create(link=link, title=title, description=description)

    def get_all_links(self):
        return self.values_list('link', flat=True)


class RssItemManager(models.Manager):
    def delete_existing(self, link):
        self.filter(channel__link= link).delete()


class RssSubscription(models.Model):
    objects = RssManager()
    link = models.CharField(verbose_name='Link', max_length=255)
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Subskrypcja RSS'
        verbose_name_plural = 'Subskrypcje RSS'


class RssChannel(models.Model):
    objects = RssChannelManager()
    link = models.CharField(verbose_name='Link', max_length=255)
    title = models.TextField(verbose_name='Tytuł', default='', blank=True)
    description = models.TextField(verbose_name='Tekst', default='', blank=True)
    last_update = models.DateTimeField(verbose_name='Ostatnia aktualizacja', null=True)

    def can_be_updated(self):
        now = pytz.UTC.localize(datetime.datetime.now())
        return self.last_update is None or (self.last_update + timedelta(hours=24)) < now

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Kanał RSS'
        verbose_name_plural = 'Kanały RSS'


class RssItem(models.Model):
    objects = RssItemManager()
    title = models.TextField(verbose_name='Tytuł', default='', blank=True)
    description = models.TextField(verbose_name='Tekst', default='', blank=True)
    channel = models.ForeignKey(RssChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Informacja RSS'
        verbose_name_plural = 'Informacje RSS'
