from django.urls import path
from blog import views


app_name = "blog"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("posts", views.PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name='post-detail'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]

