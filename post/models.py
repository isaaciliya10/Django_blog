from django.db import models
import uuid


# Create your models here.

class Category(models.Model):
    '''Model definition for Category.'''

    title = models.CharField(max_length=200)   
     
    class Meta:
        '''Meta definition for Category.'''
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    '''Model definition for Post.'''
    
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    Author = models.CharField(max_length=100, default='Admin')
    content = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    

    class Meta:
        
        '''Meta definition for Post.'''
        
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    '''Model definition for Comment.'''

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        '''Meta definition for Comment.'''

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
    

class EmailUs(models.Model):
    '''Model definition for email.'''

    email = models.EmailField(max_length=225)   
     
    class Meta:
        
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email
    
    
class Contact1(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        
        '''Meta definition for Comment.'''

        verbose_name = 'Contact'
        verbose_name_plural = 'Conatcts'

    def __str__(self):
        return self.first_name