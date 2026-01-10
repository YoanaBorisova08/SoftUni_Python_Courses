from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from fruits.forms import CategoryCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruits.models import Fruit


def index_view(request) -> HttpResponse:
    return render(request, 'common/index.html')

def dashboard_view(request) -> HttpResponse:
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)

def create_fruit_view(request) -> HttpResponse:
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context ={
        'form': form,
    }
    return render(request, 'fruits/create-fruit.html', context)

def create_category_view(request) -> HttpResponse:
    if request.method == 'GET':
        form = CategoryCreateForm()
    else:
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'categories/create-category.html', context)

def details_fruit_view(request, fruit_id) -> HttpResponse:
    fruit = Fruit.objects.filter(pk=fruit_id).get()
    context = {
        'fruit': fruit,
    }
    return render(request, 'fruits/details-fruit.html', context)

def edit_fruit_view(request, fruit_id) -> HttpResponse:
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruits/edit-fruit.html', context)

def delete_fruit_view(request, fruit_id) -> HttpResponse:
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruits/delete-fruit.html', context)