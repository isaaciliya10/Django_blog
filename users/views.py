from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login





# Create your views here.
#super admin and user registration  function and encryption
def SuperAdmin(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exixts.")
                return redirect('superadmin')
            
            elif User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists.")
                    return redirect('superadmin')
            
            else:
                user= User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                messages.info(request, "Your cccount has been created successfully")
                return redirect('userlogin')
        else:
             messages.info(request, "Password and confirm password are not the same")
             return redirect('superadmin')
    else:        
     return render(request, 'superadmin.html')

#user login function
def UserLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.info(request, "Your have login successfully")
            return redirect('add_post')
        else:
            messages.info(request, "Wrong login details")
    else:
     return render(request, 'userlogin.html')
    return redirect('userlogin')
    
# def logout(request):
#     logout(request)
#     messages.info(request, "You Have Successfully Logout")
#     return redirect('userlogin')    