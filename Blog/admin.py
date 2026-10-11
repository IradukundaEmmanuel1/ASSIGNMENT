from django.contrib import admin

from .models import *
# register your
admin.site.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")


