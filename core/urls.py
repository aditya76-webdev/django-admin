from django.contrib import admin
from django.urls import path
from blog.admin_site import blog_site_admin
from bookstore.admin_site import Book_Store_Admin
urlpatterns = [
    path("admin/", admin.site.urls),
    path('blogadmin/',blog_site_admin.urls),
    path('bookstore/', Book_Store_Admin.urls)
]

