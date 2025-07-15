from django.contrib.admin import AdminSite
from django.contrib import admin

class BookStoreAdmin(AdminSite):
    site_header = "BookStore"
    site_title = "BookStore title"
    index_title = "Book Store Administrator"

Book_Store_Admin  = BookStoreAdmin(name="BookStoreAdmin")