from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import signup_Form
from book_Category.models import Book_Type , Category

# Register
def register_view(request):
    if request.method == 'POST':
        form = signup_Form(request.POST)
        if form.is_valid():
            form.save()
            form = signup_Form()
            return redirect('book:login')
    else:
        form = signup_Form()
    return render(request,'registration/register.html',{'register_form':form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name= form.cleaned_data['username']
            pwd= form.cleaned_data['password']
            user = authenticate(request, username = name, password = pwd)
            if user is not None:
                login(request, user)
                return redirect('book:Home')
    else:
        form = AuthenticationForm()
    return render(request,'registration/login.html',{'login_form': form})

# Logout part
def logout_view(request):
    logout(request)
    return redirect('book:Home')

# View all data from data Base
def home_view(request):
    book_Data = Book_Type.objects.filter(is_sold = False)[0:6]
    all_Book_Category = Category.objects.all()
    return render(request,'book_templates/index.html',{'book_Data':book_Data,"all_Book_Category":all_Book_Category})

