from django.contrib import admin

# Register your models here.
from frontend.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['nin_price', 'demo_price', 'phone_price']
