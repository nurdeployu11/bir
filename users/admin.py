from django.contrib import admin
from .models import CustomUser, Saved
from django.contrib.auth.models import Group

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','tg_username','phone_number','avatar']
admin.site.unregister(Group)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Saved)