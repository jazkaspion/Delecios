from django.shortcuts import render
from .models import Recipe, Suggestion, Category
# Create your views here.
from .services import get_recipes_all, get_recipes_one


def index(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/index.html', ctx)


def about(requests):
    return render(requests, 'site/about.html', {})


def contact(requests):
    suggest = Suggestion()
    if requests.POST:
        suggest.name = requests.POST.get('name')
        suggest.email = requests.POST.get('email')
        suggest.subject = requests.POST.get('subject')
        suggest.message = requests.POST.get('message')

        suggest.save()

    return render(requests, 'site/contact.html', {})


def receipe(requests, pk=None):
    one = Recipe.objects.get(pk=pk)

    ctx = {
        'one': one
    }

    return render(requests, 'site/receipe-post.html', ctx)















