from django.urls import path
from posts import views
from posts.views import subscribe


app_name = "posts"


urlpatterns = [
    path("subscribe/<int:id>/",subscribe,name="subscribe")
]
