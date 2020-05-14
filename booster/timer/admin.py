
from django.contrib import admin

from booster.timer.models import Timer

@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):

    list_display = ('id', 'start_datetime', 'end_datetime', 'user')
