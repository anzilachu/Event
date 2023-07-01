from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# from django.contrib.auth impor 

class Owner(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    featured_image = models.ImageField(upload_to="posts/")
    image1 = models.ImageField(upload_to='posts/', null=True, blank=True, default='default.jpg')
    image2 = models.ImageField(upload_to='posts/', null=True, blank=True, default='default.jpg')
    image3 = models.ImageField(upload_to='posts/', null=True, blank=True, default='default.jpg')
    image4 = models.ImageField(upload_to='posts/', null=True, blank=True, default='default.jpg')
    price = models.IntegerField()
    is_draft = models.BooleanField(default=False)
    district = models.CharField(max_length=255)
    owner = models.ForeignKey("posts.Owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    user = models.ForeignKey("posts.Owner", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
    book_date = models.DateField()

    def __str__(self):
        return self.email