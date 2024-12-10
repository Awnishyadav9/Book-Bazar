from django.urls import path,include
from book import views


app_name = 'book'

urlpatterns = [
    path('',views.home_view,name='Home'),
    path('register/',views.register_view,name='Register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='Logout'),
]