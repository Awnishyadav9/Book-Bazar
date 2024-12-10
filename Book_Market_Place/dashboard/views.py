from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile_Model
from book.forms import signup_Form
from django.contrib.auth.models import User
from book_Category.models import Book_Type

def user_Dashboard(request):
    user_All_Book = Book_Type.objects.filter(created_by = request.user)
    signup_All_Data = signup_Form()
    user_All_Data = Profile_Model.objects.all()
    if request.method =='POST': 
        signup_All_Data = signup_Form(request.POST)
        
    return render(request, 'dashboard_templates/mybook.html',{'user_All_Book':user_All_Book,'user_All_Data':user_All_Data,'signup_All_Data':signup_All_Data})



