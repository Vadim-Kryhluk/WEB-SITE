from django.contrib import admin

from . models import *
# Register your models here.


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'photo', 'status', 'slug')
#     list_display_links = ('username',)
#     list_fields = ('title', 'content')
#     list_filter = ('first_name',)

class WebAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    list_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class PayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    list_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Web, WebAdmin)
admin.site.register(Pay, PayAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)