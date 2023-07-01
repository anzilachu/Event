from django import forms
from posts.models import Post
from posts.models import Subscribe


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': "input"}), label="Tags (Comma separated)")

    class Meta:
        model = Post
        exclude = ('author', 'published_date', 'category')

        widgets = {
            "title" : forms.TextInput(attrs={'class': "input"}),
            "short_description" : forms.Textarea(attrs={'class': "input"})
        }

        error_messages = {
            "title" : {
                "required": "Title field is required"
            },
            "short_description" : {
                "required": "Short description field is required"
            },
            "tags" : {
                "required": "Tag field is required"
            },
            "featured_image" : {
                "required": "Featured image field is required"
            },
            "categories" : {
                "required": "Draft field is required"
            },
            "author" : {
                "required": "author field is required"
            },
            "published_date" : {
                "required": "published_date field is required"
            }, 
           
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email','book_date')

        widgets = {
            "book_date" : forms.TextInput(attrs={'type':'date'}),
        }