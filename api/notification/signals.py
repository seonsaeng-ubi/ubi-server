from django.dispatch import receiver
from django.db.models.signals import post_save
from api.notification.models import Notification
from api.logger.models import FirebaseLog
from api.user.models import Profile
from firebase_admin import messaging


@receiver(post_save, sender=Notification)
def send_firebase(sender, instance, created, *args, **kwargs):
    if created:
        profiles = Profile.objects.all().select_related('user')

        for profile in profiles:
            message = messaging.Message(
                notification=messaging.Notification(
                    title=instance.title,
                    body=instance.body,
                ),
                token=profile.firebase_token,
            )
            response = messaging.send(message)

            firebase_log = FirebaseLog.objects.create(
                to=profile.user.email,
                title=instance.title,
                body=instance.body,
                status='S'
            )
            firebase_log.save()
        instance.save()
