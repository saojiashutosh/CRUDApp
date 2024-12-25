from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password  # Import make_password
from .models import user


def home(request):
    users = user.objects.all()

    return render(request,"index.html",{"users":users})

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if name and contact and email and password:
            # Hash the password before saving
            hashed_password = make_password(password)
            obj = user(name=name, contact=contact, email=email, password=hashed_password)
            obj.save()
            return HttpResponse("User Registered Successfully")
        else:
            return HttpResponse("An Error Occurred")
    return render(request, "signup.html")

def update(request,id):
    obj = user.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if check_password(password,obj.password):
            obj.name = name
            obj.contact = contact
            obj.email = email
            obj.save()

            return redirect('home')

    return render(request,"update.html",{"obj":obj})

def delete(request,id):
    obj = user.objects.get(id=id)
    obj.delete()
    return redirect("home")