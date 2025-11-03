from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm, ProveedorForm

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

# ---------- CATEGORÍAS ----------

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'inventario/lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'inventario/crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'inventario/editar_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'inventario/eliminar_categoria.html', {'categoria': categoria})


# ---------- PROVEEDORES ----------
@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/lista_proveedores.html', {'proveedores': proveedores})

@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventario/crear_proveedor.html', {'form': form})

@login_required
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventario/editar_proveedor.html', {'form': form})

@login_required
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'inventario/eliminar_proveedor.html', {'proveedor': proveedor})
