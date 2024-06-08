from django.contrib import admin
from api.logger.models import EmailLog, FirebaseLog


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('to', 'title', 'body', 'status')


@admin.register(FirebaseLog)
class FirebaseLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'status')
