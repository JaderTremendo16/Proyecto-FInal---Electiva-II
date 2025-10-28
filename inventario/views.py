from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# LISTAR
@login_required
def lista_productos(request):
    # Captura los parámetros de búsqueda y filtros
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria')
    proveedor_id = request.GET.get('proveedor')
    stock_bajo = request.GET.get('bajo_stock')

    # Construye la consulta base
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    if categoria_id and categoria_id.isdigit():
        productos = productos.filter(categoria_id=categoria_id)

    if proveedor_id and proveedor_id.isdigit():
        productos = productos.filter(proveedor_id=proveedor_id)

    if stock_bajo == '1':
        productos = productos.filter(cantidad__lt=10)

    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    return render(request, 'inventario/lista_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'proveedores': proveedores,
        'query': query,
        'categoria_id': categoria_id,
        'proveedor_id': proveedor_id,
        'stock_bajo': stock_bajo,
    })

# CREAR
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/crear_producto.html', {'form': form})

# EDITAR
@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})

# ELIMINAR
@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})

# LOGIN Y LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'inventario/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

