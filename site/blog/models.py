from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    """Class for Post object."""

    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts")
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)
    content = models.TextField(
        validators=[MinLengthValidator(10)]
        )
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, related_name="posts", null=True
    )
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)


    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):

    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption


class Comment(models.Model):
    """"""
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=120)
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name}: {self.user_email}"