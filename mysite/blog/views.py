from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,UserProfile,Comment,Tag,Categorie
from django.utils import timezone
from .forms import PostForm,UserLogin,UserProfilePic,UserProfileForm,CommentForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='login')
def logout_request(request):
	logout(request)
	messages.info(request,'Logout successfully')
	return redirect('login')

#@login_required(login_url='home')
def login_request(request):
	if request.method=='POST':
		form=AuthenticationForm(request,request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					messages.success(request,'You are now login')
					return HttpResponseRedirect(reverse('post_list'))
				#return render(request,'blog/login_error.html')
			if not request.user.is_authenticated:
				return render(request,'blog/home.html')
	else:
		form=AuthenticationForm()
		return render(request,'blog/login.html',{'form':form})

def register(request):
	registered=False
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			login(request,user)
			registered=True
			return redirect('register')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request,'blog/register.html',{'form':form})
	form=UserCreationForm
	return render(request,'blog/register.html',{'form':form,'registered':registered})

def user_list(request):
	users=User.objects.all()
	return render(request,'blog/user_list.html',{'users':users})

def user_detail(request,pk):
	user=get_object_or_404(User,pk=pk)
	return render(request,'blog/user_detail.html',{'user':user})

def user_edit(request,pk):
	user=User.objects.get(pk=pk)
	if request.method=='POST':
		form=UserProfileForm(request.POST,instance=user)
		profile_form=UserProfilePic(request.POST,request.FILES,instance=user)
		if form.is_valid() and UserProfilePic() :
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=form
			if 'profile_pic' in request.FILES:
				profile.profile_pic=request.FILES['profile_pic']
			profile.save()
			return redirect('user_detail',pk=user.pk)
	else:
		form=UserProfileForm(instance=user)
		profile_form=UserProfilePic(instance=user)
		return render(request,'blog/user_edit.html',{'form':form,'profile_form':profile_form})

def home(request):
	return render(request,'blog/home.html',{})


def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def tags(request,slug):
	tag=get_object_or_404(Tag,slug=slug)
	posts=Post.objects.filter(tag=tag)
	return render(request,'blog/tag.html',{'posts':posts,'tag':tag})

def categorys(request,slug):
	category=Categorie.objects.get(slug=slug)
	post=Post.objects.filter(category=category)
	return render(request,'blog/category.html',{'post':post,'category':category})

def post_detail(request,slug):
	post=get_object_or_404(Post,slug=slug)
	#image=Post.objects.all()
	comments=Comment.objects.filter(post=post, parent=None)
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			text=request.POST.get('text')
			name=request.POST.get('name')
			reply_id=request.POST.get('comment_id')
			comment_qs=None
			if reply_id:
				comment_qs=Comment.objects.get(id=reply_id)
			comment=Comment.objects.create(post=post,parent=comment_qs,text=text,name=name)
			comment.save()
			return redirect('post_detail',slug=post.slug)
	else:
		form=CommentForm()
	return render(request,'blog/post_detail.html',{'post':post,'form':form,'comments':comments})

def post_new(request):
	if request.method=='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',slug=post.slug)
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,slug):
	post=Post.objects.get(slug=slug)
	if request.method=='POST':
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', slug=post.slug)
	else:
		form=PostForm(instance=post)
		return render(request,'blog/post_edit.html',{'form':form})
