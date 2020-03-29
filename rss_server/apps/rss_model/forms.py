from django import forms

from rss_server.apps.rss_model.models import RssSubscription


class RssForm(forms.ModelForm):
    class Meta:
        model = RssSubscription
        fields = ('link', 'email')

    def __init__(self, *args, **kwargs):
        super(RssForm, self).__init__(*args, **kwargs)
        self.fields['link'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

