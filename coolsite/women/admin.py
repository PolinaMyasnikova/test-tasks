from django.contrib import admin

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slag": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'village')
    list_display_links = ('id', 'village')
    search_fields = ('village',)
    prepopulated_fields = {"slag": ("village",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
