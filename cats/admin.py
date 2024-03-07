from django.contrib import admin
from cats.models import Cat,PhotosCat
# Register your models here.

@admin.register(Cat)
class CatsAdmin(admin.ModelAdmin):
    pass

@admin.register(PhotosCat)
class PhotosCatAdmin(admin.ModelAdmin):
    pass