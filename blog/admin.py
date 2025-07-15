from django.contrib import admin
from .admin_site import blog_site_admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
blog_site_admin.register(Post,BlogAdmin)
# Register your models here.
