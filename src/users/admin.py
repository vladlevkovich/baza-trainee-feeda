from django.contrib import admin
from .models import *


# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id',)


admin.site.register(CustomUser)
admin.site.register(Projects)

