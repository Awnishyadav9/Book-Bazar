from django.urls import path,include
from . import views

app_name = 'book_Category'

urlpatterns = [
    path('Single_book/<int:id>/', views.single_Book_Details,name='SingleBook'),
    path('new_Book/',views.add_New_Book,name='Addbook'),
    path('delete_Single_book/<int:id>/',views.delete_Book,name='DeleteBook'),
    path('Update/<int:id>/',views.edit_Book,name='EditBook')
]