from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(_('created'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class Timer(TimeStampedModel):
    """
    Timer Model: for Saving Time entry
    Each Time Enty will have
    1. Task
    2. Project
    3. Start Time
    4. End Time
    """
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    task = models.CharField(max_length=512)
    project = models.CharField(max_length=512)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    last_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Entry" + self.task
