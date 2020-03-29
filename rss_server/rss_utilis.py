import requests
import xml.etree.ElementTree as et

from django.core.mail import send_mail

from rss_server.apps.rss_model.models import RssChannel, RssItem
import datetime


def item_text(item, tag):
    element = item.find(tag)
    return element.text.strip() if element is not None and element.text is not None else ''


def update_rss(link, force=False):
    r = requests.get(link)
    rss_text = r.text
    tree = et.fromstring(rss_text)
    channel = tree.find('channel')
    rss_channel = RssChannel.objects.create_or_get(link=link, title=item_text(channel, 'title'),
                                                   description=item_text(channel, 'description'))
    if rss_channel.can_be_updated() or force:
        rss_channel.last_update = datetime.datetime.now()
        rss_channel.save()
        RssItem.objects.delete_existing(link)
        for child in tree.iter('item'):
            RssItem.objects.create(title=item_text(child, 'title'), description=item_text(child, 'description'),
                                   channel=rss_channel)
    return rss_text


def send_rss_mail(link, recipient):
    items = RssItem.objects.filter(channel__link=link)
    message = ''
    for item in items:
        message += item.title + ':\n' + item.description + '\n\n'

    is_sent = send_mail('Aktualizacja dla ' + link, message, 'info@rss-updates.com', [recipient], fail_silently=True)
    return is_sent == 1
