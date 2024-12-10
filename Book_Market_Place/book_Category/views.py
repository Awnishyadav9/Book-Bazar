from django.shortcuts import render,get_object_or_404,redirect
from .models import Book_Type
from .forms import All_Input_Model


def single_Book_Details(request,id):
    book_Info = get_object_or_404(Book_Type,id=id)
    related_Book = Book_Type.objects.filter(category= book_Info.category,is_sold=False).exclude(id=id)[0:3]
    return render(request,'category_templates/details.html',{'book_Info':book_Info,'related_Book':related_Book})


def add_New_Book(request):
    if request.method == 'POST':
        new_Book_Form = All_Input_Model(request.POST, request.FILES)
        if new_Book_Form.is_valid():
            item = new_Book_Form.save(commit=False)
            item.created_by =request.user
            item.save()
            new_Book_Form = All_Input_Model()
            return redirect('book_Category:SingleBook',id=item.id)
    else:
        new_Book_Form = All_Input_Model()
    return render(request,'category_templates/form.html',{'new_Book_Form':new_Book_Form})


def delete_Book(request,id):
    select_Book = get_object_or_404(Book_Type, id=id, created_by=request.user)
    select_Book.delete()
    return redirect('Dashboard:User_Dashboard')


def edit_Book(request,id):
    if request.method == "POST":
        update_Book = Book_Type.objects.get(id=id)
        edit_Book_Details = All_Input_Model(request.POST, instance=update_Book)
        if edit_Book_Details.is_valid():
            item = edit_Book_Details.save()
            item.created_by = request.user
            item.save()
            return redirect('book_Category:SingleBook',id = item.id)
    else:
        update_Book = Book_Type.objects.get(id=id)
        edit_Book_Details = All_Input_Model(instance=update_Book)
           
    return render(request,'dashboard_templates/update_Form.html',{'edit_Book_Details':edit_Book_Details})