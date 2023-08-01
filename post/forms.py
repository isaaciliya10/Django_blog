from django import forms
from . models import Comment,Post,Category,EmailUs,Contact1

    
    
    
class CommentForm(forms.ModelForm):
    '''Form definition for Comment.'''

    class Meta:
        model = Comment
        fields = ('name','email','body')
    
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your name','required':'required'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Please your email','required':'required'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your comment content', 'rows':8, 'cols':10,'required':'required'}),
           
        }
        
        
    
class NewsForm(forms.ModelForm):
    '''Form definition for Post.'''

    class Meta:
        model = Post
        fields = "__all__"
        
        
        widgets={
            'category':forms.Select(attrs={'class':'form-control','name':'category','placeholder':'Please Select Category','required':'required'}),
            'title':forms.TextInput(attrs={'class':'form-control','name':'title','placeholder':'Please Enter The News Title','required':'required'}),
            'Author':forms.TextInput(attrs={'class':'form-control','name':'author'}),
            'content':forms.Textarea(attrs={'class':'form-control','rows':6, 'cols':8,'name':'content','placeholder':'Please Enter The News Content','required':'required' }),
            'image':forms.FileInput(attrs={'class':'form-control','Pleceholder':'Select Image From Your Device','required':'required'}),
        }
        
class AddCategory(forms.ModelForm):
    '''Form definition for Category.'''
    
    class Meta: 
        model = Category
        fields = "__all__"
    
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','name':'category','placeholder':'Please Enter New Category'}),
           
        }


class UserEmail(forms.ModelForm):
    '''Form definition for Category.'''
    
    class Meta: 
        model = EmailUs
        fields = "__all__"
    
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control','name':'emailus','placeholder':'Please Enter your Email'}),
           
        }
        
        
        
class ContactUs(forms.ModelForm):
    
    class Meta:
        model = Contact1
        fields = "__all__"
    
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Please your email'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your comment content', 'rows':8, 'cols':10}),
           
        }
        
         