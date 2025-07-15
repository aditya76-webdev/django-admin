from django.contrib import admin
from .models import BookStore
from .admin_site import Book_Store_Admin

Book_Store_Admin.register(BookStore)

