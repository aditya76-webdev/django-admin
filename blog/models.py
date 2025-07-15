from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
class Post(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PUBLISHED', 'Published'),
        ('UNPUBLISHED', 'Unpublished'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)])
    status = models.CharField(choices=STATUS_CHOICES,default='PENDING',)
    category = models.ForeignKey('Category', verbose_name=_(
        "category_name"), on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    # options
    name = models.CharField(max_length=200)
    count = models.IntegerField()
        
    def __str__(self):
        return  self.name

class Comment(models.Model):
    user_name = models.CharField(max_length=199)
    comment_desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey("Post", verbose_name=_("post_comment"), on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user_name