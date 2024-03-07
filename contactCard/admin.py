from django.contrib import admin

# Register your models here.
from contactCard.models import ContactCard

@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    pass