from django.contrib import admin # type: ignore
from .models import Reward

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'points', 'badge')
