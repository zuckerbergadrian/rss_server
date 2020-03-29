from django.core.management import BaseCommand

from rss_server.apps.rss_model.models import RssSubscription, RssChannelManager, RssChannel
from rss_server.rss_utilis import update_rss, send_rss_mail


class Command(BaseCommand):

    def handle(self, *args, **options):
        links = RssChannel.objects.get_all_links()

        for link in links:
            update_rss(link, True)

        rss_sub = RssSubscription.objects.all()
        for sub in rss_sub:
            print(sub.link, sub.email)
            o = send_rss_mail(sub.link, sub.email)
            if not o:
                print('\t\tFailed: ', sub.link, sub.email)
