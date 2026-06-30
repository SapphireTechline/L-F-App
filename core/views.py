from django.shortcuts import render,redirect
from core.models import *
from django.http import HttpResponse
from django.db.models import Q
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



# Create your views here.

def index(request):
    item_name = request.GET.get('item_name')

    if item_name:
        top_items = Submit.objects.filter(
            Q(item_name__icontains=item_name) |
            Q(location__icontains=item_name)
        )
    else:
        top_items = Submit.objects.order_by('-created_at')[:3]

    context = {
        "top_two_items": top_items
    }

    return render(request,'index.html', context)




@login_required
def my_posts(request):
    post= Submit.objects.filter(user=request.user).order_by('-created_at')

    context={
        "post":post
    }
    return render(request,'my_post.html',context)


def login_view(request):
     
    if request.user.is_authenticated:
        return redirect('homepage')
     

     
    if request.method == 'POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username, password=password)


        
        if user is not None:
            login(request, user)   
            return redirect('homepage')
        
        else:
            return render(request, "login.html", {
                'error': 'Invalid username or password'
            })


    return render(request, "login.html")

       

    
@login_required(login_url='/login')
def submit_item(request):

    if request.method == "POST":

        item_name = request.POST.get('item_name')
        description = request.POST.get('description_of_item')
        department=request.POST.get('department')
        faculty=request.POST.get('faculty')
        location = request.POST.get('location')
        status = request.POST.get('status')
        profile_pic = request.FILES.get('profile_pic') 

        Submit.objects.create(
            user=request.user,
            item_name=item_name,
            description_of_item=description,
            faculty=faculty,
            department=department,
            location=location,
            status=status,
            profile_pic=profile_pic
        )

        return redirect('homepage')  # or success page

    return render(request, "submit.html")

   
    
@login_required(login_url='/login')
def all_item(request):

    item_name = request.GET.get('item_name')

    if item_name:
        items = Submit.objects.filter(
            Q(item_name__icontains=item_name) |
            Q(location__icontains=item_name)  |
            Q(status__icontains=item_name)
        ).order_by('-created_at')
    else:
        items = Submit.objects.all()

    context = {
        "items": items
    }

    return render(request,"allitem.html",context)

def register(request):
    if request.method == 'POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        User.objects.create_user(first_name= fname ,last_name =lname ,email=email,username=username,password=password)
        
       

        return redirect('login')

    return render(request, "register.html")



def signout(request):

    if request.method == "POST":
        logout(request)

    return redirect('homepage')



@login_required
def delete_item(request, id):
    post= Submit.objects.filter(user=request.user).order_by('-created_at')

    if request.method == "POST":
        post.delete()
        return redirect('my_posts')
