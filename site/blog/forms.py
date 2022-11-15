from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for Comment object.
    """
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user_name'].widget.attrs.update(
    #         {'class': 'form-control'})
    #     self.fields['user_email'].widget.attrs.update(
    #         {'class': 'form-control'})
    #     self.fields['text'].widget.attrs.update(
    #         {'class': 'form-control'})

    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment",
            }