from django.contrib import admin

from src.custom_user.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)