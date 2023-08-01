from django.shortcuts import redirect, render
from post.forms import NewsForm, AddCategory
from post.models import Category, Post, Comment,EmailUs,Contact1
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages



#view post function
def view_post(request):
    count_post = Post.objects.all().count()
    post = Post.objects.all().order_by('-content')
    page = Paginator(post, 4)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    
    context={'count_post':count_post, 'page':page}
    return render(request, 'view_post.html',context)

#Update post function
def update_post(request,id):
   post = Post.objects.get(id=id)
   forms= NewsForm(request.POST or None, request.FILES or None, instance=post)
   if forms.is_valid():
             forms.save()
             messages.info(request, "Your post has been updated successfully")
             return redirect('view_post')
   else:   
        forms= NewsForm()             
        return render(request, 'add_post.html', {'forms':forms, 'post':post })

#Delete post function
def delete_post(request,id):
   post = Post.objects.get(id=id)
   if request.method == 'POST':
       post.delete()  
   return render(request, 'delete_post.html', {'post':post} )
    
#add post function
def add_post(request):
     if request.method == 'POST':
         forms= NewsForm(request.POST, request.FILES)
         if forms.is_valid():
             forms.save()
             messages.info(request, "Your post has been successfully submitted")
             return redirect('add_post')  
     else:   
        forms= NewsForm()             
        return render(request, 'add_post.html', {'forms':forms})

def registration(request):
    return render(request, 'registration.html')

def view_user(request):
    user_count = User.objects.all().count()
    user = User.objects.all()
    
    context = {
                'user_count':user_count,
                'user':user
             }
    return render(request, 'view_user.html', context)

def view_category(request): 
    cat_count = Category.objects.all().count()
    cat = Category.objects.all()
    
    context = {
                'cat':cat,
                'cat_count':cat_count
                
        
                }
    return render(request, 'view_category.html',context)

# add category function
def add_category(request): 
    if request.method == 'POST':
         forms=AddCategory(request.POST, request.FILES)
         if forms.is_valid():
            #  category = forms.save(commit=False)
            #  category.post = AddCategory
             forms.save()
             messages.info(request, "Your category has been sucessfully added")
             return redirect('add_category')
             
    else:
          forms = AddCategory()
    return render(request, 'add_category.html', {'forms':forms})

# comment function
def comment(request):
    count_comment = Comment.objects.all().count()
    comment = Comment.objects.all()
    
    context ={'count_comment':count_comment, 'comment':comment}
    return render(request, 'comment.html', context)

# subscribe function
def subscribe(request):
    count_subscribe  = EmailUs.objects.all().count()
    subscribe = EmailUs.objects.all()
    context ={'count_subscribe':count_subscribe , 'subscribe':subscribe }
    return render(request, 'subscribe.html', context)

# Contact us function
def contact_us(request):
    count_contact = Contact1.objects.all().count()
    contact = Contact1.objects.all()
    context ={'count_comment':count_contact, 'contact':contact }
    return render(request, 'subscribe.html', context)

# signout function
def signout(request):
    logout(request)
    messages.info(request, "You Have Successfully Logout")
    return redirect('userlogin')    

