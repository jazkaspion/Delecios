from django.shortcuts import render, redirect

from dashboard.categorie.forms import CategoryForm
from recipe.models import Category
from dashboard.categorie.services import cat_list, cat_delete, cat_one, cat_rec_delete


def list(requests):
    all = cat_list()
    ctx = {
        "all": all
    }
    return render(requests, 'dashboard/categorie/list.html', ctx)


def one(requests, pk):
    one = cat_one(pk)
    ctx = {
        "one": one
    }
    return render(requests, 'dashboard/categorie/detail.html', ctx)


def cat_add(requests):
    form = CategoryForm()
    if requests.POST:
        forms = CategoryForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('cat_list')
        else:
            print(forms.errors)
    ctx = {
        'forms': form
    }

    return render(requests, 'dashboard/categorie/forms.html', ctx)


def cat_edit(requests, pk):
    root = Category.objects.get(pk=pk)
    form = CategoryForm(instance=root)
    if requests.POST:
        forms = CategoryForm(requests.POST, instance=root)
        if forms.is_valid():
            form.save()
            return redirect('cat_list')
        else:
            print(forms.errors)
    ctx = {
        'forms': form
    }
    return render(requests, 'dashboard/categorie/forms.html', ctx)


def delete(requests, pk):
    cat_rec_delete(pk)
    cat_delete(pk)
    return redirect('cat_list')


















