from django.contrib import admin
from .models import User

# Register your models here.

class searchUser(admin.ModelAdmin):
    search_fields = ['userName']

admin.site.register(User, searchUser)