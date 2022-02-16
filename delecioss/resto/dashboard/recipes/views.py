from django.shortcuts import render, redirect
from recipe.models import Recipe
from .forms import RecipeForm
from .services import get_recipe_list, get_recipe_one, delete


def rec_list(request):
    lists = get_recipe_list()
    ctx = {
        "all": lists
    }
    return render(request, 'dashboard/recipe/list.html', ctx)


def rec_detail(request, pk):
    one = get_recipe_one(pk)
    ctx = {
        "one": one
    }
    return render(request, 'dashboard/recipe/detail.html', ctx)


def rec_add(requests):
    form = RecipeForm()
    if requests.POST:
        forms = RecipeForm(requests.POST, requests.FILES)
        if forms.is_valid():
            forms.save()
        else:
            forms.errors

    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/recipe/forms.html', ctx)


def edit(requests, pk):
    root = Recipe.objects.get(pk=pk)
    form = RecipeForm(instance=root)
    if requests.POST:
        forms = RecipeForm(requests.POST, requests.FILS, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('rec_list')
        else:
            forms.errors
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/recipe/forms.html', ctx)


def rec_delete(requests, pk):
    delete(pk)
    return redirect('rec_list')










