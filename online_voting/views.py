def about_us(request):
    return render(request, 'about-us.html')

def our_services(request):
    return render(request, 'our-services.html')


from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404 
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
def contact_us(request):
    return render(request, 'contact-us.html')

def reg(request):
 
    return render(request, 'register.html')
                  
def register_view(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email') 
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        myfile = request.FILES['id_proof']
        fs = FileSystemStorage()    
        filename = fs.save(myfile.name, myfile)
        ins=register(name=name,email=email,phone=phone,password=password,id_proof=filename)
        ins.save()
        return  render(request,'register.html',{'msg':'Registered Successfully'})


def login(request):
    return render(request, 'login.html')

def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
         request.session['details'] = 'admin'
         return render(request,'index.html')

    elif register.objects.filter(email=email,password=password).exists():
        users=register.objects.get(email=email,password=password)
        request.session['uid']=users.id
        return render(request,'index.html')
    

    elif election_commission.objects.filter(email=email,password=password).exists():
        wrk=election_commission.objects.get(email=email,password=password)
        request.session['wid']=wrk.id
        return render(request,'index.html')
    else:
         return render(request, 'login.html', {'message':'Invalid Email or Password'})
    


def logout_view(request):
    # Clear session
    request.session.flush()
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


def viewuser(request):
    users=register.objects.all()
    return render(request,'viewregister.html',{'user':users})