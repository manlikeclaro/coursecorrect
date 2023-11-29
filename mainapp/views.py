from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from mainapp.app_forms import ProductForm, UpdateUser, ProfileForm
from mainapp.models import Product, CustomUser


# Create your views here.
def home(request):
    products = Product.objects.all()
    # products = Product.objects.all().order_by('product_price')
    # products = Product.objects.all().filter(product_category='education')
    # products = Product.objects.all().filter(product_category__icontains='ma')
    # products = Product.objects.all().filter(sale=False, product_price__lt=500)
    # products = Product.objects.all().order_by('-product_name')

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    data = {
        'products': products
    }

    return render(request, 'index.html', context=data)


def shop(request):
    products = Product.objects.all()
    unique_category = set()

    # for item in products:
    #     if item.product_category not in unique_category:
    #         unique_category.add(item.get_product_category_display())
    #         # unique_category.add(item.product_category)

    for item in products:
        if item.category not in unique_category:
            # unique_category.add(item.get_product_category_display())
            unique_category.add(item.category)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    data = {
        'products': products,
        'unique_category': unique_category
    }

    return render(request, 'shop.html', context=data)


@login_required
def profile(request):
    userinfo = CustomUser.objects.all()
    data = {
        'userinfo': userinfo
    }

    return render(request, 'profile-details.html', context=data)


def address(request):
    return render(request, 'address.html')


def about(request):
    return render(request, 'about.html')


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'User Logged In Successfully')

            if 'next' in request.POST:
                # return redirect(request.POST('next'))
                return redirect('profile')
            else:
                return redirect('home')

            # return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"data": form})

    # if request.method == 'GET':
    #     form = LoginForm()
    #     return render(request, 'login.html', {"data": form})
    #
    # elif request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, username=username, password=password)
    #         if user:
    #             login(request, user)
    #             messages.success(request, 'Signed in Successfully')
    #             return redirect('home')
    #     messages.error(request, 'Invalid Username/Password')
    #     return render(request, 'login.html', {"data": form})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully')
            # messages.error(request, 'Error Creating User')
            return redirect('sign-in')
    else:
        form = UserCreationForm()

    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'User Created Successfully')
    #         # messages.error(request, 'Error Creating User')
    #         return redirect('sign-in')
    # else:
    #     form = SignupForm()

    return render(request, 'sign-up.html', {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, 'User Logged Out Successfully')
    return redirect('home')


def product(request, id):
    single_product = Product.objects.get(pk=id)
    related_products = Product.objects.all()

    # paginator = Paginator(related_products, 4)
    # page_number = request.GET.get('page')
    # related_products = paginator.get_page(page_number)

    data = {
        'product': single_product,
        'related': related_products,
    }

    return render(request, 'product-single.html', context=data)


def product_search(request):
    search = request.GET['search']
    products = Product.objects.filter(
        Q(product_name__icontains=search) |
        Q(product_code__icontains=search) |
        Q(category__category_tag__icontains=search)
    )

    data = {
        'products': products
    }

    return render(request, 'index.html', context=data)


def product_category(request):
    category = request.GET['category']
    products = Product.objects.filter(
        Q(product_category__icontains=category)
    )

    data = {
        'products': products
    }

    return render(request, 'shop.html', context=data)


@login_required()
def update_profile(request):
    # form = UserChangeForm()

    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Settings Updated Successfully')
            return redirect('profile')
    else:
        form = UpdateUser(instance=request.user)

    return render(request, 'update-details.html', {'form': form})


@login_required()
def update_profile_details(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Details Updated Successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'update-profile-details.html', {'form': form})


@permission_required('mainapp.change_product')
def product_update(request, product_id):
    # item = get_object_or_404(Product, product_id)
    instance = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        # pass
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated Successfully')
            return redirect('product', id=product_id)
    else:
        form = ProductForm(instance=instance)

    context = {
        'form': form,
        'product': product_id,
    }

    return render(request, 'product-update.html', context)


@permission_required('mainapp.delete_product')
def product_delete(request, product_id):
    instance = get_object_or_404(Product, pk=product_id)
    # instance = Product.objects.get(pk=product_id)
    instance.delete()
    messages.success(request, 'Product Deleted Successfully')

    return redirect('home')

    # try:
    #     # Get the instance of the product to be deleted
    #     product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist")

    # product = Product.objects.get(pk=product_id)
    # if request.method == 'POST':
    #     product.delete()
    #     messages.success(request, 'Product Deleted Successfully')
    #     return redirect('home')  # Redirect to the list of products or another appropriate page
    #
    # context = {
    #     'product': product,
    # }
    #
    # return render(request, 'delete_product.html', context)


def confirmation(request):
    return render(request, 'confirmation.html')