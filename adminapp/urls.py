from django.urls import path
from .import views
urlpatterns = [
    path('service',views.service,name='service'),
    path('addcate',views.addcate,name='addcate'),
    path('subcate',views.subcate,name='subcate'),
    path('userview',views.userview,name='userview'),
    path('addnotification',views.addnotification,name='addnotification'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('Send_Message',views.Send_Message,name='Send_Message'),
    path('admineditprofile',views.admineditprofile,name='admineditprofile'),
    path('map',views.map,name='map'),
    path('^edit_delete_cate/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',views.Edit_Delete_cate,name="edit_delete_cate"),
    path('^edit_delete_subcate/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',views.Edit_Delete_subcate,name="edit_delete_subcate"),
    path('^edit_delete_user/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',views.Edit_Delete_user,name="edit_delete_user"),
    path('^edit_delete_feedback/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',views.Edit_Delete_feedback,name="edit_delete_feedback"),
    path('^edit_delete_note/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',views.Edit_Delete_note,name="edit_delete_note"),
]