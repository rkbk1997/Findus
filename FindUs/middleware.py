from django.shortcuts import HttpResponseRedirect
from django.urls import resolve
from findusapp.models import *
def login_register_middleware(get_response):
    def middleware(request):
        url_name=resolve(request.path_info).url_name
        if (url_name=='login' or url_name=='reg') and request.session['is_logged']==True:
            response=HttpResponseRedirect('userhome') 
        #elif (url_name=='login' or url_name=='reg') and request.session['is_logged']==True and data.role=='admin':
         #   response=HttpResponseRedirect('service')
        else:
            response=get_response(request)
        return response
    return middleware