from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from findusapp.models import *
from adminapp.models import *
from userapp.models import *
from userapp import state_city_list
import json
import time
# Create your views here.
info=time.strftime("%d/%m/%Y-%H:%M:%S")

def userhome(request):
    if request.session.has_key('is_logged'):
        car=Location.objects.filter(subcate='car showroom')[:4]
        mob=Location.objects.filter(subcate='mobile')[:4]
        res=Location.objects.filter(subcate='restaurant')[:4]
        hot=Location.objects.filter(subcate='hotel')[:4]

        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'userhome.html',{'hot':hot,'res':res,'mob':mob,'car':car,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass'],'data':data,'data1':data1})
    return redirect('login')

def contactus(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'contactus.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def addlocation(request):
    if request.session.has_key('is_logged'):
        cate=Cate.objects.all()
        slist=state_city_list.fetchstatelist()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        uob=Registration.objects.filter(username=request.session['sunm']).first()
        vid=uob.id
        if request.method=='POST' or request.method=="FILES":
            state=request.POST['state']
            city=request.POST['city']
            locality=request.POST['locality']
            cate=request.POST['cate']
            subcate=request.POST['subcate']
            location_title=request.POST['location_title']
            des=request.POST['des']
            img1=request.FILES['img1']
            img2=request.FILES['img2']
            img3=request.FILES['img3']
            img4=request.FILES['img4']
            Location.objects.create(state=state,city=city,locality=locality,cate=cate,subcate=subcate,location_title=location_title,des=des,img1=img1,img2=img2,img3=img3,img4=img4,v_status=0,info=info,vid=vid)
            return redirect('addlocation')
        return render(request,'addlocation.html',{'state':state,'cate':cate,'slist':slist,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def viewloaction(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        uob=Registration.objects.filter(username=request.session['sunm']).first()
        vid=uob.id
        data=Location.objects.all()
        newdata=[]
        for i in data:
            if i.vid==vid:
                newdata.append(i)
        PAYPAL_URL="https://www.sandbox.paypal.com/cgi-bin/webscr"
        PAYPAL_ID="sb-vj47lg1212144@business.example.com"
        return render(request,'viewlocation.html',{'PAYPAL_URL':PAYPAL_URL,'PAYPAL_ID':PAYPAL_ID,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass'],'data':newdata})
    return redirect('login')

def fetchcity(request):
    snm=request.GET.get('snm')
    #print(snm)
    clist=state_city_list.fetchcitylist(snm)
    cityoptlist=["<option>Select city</option>"]
    for x in clist:
        cityoptlist.append("<option>"+x+"</option>")
    return HttpResponse(cityoptlist)

def fetchsubcate(request):
    snm=request.GET.get('snm')
    data1=Cate.objects.filter(name=snm).first()
    data=Subcate.objects.all()
    subcateoptlist=["<option>Select Subcate</option>"]
    for i in data:
        if i.cate_id==data1.id:
            subcateoptlist.append("<option>"+i.nameofsubcate+"</option>")
    print(subcateoptlist)
    return HttpResponse(subcateoptlist)

def aboutus(request):
    if request.session.has_key('is_logged'):
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'aboutUs.html',{'sunm':request.session['sunm'],'spass':request.session['spass'],'data':data,'data1':data1,'state':state})
    return redirect('login')

def notification(request):
    if request.session.has_key('is_logged'):
        data=Notification.objects.all()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'notification.html',{'state':state,'data':data,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def addfeedback(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            message=request.POST['message']
            Feedback.objects.create(name=name,email=email,message=message)
            return redirect('notification')
        return render(request,'notification.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def editprofile(request):
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
        return render(request,'editprofile.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass'],'data':data})
    return redirect('login')

def usermore(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'usermore.html',{'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def contactsms(request):
    if request.session.has_key('is_logged'):
        if request.method=='POST':
            name=request.POST['name']
            message=request.POST['message']
            email=request.POST['email']
            subject =request.POST['subject']
            message=request.POST['message']
            recipient_list=[email]
            email_from = settings.EMAIL_HOST_USER
            message1='Email Id='+email+'\n'+message
            email1=EmailMessage( subject, message1, email_from, recipient_list)
            email1.send()
            return redirect('contactus')
    return redirect('login')

def payment(request):
    vid=request.GET.get("vid")
    price=request.GET.get("price")
    uname=request.GET.get("sunm")
    locid=request.GET.get("lid")
    data=Location.objects.filter(id=locid).first()
    data.v_status=1
    data.save()
    Payment.objects.create(uid=vid,amount=price,loc_id=locid,info=info)
    return redirect('viewloaction')

def payment_histroy(request):
    if request.session.has_key('is_logged'):
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        data1=Registration.objects.filter(username=request.session['sunm']).first()
        vid=data1.id
        print(vid)
        d=Payment.objects.all()
        data=[]
        for i in d:
            if i.uid==vid:
                data.append(i)
                print(i.uid)
        print(data)
        return render(request,'payment_histroy.html',{'data':data,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')

def itemview(request,sid):
    if request.session.has_key('is_logged'):
        data=Location.objects.filter(id=sid).first()
        f=open('findusapp/static/states.json')
        state = json.load(f)
        state=(state.values())
        return render(request,'itemview.html',{'data':data,'state':state,'sunm':request.session['sunm'],'spass':request.session['spass']})
    return redirect('login')