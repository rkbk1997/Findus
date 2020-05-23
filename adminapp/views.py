from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from adminapp.form import *
from findusapp.models import *
from adminapp.models import *
from userapp.models import *
import json
# Create your views here.
def service(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'service.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def viewfeedback(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data=Feedback.objects.order_by('id')[::-1]
        return render(request,'viewfeedback.html',{'state':state,'data':data,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def Edit_Delete_feedback(request,sid,option):
    if request.session.has_key('is_logged'):
        data=Feedback.objects.filter(id=sid).first()
        if option=='Delete':
            data.delete()
            return redirect('viewfeedback')
        return render(request,'viewfeedback.html',{'data':data})
    return redirect('login')

def Send_Message(request):
    if request.session.has_key('is_logged'):
        if request.method=='POST':
            email=request.POST['email']
            message=request.POST['message']
            file=request.FILES['file']
            subject = 'no reply'
            recipient_list=[email]
            email_from = settings.EMAIL_HOST_USER
            email1=EmailMessage( subject, message, email_from, recipient_list)
            email1.attach(file.name,file.read(),file.content_type)
            email1.send()
            return redirect('viewfeedback')
    return redirect('login')

def addnotification(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data=Notification.objects.order_by('id')[::-1]
        if request.method=="POST":
            date=request.POST['date']
            des=request.POST['des']
            Notification.objects.create(date=date,des=des)
            return redirect('addnotification')
        return render(request,'addnotification.html',{'state':state,'data':data,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def Edit_Delete_note(request,sid,option):
    if request.session.has_key('is_logged'):
        data=Notification.objects.filter(id=sid).first()
        if option=='Delete':
            data.delete()
            return redirect('addnotification')
        if option=='Edit':
            if request.method=='POST':
                data.date=request.POST['date']
                data.des=request.POST['des']
                data.save()
            return redirect('addnotification')
        return render(request,'addnotification.html',{'data':data})
    return redirect('login')

def addcate(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data=Cate.objects.all()
        if request.method=="POST" or request.method=="FILES":
            form=CateForm(request.POST,request.FILES)
            if form.is_valid():
                    try:
                        form.save()
                        return redirect('addcate')
                    except:
                        print("error")
            else:
                    form=CateForm()
        return render(request,'addcate.html',{'state':state,'data':data,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def Edit_Delete_cate(request,sid,option):
    if request.session.has_key('is_logged'):
        data=Cate.objects.filter(id=sid).first()
        if option=='Delete':
            data.delete()
            return redirect('addcate')
        if option =='Edit':
            #if request.method=="POST" or request.method=="FILES":
            form=CateForm(request.POST,request.FILES, instance=data)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('addcate')
                except:
                    print("error")
        else:
            form=CateForm()
            return redirect('addcate')
        return render(request,'addcate.html',{'data':data})
    return redirect('login')

def subcate(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        if request.method=='POST':
            cate_id=request.POST['cate_id']
            nameofsubcate=request.POST['nameofsubcate']
            cat = Cate.objects.all().filter(id=cate_id).first()
            Subcate.objects.create(cate=cat,nameofsubcate=nameofsubcate)
            return redirect('subcate')
        return render(request,'subcatepage.html',{'state':state,'data':data,'data1':data1,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def Edit_Delete_subcate(request,sid,option):
    if request.session.has_key('is_logged'):
        data1=Subcate.objects.filter(id=sid).first()
        if option=='Delete':
            data1.delete()
            return redirect('subcate')
        if option =='Edit':
            if request.method=="POST" or request.method=="FILES":
                data1.cate=request.POST['cate']
                data1.nameofsubcate=request.POST['nameofsubcate']
                data1.save()
                return redirect('subcate')
        return render(request,'subcatepage.html',{'data1':data1})
    return redirect('login')

def userview(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data=Registration.objects.all()
        return render(request,'userview.html',{'state':state,'data':data,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def Edit_Delete_user(request,sid,option):
    if request.session.has_key('is_logged'):
        data=Registration.objects.filter(id=sid).first()
        if option=='Delete':
            data.delete()
            return redirect('userview')
        if option =='unblock':
            data.status=1
            data.save()
            return redirect('userview')
        if option=='block':
            data.status=0
            data.save()
            return redirect('userview')
        return render(request,'userview.html',{'data':data})
    return redirect('login')

def admineditprofile(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        sunm=request.session['sunm']
        data=Registration.objects.filter(username=sunm).first()
        if request.method=='POST':
            data.fname=request.POST['fname']
            data.lname=request.POST['lname']
            data.username=request.POST['username']
            data.email=request.POST['email']
            data.password=request.POST['password']
            data.address=request.POST['address']
            data.save()
        return render(request,'admineditprofile.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass'],'data':data})
    return redirect('login')


def map(request):
    f=open('findusapp/static/states.json')
    state = json.load(f)
    state=(state.values())
    sunm=request.session['sunm']
    l=Location.objects.all()
    if request.method=='POST':
        lt=request.POST['lt']
        map=request.POST['map']
        data=Location.objects.filter(location_title=lt).first()
        data.map=map
        data.save()
    return render(request,'map.html',{'l':l,'state':state,'sunm':request.session['sunm']})
