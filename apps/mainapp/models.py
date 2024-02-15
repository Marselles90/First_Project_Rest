from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    author = models.CharField(max_length=100)
    view = models.PositiveBigIntegerField(default=0)
    
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now() # При изменении новости обновляем дату и время на текущее
        super().save(*args, **kwargs)    
    
    def __str__(self):
        return self.title