from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('delete-task/<int:id>/', views.Deletetask, name='delete'),
    path('update-task/<int:id>/', views.Update, name='update'),
    path('logout/', views.logout_view, name='logout'),
]