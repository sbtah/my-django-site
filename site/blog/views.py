from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Post
from blog.forms import CommentForm
from django.views import generic


class HomeView(generic.ListView):
    """
    Base Home View.
    """

    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        query_set = Post.objects.all().order_by('-date')[:3]
        return query_set


class PostsView(generic.ListView):
    """
    List View for all Post objects.
    """

    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]


class PostDetailView(generic.View):
    """
    DetailView for Post Object.
    Also serves CommentForm that collects Comments objects related to Post.
    """

    def get(self, request, slug):

        post = Post.objects.get(slug=slug)
        comment_form = CommentForm()

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form": comment_form,
        })

    def post(self, request, slug):

        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:post-detail', kwargs={"slug": slug}))

        return render(request, "blog/post-detail.html", {
            "post": post,
            "comment_form": comment_form,
        })


class ReadLaterView(generic.View):
    """"""

    def post(self, request):

        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        return redirect("blog:home")