import json
import datetime

from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from posts.forms import PostForm
from posts.models import Owner, Category, Post, Subscribe
from main.functions import generate_form_error, paginate_instances
from main.decorators import allow_self


@login_required(login_url="/users/login/")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            tags = form.cleaned_data['tags']

            if not Owner.objects.filter(user=request.user).exists():
                owner = Owner.objects.create(user=request.user, name=request.user.username)
            else:
                owner = request.user.owner


            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.owner= owner
            instance.save()

            tags_list = tags.split(",")
            for tag in tags_list:
                category, created = Category.objects.get_or_create(title=tag.strip())
                instance.category.add(category)

            response_data ={
                "title" : "Succefully created",
                "message" : "Succefully Created",
                "status" : "success",
                "redirect" : "yes",
                "redirect_url" : "/"

            }

        else:
            error_message = generate_form_error(form)
            response_data = {
                "title" : "From validation error",
                "message" : str(error_message),
                "status" : "error",
                "stable" : "yes",

            }
        return HttpResponse(json.dumps(response_data), content_type="application/json")   

    else:
        form = PostForm()
        context = {
            "title" : "Create new Post",
            "form" : form,
        }
        return render(request, "posts/create.html", context=context)


@login_required(login_url="/users/login/")
def my_posts(request):
    posts = Post.objects.filter(owner__user=request.user, is_deleted=False)
    instances = paginate_instances(request, posts, per_page=1)
    context = {
        "title" : "Blog | My Post",
        "instances" : instances
    }
    return render(request, "posts/my-posts.html", context=context)


@login_required(login_url="/users/login/")
@allow_self
def delete_post(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.save()

    reponse_data = {
        "title" : "Succefully deleted",
        "message" : "Post Deleted successfully",
        "status" : "success",
    }

    return HttpResponse(json.dumps(reponse_data), content_type="application/json")


@login_required(login_url="/users/login/")
@allow_self
def draft_post(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.save()

    reponse_data = {
        "title" : "Succefully Changed",
        "message" : "Post Updated successfully",
        "status" : "success",
    }

    return HttpResponse(json.dumps(reponse_data), content_type="application/json")

 
@login_required(login_url="/users/login/")
@allow_self
def edit_post(request, id):
    instance = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():

            tags = form.cleaned_data['tags']

            instance = form.save(commit=False)
            instance.save()

            instance.category.clear()

            tags_list = tags.split(",")
            for tag in tags_list:
                category, created = Category.objects.get_or_create(title=tag.strip())
                instance.category.add(category)

            response_data ={
                "title" : "Succefully created",
                "message" : "Succefully Created",
                "status" : "success",
                "redirect" : "yes",
                "redirect_url" : "/"

            }  

        else:
            error_message = generate_form_error(form)
            response_data = {
                "title" : "From validation error",
                "message" : str(error_message),
                "status" : "error",
                "stable" : "yes",

            }
        return HttpResponse(json.dumps(response_data), content_type="application/json")     

    else:
        category_string = ""
        for category in instance.category.all():
            category_string += f"{category.title},"

        form = PostForm(instance=instance, initial={"tags" : category_string[:-1]})
        context = {
            "title" : "Create new Post",
            "form" : form,
        }
        return render(request, "posts/create.html", context=context)


@login_required(login_url="/users/login/")
def subscribe(request, id):
    user = request.user

    email = request.POST.get("email")
    book_date = request.POST.get("book_date")

    if Post.objects.filter(id=id).exists():
        print(Subscribe.book_date)
        owner = Owner.objects.get(user=user)

        post = Post.objects.get(id=id)

        sub = Subscribe.objects.all()
        
        book = False
        for s in sub:
            print(s.book_date, '========', book_date)
            str_sub_book_date = str(s.book_date)
            str_book_date = str(book_date)
            print(str_sub_book_date == str_book_date)

            if str_sub_book_date == str_book_date:
                sub_post_title = s.post.title
                # print(s.post.filter(title=sub_post_title).exists(), "postlkjdsafkuhdsiu")
                # print(, 'title')
                # print(sub_post_title)
                if s.post.title == post.title:
                    print("hello")
                    book = False
                    print('break')
                    break
                    response_data = {
                            "title" : "Already booked",
                            "status" : "Error",
                            "stable" : "yes",
                        }

                    return HttpResponse(json.dumps(response_data), content_type="application/json") 
                else:
                    book = True
            else:
                    book = True
                

        print(book, "++++++++++++=")

        if book:
            post = Post.objects.get(id=id)
            Subscribe.objects.create(
                                email=email,
                                book_date=book_date,
                                post=post,
                                user=owner
                            )

            response_data = {
                                    "title" : "Successfully Booked",
                                    "status" : "success",
                                    "stable" : "yes",
                                }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {
                            "title" : "Already booked",
                            "status" : "Error",
                            "stable" : "yes",
                        }

            return HttpResponse(json.dumps(response_data), content_type="application/json")        
    else:
        response_data = {
                "title" : "This post doesn't exists",
                "status" : "Error",
                "stable" : "yes",

            }
        return HttpResponse(json.dumps(response_data), content_type="application/json") 