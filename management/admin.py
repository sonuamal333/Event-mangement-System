from django.contrib import admin

from .models import Participant,Event

from .import models

admin.site.register(models.Participant)

admin.site.register(models.Event)
