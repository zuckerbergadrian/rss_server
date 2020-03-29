from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from rss_server.apps.rss_model.forms import RssForm
from rss_server.apps.rss_model.models import RssSubscription
from rss_server.rss_utilis import update_rss, send_rss_mail


def index(request):
    if request.method == 'POST':
        form = RssForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            email = form.cleaned_data['email']
            rss_text = update_rss(link)
            if 'submit-save' in request.POST:
                if RssSubscription.objects.exists(link, email):
                    messages.info(request, "Podany email i link już istnieją w systemie")
                else:
                    form.save()
                    messages.success(request, "Email i link zostały zapisane")
            else:
                email_sent = send_rss_mail(link, email)
                if email_sent:
                    messages.success(request, "Wiadomość została wysłana")
                else:
                    messages.error(request, "Wystąpił nieoczekiwany błąd. Wiadomość nie została wysłana")

    else:
        form = RssForm()
    return render(request, 'index.html', locals())
