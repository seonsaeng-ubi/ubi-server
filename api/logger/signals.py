import requests
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from api.logger.models import EmailLog


@receiver(post_save, sender=EmailLog)
def send_mail_gun(sender, instance, created, *args, **kwargs):
    if created:
        url = "https://api.mailgun.net/v3/www.woobi.co.uk/messages"
        headers = {
            'Authorization': f'api {settings.MAILGUN_API_KEY}'
        }
        response = requests.post(
            "https://api.mailgun.net/v3/www.woobi.co.uk/messages",
            auth=("api", settings.MAILGUN_API_KEY),
            data={"from": "mail@woobi.co.uk",
                  "to": instance.to,
                  "subject": instance.title,
                  "text": instance.body})
        if response.status_code != 200:
            instance.status = 'F'
        else:
            instance.status = 'S'
        instance.save()
