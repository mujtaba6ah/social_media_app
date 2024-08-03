from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,UserRegistrationForm 


# Create your views here.
# this func for user login submiting 
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,username=data['username'],password=data['password']
            )
            if user is not None:
                login(request,user)
                return HttpResponse('user authenticated and logged in ')
            else:
                return HttpResponse('invalid user')



    else:
         form = LoginForm()
    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    logout(request)
  
    return render(request, 'users/logout.html')
@login_required
def index(request):
    return render(request,'users/index.html')

# this the view to user register:
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'users/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form})        