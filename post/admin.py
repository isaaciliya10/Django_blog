from django.contrib import admin
from .models import Category, Post,Comment,Contact1,EmailUs

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''
    list_display = ('title','created','Author','image','category') 
    search_fields = ['title']
    list_filter = ['title','created']
    

class CommentAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''
    list_display = ('post','name','created','email') 
    list_filter = ['name','created','email']
    search_fields = ['name']
    
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''
    list_display = ('first_name','body','created','email') 
    list_filter = ['first_name','created','email']
    search_fields = ['first_name']
    

class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''

    list_display = ['title']
    search_fields = ['title']
 

# Register your models here.
    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact1, ContactAdmin)
admin.site.register(EmailUs)


