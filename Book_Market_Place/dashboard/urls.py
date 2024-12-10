from django.urls import path
from dashboard import views

app_name = 'Dashboard'

urlpatterns = [
    path('user_dashboard/',views.user_Dashboard,name='User_Dashboard'),
]
