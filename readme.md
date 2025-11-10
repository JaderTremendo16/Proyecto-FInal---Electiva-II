# Sistema de Inventario – Proyecto Final (Django)

> Proyecto Final para Electiva II  
> Universidad Cooperativa de Colombia Montería  
> Desarrollado por Jader Torres, Mateo Arroyo y Sebastián Rivero    
> Enlace del Funcionamiento del proyecto: https://www.youtube.com/watch?v=RHSaQOFFf8w

## Descripción general

El Sistema de Inventario es una aplicación web desarrollada con el framework Django que permite la gestión completa de productos, categorías y proveedores.  
El sistema está diseñado para aquellas personas que buscan optimizar su control de stock, facilitando la administración de su inventario mediante una interfaz moderna, validaciones visuales con SweetAlert2, y control de acceso por usuario.

Este proyecto integra conceptos de desarrollo backend, frontend y bases de datos, aplicados en un entorno web funcional y seguro.

## Características principales

- Autenticación de usuarios (inicio y cierre de sesión)  
- CRUD completo de productos, categorías y proveedores  
- Alertas visuales con SweetAlert2 para confirmaciones y mensajes del sistema  
- Cambio automático del estado del producto (`Disponible`, `Fuera de stock`, `Inactivo`)    
- Diseño limpio y responsivo con Bootstrap 5
- Evita la eliminación permanente de productos (solo los deshabilita)  

## Tecnologías utilizadas

**Framework:** Django 
**Lenguaje:** Python 
**Base de datos:** SQLite3
**Frontend:** HTML5, CSS, Bootstrap, SweetAlert2
**Control de versiones:** Git + GitHub
**Entorno virtual:** venv 

## Instalación y configuración

### 1. Clonar el repositorio

git clone https://github.com/JaderTremendo16/Proyecto-FInal---Electiva-II.git


### 2. Acceder al directorio del proyecto

cd Proyecto_Final

### 3. Crear entorno virtual

python -m venv venv


### 4. Activar entorno virtual

**Windows:**

venv\Scripts\activate

### 5. Instalar dependencias

pip install -r requirements.txt

### 6. Crear la base de datos y aplicar migraciones

python manage.py makemigrations
python manage.py migrate

### 7. Crear un superusuario

python manage.py createsuperuser


### 8. Ejecutar el servidor

python manage.py runserver


### 9. Acceder al sistema

http://127.0.0.1:8000/

## Uso básico

### Iniciar sesión
- Inicia sesión con el usuario creado (superusuario).  
- Si el ingreso es exitoso, aparece una alerta con el mensaje “Ingreso exitoso”.  
- Si las credenciales son incorrectas, se muestra un mensaje de error.

### Módulo de productos
- Crear, editar y deshabilitar productos.  
- El sistema actualiza automáticamente el estado:
  - `Disponible`: cantidad > 0  
  - `Fuera de stock`: cantidad = 0  
  - `Inactivo`: deshabilitado manualmente  

### Módulos de categorías y proveedores
- CRUD completo con alertas visuales (confirmar antes de eliminar).  
- Datos ordenados y listados con diseño limpio y responsivo.

## Ejemplo de funcionamiento

1. Inicias sesión con el usuario y contraseña puestos a la hora de crear el superusuario
2. Creas un nuevo proveedor y categoría  
2. Agregas un nuevo producto con su categoría y proveedor.  
3. Si la cantidad baja a 0, el producto cambia automáticamente a “Fuera de stock”.  
4. Si deseas suspenderlo temporalmente, puedes deshabilitarlo.  
5. Al intentar eliminar un registro, se muestra una confirmación visual con SweetAlert2.  

## Requisitos mínimos

- Python 3.10 o superior  
- Django 5.0 o superior  
- Navegador moderno
- Git instalado (opcional)

## Autores

**-Jader Torres**  
**-Mateo Arroyo**  
**-Sebastián Rivero**  
Universidad Cooperativa de Colombia Montería
Asignatura: Electiva II  
 

