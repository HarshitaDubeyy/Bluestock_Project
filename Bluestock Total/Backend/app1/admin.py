from django.contrib import admin
from . models import Item

# Register your models here.

@admin.register(Item)
class BookAdmin(admin.ModelAdmin):
  list_display = ('name','Brand','Price_Band','Open','Close','Issue_size','Issue_Type','Listing_Date')