from django.contrib import admin
from Asociations.models import Asociation
# Register your models here.
@admin.register(Asociation)
class AsociationAdmin(admin.ModelAdmin):
    pass