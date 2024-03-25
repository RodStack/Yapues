from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(vendido=False)[0:6]
    categorias = Category.objects.all()

    return render(request, 'core/index.html', {
        'categorias': categorias,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contacto.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
        else:
            form = SignupForm()

    form = SignupForm()

    return render (request, 'core/registrarse.html',{
        'form':form
    })
