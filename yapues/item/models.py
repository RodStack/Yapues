from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

        verbose_name_plural = 'Categorias'
    
    def __str__ (self):
        return self.name

class  Item(models.Model):
    categoria = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='item_images', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.nombre