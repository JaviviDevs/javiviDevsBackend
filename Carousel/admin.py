from django.contrib import admin
from Carousel.models import CarouselElement
# Register your models here.

@admin.register(CarouselElement)
class CarouselAdmin(admin.ModelAdmin):
    pass