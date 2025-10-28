from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=11, blank=True)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True, blank= True)
    proveedor = models.ForeignKey("Proveedor", on_delete=models.SET_NULL, null=True, blank= True)
    cantidad = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} unidades)"