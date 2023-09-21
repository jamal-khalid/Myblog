from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from blog.models import Post
import re

# Create your views here.
def home(request):
    viewss=Post.objects.filter(views__gt=5)
    print(viewss)
    context={'viewss':viewss}
    return render(request , 'home/home.html' , context)

def about(request):
    return render (request , 'home/about.html')

def contact(request):
    # messages.success(request ,"Ypur Form Has beem submited")
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request ,"Please Fill Your Form Properly ")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request , 'Your Form Has Been Submited Successfuly ')
        

    return render(request , 'home/contact.html')

def search(request):
    query=request.GET["query"]
    if len(query)>80:
        allPosts=Post.objects.none()
    else:
        allPoststitle=Post.objects.filter(title__icontains=query)
        allPostscontent=Post.objects.filter(content__icontains=query)
        allPosts=allPoststitle.union(allPostscontent)

    if allPosts.count()==0:
        messages.warning(request ,"Your Query is not exist . Please refine Your Query ")
    param={'allPosts':allPosts,'query':query}
    return render (request , 'home/search.html',param)

def handlesignup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"You have to choose username under Ten characters ")
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request ,"Your password Is Wrong Fill again")
            return redirect('home')
        
        if len(pass1)<8:
            messages.error(request,'Password LEngth minimum should be 8 characters')
            return redirect('home')
        
        if not re.search(r'[A-Z]', pass1):
            messages.error(request,'Atleast one character should be uppercase ')
            return redirect('home')
        
        if not re.search(r'[a-z]', pass1):
            messages.error(request,'Atleast one character should be lowercase ')
            return redirect('home')

        if not re.search(r'\d', pass1):
            messages.error(request,'Atleast one character should be Numbers ')
            return redirect('home')
    


        myuser= User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'Your Profile has been successfully Created In Vlogs_with_jamal')

        return redirect('home')
    else:
        return HttpResponse('404 record not found')
    
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername ,password=loginpassword)
        if user is not None:
            login(request ,user)
            messages.success(request,"You Have Successfully Loged In Vlogs_with_Jamal")
            return redirect('home')

        else:
            messages.error(request ,"Invalid Credentials ; Please Try Again")
            return redirect('home')
        
    return HttpResponse('404 record not found')


def handlelogout(request):
    logout(request)
    messages.success(request, "You Have Successfuly Loged Out From Vlogs_with_jamal")
    return redirect('home')
    




