from django.urls import path
from .import views
urlpatterns = [
    path('userhome',views.userhome,name='userhome'),
    path('notification',views.notification,name='notification'),
    path('addfeedback',views.addfeedback,name='addfeedback'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('usermore',views.usermore,name='usermore'),
    path('contactus',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('addlocation',views.addlocation,name='addlocation'),
    path('fetchcity', views.fetchcity,name='fetchcity'),
    path('fetchsubcate',views.fetchsubcate,name='fetchsubcate'),
    path('viewloaction',views.viewloaction,name='viewloaction'),
    path('contactsms',views.contactsms,name='contactsms'),
    path('payment',views.payment,name='payment'),
    path('payment_histroy',views.payment_histroy,name='payment_histroy'),
    path('^itemview(?P<sid>[0-9]+)$',views.itemview,name="itemview"),
    
]