from django.contrib import admin
from .models import Setting, AndroidSetting


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(AndroidSetting)
class SettingsAdmin(admin.ModelAdmin):
    pass
