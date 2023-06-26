from django.contrib import admin
from .models import *


@admin.register(JoinProject)
class JoinProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')

