from django.shortcuts import render, redirect
from django.db.models import Q
from portal.models import *

# Create your views here.

def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        data = request.POST
        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        print(full_name,email,password, confirm_password)

        Signup.objects.create(
            full_name = full_name,
            email = email,
            password = password,
            confirm_password = confirm_password
        )

        return redirect("/home/")

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        
        print(email, password)

        return redirect('/home/')

    return render(request, "login.html")


def job(request):
    queryset = AddJob.objects.all()
    context = {'jobs' : queryset}
    job_title = request.GET.get("job_title")
    job_location = request.GET.get("job_location")
    job_type = request.GET.get("job_type")
    if (job_title is not None and job_title == "") or (job_location is not None and job_location == "") or (job_type is not None and job_type == ""):
        queryset = AddJob.objects.filter(
            Q(job_title = job_title) | Q(job_location = job_location) | Q(job_type = job_type)
        )
        context = {'jobs' : queryset}
    return render(request, "job.html",context)

def addJob(request):
    if request.method == "POST":

        print('hello-----------------------')
        data = request.POST

        job_title = data.get("job_title")
        job_description = data.get("job_description")
        job_type = data.get("job_type")
        job_location = data.get("job_location")

        print(job_title,job_description,job_type,job_location)

        AddJob.objects.create(
            job_title = job_title,
            job_description = job_description,
            job_type = job_type,
            job_location = job_location
        )

        return redirect("/addjob/")

    return render(request, "addjob.html")