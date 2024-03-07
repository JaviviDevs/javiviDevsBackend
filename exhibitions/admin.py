from django.contrib import admin
from exhibitions.models import Exhibition,PhotosExhibition
# Register your models here.

@admin.register(Exhibition)
class CatsAdmin(admin.ModelAdmin):
    pass

@admin.register(PhotosExhibition)
class PhotosCatAdmin(admin.ModelAdmin):
    pass