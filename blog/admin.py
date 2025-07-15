from django.contrib import admin
from .admin_site import blog_site_admin
from .models import Post,Category , Comment


def publish_action(modeladmin,request,queryset):
    queryset.update(status='PUBLISHED')
publish_action.short_description = "Mark selected items as published"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description' , 'rating','status')
    list_filter = ['rating']
    fields = ['title','description','status']
    actions = [publish_action]
blog_site_admin.register(Post,PostAdmin)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name','count']
    list_display = ('name','count' ,)
    list_filter = ("name",)
    
    class Meta:
        
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','comment_desc','created_at')
    list_filter = ['user_name']
    
    class  Meta:
        
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']
    
blog_site_admin.register(Category, CategoryAdmin)
blog_site_admin.register(Comment, CommentAdmin)