from django.contrib import admin

# Register your models here.
from webprofile.models import WebProfile

@admin.register(WebProfile)
class ContactCardAdmin(admin.ModelAdmin):
    pass