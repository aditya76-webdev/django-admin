from django.contrib import admin
from .models import Post

class BlogAdminSite(admin.AdminSite):
    site_header = "Blog Site"
    site_title = "Blog"
    index_title = "Blog Administrator"



blog_site_admin = BlogAdminSite(name="BlogAdmin")



