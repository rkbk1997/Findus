from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
from adminapp.models import *
from findusapp.models import *
from userapp.models import *
import json
import time

def page(request,option):
    if request.session.has_key('is_logged'):
        loc=Location.objects.filter(subcate=option)
        #print(loc)
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'page.html',{'loc':loc,'data':data,'data1':data1,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def page1(request,option):
    if request.session.has_key('is_logged'):
        pic=Cate.objects.filter(name=option).first()
        loc=Subcate.objects.filter(cate_id=pic.id)
        #print(loc)
        print(option)
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'page1.html',{'pic':pic,'loc':loc,'data':data,'data1':data1,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def page3(request,option):
    if request.session.has_key('is_logged'):
        #pic=Cate.objects.filter(name=option).first()
        loc=Location.objects.filter(subcate=option)
        #print(loc)
        print(option)
        print(loc)
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'page3.html',{'loc':loc,'data':data,'data1':data1,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')
# Create your views here.

info=time.strftime("%d/%m/%Y-%H:%M:%S")

def index(request):
    car=Location.objects.filter(subcate='car showroom')[:4]
    mob=Location.objects.filter(subcate='mobile')[:4]
    res=Location.objects.filter(subcate='restaurant')[:4]
    hot=Location.objects.filter(subcate='hotel')[:4]
    data=Cate.objects.all()
    data1=Subcate.objects.all()
    f=open('findusapp/static/states.json')
    state = json.load(f)
    state=(state.values())
    return render(request,'index.html',{'hot':hot,'data':data,'data1':data1,'state':state,'car':car,'mob':mob,'res':res})

def login(request):
    f=open('findusapp/static/states.json')
    state = json.load(f)
    state=(state.values())
    error=False
    try:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            data=Registration.objects.filter(username=username).first()
            if data.username==username and data.password==password and data.role=="admin":
                request.session['sunm']=username
                request.session['spass']=password
                request.session['is_logged']=True
                return redirect('service')
            elif data.username and data.password==password and data.role=="user" and data.status==1:
                request.session['sunm']=username
                request.session['spass']=password
                request.session['is_logged']=True
                return redirect('userhome')

            else:
                error=True
    except:
        error=True
    return render(request,'loginform.html',{'error':error,'state':state})

def Logout(request):
    request.session['is_logged']=False
    #request.session['sunm']=None
    logout(request)
    return redirect('index')

def reg(request):
    f=open('findusapp/static/states.json')
    state = json.load(f)
    state=(state.values())
    data=Registration.objects.all()
    user_taken = False
    email_taken = False
    password_match = False
    if request.method=='POST':
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        gender=request.POST['gender']
        city=request.POST['city']
        address=request.POST['address']
        if password1==password2:
            if Registration.objects.filter(username=username).exists():
                user_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            elif Registration.objects.filter(email=email).exists():
                email_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            else:
                Registration.objects.create(fname=fname,lname=lname,username=username,email=email,password=password1,gender=gender,city=city,address=address,status=0,role='user',info=info)
                subject = 'no-reply'
                message = "http://rkbk1998.pythonanywhere.com/verifyuser?email="+email
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponse("<h1>Thank For Register On Site We Will Send A Email Conformation Mail On Your Email Plz Comform That, Then Login The Site</h1>")
        else:
            password_match=True
            return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
        return redirect('reg')
    return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match,'state':state})

def show(request):
    if request.session.has_key('is_logged'):
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        if request.method=='POST':
            data2=request.POST['search']
            loc=Location.objects.filter(subcate=data2)
        return render(request,'show.html',{'data':data,'data1':data1,'state':state,'loc':loc,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def verifyuser(request):
    email=request.GET.get("email")
    print(email)
    data=Registration.objects.filter(email=email).first()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==data.username and password==data.password:
            data.status=1
            data.save()
            return HttpResponse("<h1>welcome</h1>"+username)
        else:
            return HttpResponse("<h1>Sorry You Not Valid User</h1>")
    return render(request,'verifyuser.html',{})

def contactindex(request):
    data=Cate.objects.all()
    data1=Subcate.objects.all()
    f=open('findusapp/static/states.json')
    state = json.load(f)
    state=(state.values())
    return render(request,'contactindex.html',{'data':data,'data1':data1,'state':state})

