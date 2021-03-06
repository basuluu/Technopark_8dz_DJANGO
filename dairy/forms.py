from django import forms
from .models import Post, Comment, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'vision')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
)

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
)
