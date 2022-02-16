from django.db import models

# Create your models here.
from django.utils.text import slugify

def default_rate():
    return (
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),

    )


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kvargs):
        if not self.slug:
            self.slug = slugify(self.content)
        super(Category, self).save(*args, **kvargs)


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    steps = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.IntegerField()
    rate = models.IntegerField(choices=default_rate())
    img = models.ImageField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Suggestion(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=512)
    message = models.TextField()

    def __str__(self):
        return self.name























