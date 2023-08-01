from django.contrib import admin
from django.urls import path
from newPost import views as new_views
from post import views as post_views
from users import views as users_admin
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Blog post urls
    path('', post_views.home, name='home'),
    path('about/', post_views.about, name='about'),
    path('contact/', post_views.contact, name='contact'),
    path('single/<str:pk>', post_views.single, name='single'),
    path('search/', post_views.search, name='search'),
    path('sidebar/', post_views.sidebar, name='siderbar'),
    
     #admin Urls
    path('view_post/', new_views.view_post, name='view_post'),
    path('add_post/', new_views.add_post, name='add_post'), 
    path('update_post/<int:id>/', new_views.update_post, name='update_post'), 
    path('delete_view/<int:id>/', new_views.delete_post, name='delete_post'), 
    path('add_category/', new_views.add_category, name='add_category'),
    path('view_category/', new_views.view_category, name='view_category'),
    path('registration/', new_views.registration, name='registration'),
    path('view_user/', new_views.view_user, name='view_user'), 
    path('contact_us/', new_views.contact_us, name='contact_us'),
    path('comment/', new_views.comment, name='comment'),  
    path('subscribe/', new_views.subscribe, name='subscribe'),
    path('signout/', new_views.signout, name='signout'), 
    
    #login Urls
    path('SuperAdmin/', users_admin.SuperAdmin, name='superadmin'), 
    path('UserLogin/', users_admin.UserLogin, name='userlogin'), 
   
     
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

