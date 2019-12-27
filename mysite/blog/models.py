from django.db import models
from django.conf import settings
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from django.urls import reverse

STATUS_CHOICES=[('A','Active'),('D','Draft'),('P','published')]

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

	def __str__(self):
		return self.user.username

class Post(models.Model):
	category=models.ManyToManyField('Categorie')
	tag=models.ManyToManyField('Tag')	
	title=models.CharField(max_length=60)
	slug=AutoSlugField(populate_from='title',editable=True)
	text=models.TextField()
	create_date=models.DateTimeField(default=timezone.now())
	keyword=models.CharField(max_length=200,blank=True)
	meta_title=models.CharField('meta title',max_length=40,blank=True)
	meta_description=models.TextField('meta description',blank=True)
	thumbnail=models.ImageField(blank=True)
	featured=models.ImageField(blank=True)
	view=models.IntegerField(default=0)
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	published_date=models.DateTimeField(blank=True,null=True)
	status=models.CharField(max_length=1,choices=STATUS_CHOICES,blank=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def slug_fun(self,content):
		return content.replace('_','-').lower()

	def image_tag(self):
		# used in the admin site model as a "thumbnail"
		if self.thumbnail:
			return mark_safe('<img src="%s" width="40px" height="42px" />' % self.thumbnail.url)
		else:
			return 'No Image Found'
	image_tag.short_description = 'Thumbnail'
	
	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'slug':str(self.slug)})

class Comment(models.Model):
	post=models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comments')
	author=models.CharField(max_length=200,blank=True)
	name=models.CharField(max_length=20,blank=True)
	text=models.TextField(default=False)
	create_date=models.DateTimeField(default=timezone.now())
	approved_comments=models.BooleanField(default=False)
	mobile=models.IntegerField(max_length=12,default=False)
	email=models.EmailField(max_length=40,blank=True)
	website=models.URLField(max_length=160,blank=True)
	parent=models.ForeignKey('self',null=True,on_delete=models.CASCADE, related_name='replies')

	def approve(self):
		self.approved_comments=True
		self.save()

	def __str__(self):
		return self.name

class Categorie(models.Model):
	category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
	title=models.CharField(max_length=60)
	slug=AutoSlugField(populate_from='title',editable=True)
	content=models.TextField()
	utimestamp=models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title

	def slug_fun(self,content):
		return content.replace('_','-').lower()

class Tag(models.Model):
	title=models.CharField(max_length=60)
	slug=AutoSlugField(populate_from='title',editable=True)
	content=models.TextField()
	utimestamp=models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title

	def slug_fun(self,content):
		return content.replace('_','-').lower()