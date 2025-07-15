from django.db import models

# Create your models here.


class BookStore(models.Model):
    store_name  = models.CharField(max_length=250)
    
    def __str__(self):
        return self.store_name