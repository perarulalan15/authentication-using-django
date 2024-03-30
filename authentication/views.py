from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        myuser = User.objects.create_user(email,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        return redirect("signin")

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']

        user = authenticate(username=email,password=password1)

        if user is not None:
            login(request,user)
            email = user.email
            return render(request,"authentication/index.html",{'email':email})
        
        else:
            messages.error(request,"Invalid Credentials!")
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully.")
    return redirect('home')