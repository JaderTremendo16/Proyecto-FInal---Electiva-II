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
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey("Proveedor", on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('disponible', 'Disponible'),
            ('fuera_stock', 'Fuera de stock'),
            ('inactivo', 'Inactivo'),
        ],
        default='disponible'
    )

    def save(self, *args, **kwargs):
        """
        Cada vez que se guarda un producto, su estado se actualiza automáticamente:
        - Si cantidad = 0 → 'fuera_stock'
        - Si cantidad > 0 → 'disponible'
        - Si está inactivo, se mantiene así (no se cambia automáticamente).
        """
        if self.estado != 'inactivo':  # No sobreescribir si está deshabilitado manualmente
            if self.cantidad == 0:
                self.estado = 'fuera_stock'
            else:
                self.estado = 'disponible'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} unidades)"
