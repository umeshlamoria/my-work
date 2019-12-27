from django import forms
from .models import Post,UserProfile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','text',)

class UserLogin(UserCreationForm):
	class Meta:
		 model=User
		 fields=('username','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email')

class UserProfilePic(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('profile_pic',)

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=('name','email','website','mobile','text')