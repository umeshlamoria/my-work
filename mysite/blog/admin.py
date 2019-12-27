from django.contrib import admin
from .models import Post,Categorie,Comment,Tag,UserProfile
from django.urls import reverse
#from django.utils.html import format_html
#from imagekit.admin import AdminThumbnail

class InLineComment(admin.StackedInline):
	model=Comment
	extra=0

class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','image_tag','view','published_date','status',)
	search_fields=('title','slug',)
	filter_horizontal=('category',)
	list_editable=('view',)
	list_filter=('title',)
	autocomplete_fields=('tag',)
	actions=['post_active','post_draft',]
	inlines=[InLineComment]

	def post_active(modeladmin,request,queryset):
		queryset.update(status='A')
	post_active.short_description="Selected posts as Active"

	def post_draft(modeladmin,request,queryset):
		posts=queryset.update(status='D')
		posts=request.user
		posts.save()
	post_draft.short_description='Selected posts as Draft'

class CommentAdmin(admin.ModelAdmin):
	list_display=('post','text','name','mobile','email','parent',)
	search_fields=('name','text','mobile','email')

class TagAdmin(admin.ModelAdmin):
	list_display=('title','slug','content','utimestamp')
	search_fields=('title','utimestamp')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Categorie)
#admin.site.register(Comment)
#admin.site.register(Tag)
admin.site.register(UserProfile)