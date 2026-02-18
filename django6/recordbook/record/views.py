from django.shortcuts import render, redirect
from .models import record
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


@login_required
def record_list(request):
    records = record.objects.all()
    return render(request, 'list.html', {'records': records})


def add_record(request):
    if request.method == 'POST':
        record.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            roll=request.POST['roll']
        )
        return redirect('record_list')
    return render(request, 'add.html')


def edit_record(request, id):
    record_obj = record.objects.get(id=id)

    if request.method == 'POST':
        record_obj.name = request.POST['name']
        record_obj.email = request.POST['email']
        record_obj.roll = request.POST['roll']
        record_obj.save()
        return redirect('record_list')

    return render(request, 'edit.html', {'records': record_obj})


def delete_record(request, id):
    record.objects.get(id=id).delete()
    return redirect('record_list')


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
             messages.error(request, "Username already exists")
             return redirect('register_user')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login_user')

    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('record_list')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login_user')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('login')
