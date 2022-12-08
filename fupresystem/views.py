from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db.models import Count
from django.http import HttpResponse
# from datetime import datetime
# x=datetime.now



# Create your views here.

def index(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        phone=request.POST['phone']
        company=request.POST['company']
        
        data=response(firstname=firstname,lastname=lastname,address=address,phone=phone,company=company)
        data.save()
        return render(request,'submitted.html')
    else:
        pass
    return render(request,'index.html')



def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def submitted(request):
    return render(request, 'submitted.html')

def adminlogin(request):
    if request.method=='POST':
        try:
            log=login.objects.get(username=request.POST['username'],password=request.POST['password'])
            return redirect('adminlanding')
        except login.DoesNotExist as e:
            messages.info(request,'Invalid username or password.')
    return render(request,'adminlogin.html')

def dashboard(request):
    list=response.objects.all()
    context={
        'list' : list
    }
    return render(request,'dashboard.html',context)

# def adminlanding2(request):
#     loglist=login.objects.all()
#     content={
#         'loglist' : loglist
#     }
#     return render(request,'adminlanding.html',content)
# def showme(request):
#     loglist=login.objects.all()
#     context={
#         'loglist' : loglist
#     }
#     return render(request, 'adminlanding.html',context)
def adminlanding(request):
    # current_date = datetime.date()
    list=response.objects.all()
    loglist=login.objects.all()
    context={
        'list' : list,
        'loglist' : loglist
    }
    return render(request, 'adminlanding.html',context)
    

def del_item(request,myid):
    delitem=response.objects.get(id=myid)
    delitem.delete()
    return redirect('dashboard')