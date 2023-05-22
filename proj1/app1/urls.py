from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.login_view),
    path('loginvalidation/', views.loginvalidation),
    path('logout/', views.logout_view),
    path('home/', views.home),
   
    path('form/', views.form),
    path('inventory/', views.inventory),
    path('about/', views.about),
    path('form2/', views.form2),
    path('submit/', views.submit),
    path('inventory2/', views.inventory2),
    path('save_print/', views.save_print),

    path('update/', views.update),

    path('add_item/', views.add_item),
    path('about/', views.about),

    #path('test/', views.test),

]