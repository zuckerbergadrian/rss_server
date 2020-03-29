from django.contrib import admin

from rss_server.apps.rss_model.models import RssSubscription, RssChannel, RssItem


class RssSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('link', 'email')


class RssItemAdmin(admin.ModelAdmin):
    list_display = ('channel_link', 'title', 'description')

    def channel_link(self, obj):
        return obj.channel.link


admin.site.register(RssSubscription, RssSubscriptionAdmin)
admin.site.register(RssChannel)
admin.site.register(RssItem, RssItemAdmin)
