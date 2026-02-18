from django.shortcuts import render, redirect,get_object_or_404
from .models import record
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


@login_required
def record_list(request):
    records = record.objects.filter(user=request.user)
    return render(request, 'records/list.html', {'records': records})


def add_record(request):
    if request.method == 'POST':
        record.objects.create(
            user=request.user,
            name=request.POST['name'],
            email=request.POST['email'],
            roll=request.POST['roll']
        )
        return redirect('record_list')
    return render(request, 'records/add.html')



def edit_record(request, id):
    record_obj = get_object_or_404(record, id=id, user=request.user)

    if request.method == 'POST':
        record_obj.name = request.POST['name']
        record_obj.email = request.POST['email']
        record_obj.roll = request.POST['roll']
        record_obj.save()
        return redirect('record_list')

    return render(request, 'records/edit.html', {'record': record_obj})



def delete_record(request, id):
    record_obj = get_object_or_404(record, id=id, user=request.user)
    record_obj.delete()
    return redirect('record_list')

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
             messages.error(request, "Username already exists")
             return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'records/register.html')


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
            return redirect('login')
    return render(request, 'records/login.html')


def log_out(request):
    logout(request)
    return redirect('login')
