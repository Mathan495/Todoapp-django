from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('delete-task/<int:name>/', views.Deletetask, name='delete'),
    path('update-task/<int:name>/', views.Update, name='update'),
    path('logout/', views.logout_view, name='logout'),
]