from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Books)
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    # fields=['title']
    list_display=['title','price']
    list_filter=['title','price']
    search_fields=['title','price']