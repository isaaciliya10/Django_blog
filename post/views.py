from django.shortcuts import redirect, render
from django.db.models import Q
from . models import Comment, Post,EmailUs
from . forms import CommentForm,UserEmail,ContactUs
from django.contrib import messages
from django.core.paginator import Paginator



# Create your views here.
def home(request):
  
    posts = Post.objects.all().order_by('-content')
    page = Paginator(posts, 4)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    visited = Post.objects.all()[:4]
    
    if request.method == 'POST':
         sidebar = UserEmail(request.POST)
           
         if sidebar.is_valid():
             sidebar = sidebar.save(commit=False)
             sidebar.post = EmailUs
             sidebar.save()
             messages.info(request, "Thank you for subscribe to our newsletter")
             return redirect('/')
             
    else:
           sidebar = UserEmail() 
    context={ 'page':page,
             'visited':visited,
             'sidebar':sidebar
             }
    return render(request, 'index.html', context)

def sidebar(request):
    sidebar = UserEmail()
    return render(request, 'sidebar.html',{'sidebar':sidebar})


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
         forms = ContactUs(request.POST)
         if forms.is_valid():
             contact = forms.save(commit=False)
             contact.post = ContactUs
             contact.save()
             messages.info(request, "Thank you for contact us we will get back you shortly")
             return redirect('contact')
             
    else:
         forms=ContactUs() 
         
    return render(request, 'contact.html', {'contact1': forms})

def single(request, pk):
    count_comment = Comment.objects.all().count()
    commentlist = Comment.objects.all()
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
         forms = CommentForm(request.POST)
         
         if forms.is_valid():
             comment = forms.save(commit=False)
             comment.post = posts
             comment.save()
             return redirect('/')
             
    else:
         forms= CommentForm() 
         
         context={'posts':posts, 
                  'forms':forms, 
                  'commentlist':commentlist,
                  'count_comment':count_comment }
           
    return render(request, 'single.html', context)

def search(request):
    visited = Post.objects.all()[:4]
    if request.method =='POST':
        search = request.POST['search_bar']
        dbsearched = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        
    context={
                'visited':visited, 
                'dbsearched':dbsearched
             }
    return render(request, 'search.html', context)

 
 