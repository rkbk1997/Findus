from django.urls import path
from  findusapp import views
from django.conf import settings
urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('reg',views.reg,name='reg'),
    path('logout',views.Logout,name='logout'),
    path('verifyuser',views.verifyuser,name='verifyuser'),
    path('show',views.show,name='show'),
    path('contactindex',views.contactindex,name='contactindex'),
    path('^page(?P<option>[\w-]+)$',views.page,name='page'),
    path('^page1(?P<option>[\w-]+)$',views.page1,name='page1'),
    path('^page3(?P<option>[\w-]+)$',views.page3,name='page3'),
    
    
]