from django.contrib import admin
from posts.models import Owner, Category, Post,Subscribe


class OwnerAdmin(admin.ModelAdmin):
    list_display = ("name", "user")

admin.site.register(Owner, OwnerAdmin)


admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "short_description","district","price","image1","image2","image3","image4")

admin.site.register(Post, PostAdmin)


admin.site.register(Subscribe)