from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category
from .forms import LoginForm, RegisterForm
from .cart import Cart

def home(request):
    products = Product.objects.all()[:8]  # 8 последних товаров
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {
        'products': products,
        'categories': categories,
    })

def catalog(request):
    category_slug = request.GET.get('category')
    products = Product.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    categories = Category.objects.all()
    return render(request, 'shop/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_slug,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('home')
    else:
        form = LoginForm()
    
    return render(request, 'shop/login.html', {'form': form})

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Регистрация прошла успешно! Добро пожаловать, {user.username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'shop/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('home')

@login_required
def cart_view(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    messages.success(request, f'Товар "{product.name}" добавлен в корзину.')
    return redirect(request.META.get('HTTP_REFERER', 'catalog'))

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.success(request, f'Товар "{product.name}" удален из корзины.')
    return redirect('cart')

@login_required
def update_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)
        cart.update(product, quantity)
        messages.success(request, f'Количество товара "{product.name}" обновлено.')
    return redirect('cart')

@login_required
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, 'Корзина очищена.')
    return redirect('cart')

# stuff i added

def about(request):
    return render(request, "about.html")

def socialmedia(request):
    return render(request, "socialmedia.html")