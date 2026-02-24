from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job,Application
from .forms import JobForm,Applicationform

def home(request):
    jobs=Job.objects.all().order_by('-created_at')
    return render(request,'jobs/home.html',{'jobs':jobs})

def job_detail(request,id):
    job=get_object_or_404(Job,id=id)
    return render(request,'jobs/job_detail.html',{'job':job})

@login_required
def post_job(request):

    # Role restriction
    if request.user.profile.role != "RECRUITER":
        return redirect('home')

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def recruiter_dashboard(request):
    jobs=Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/recruiter_dashboard.html', {'jobs': jobs})

@login_required
def seeker_dashboard(request):
     applications = Application.objects.filter(applicant=request.user)
     return render(request, 'jobs/seeker_dashboard.html', {'applications': applications})

@login_required
def apply_job(request, id):

    # Role restriction
    if request.user.profile.role != "JOB_SEEKER":
        return redirect('home')

    job = get_object_or_404(Job, id=id)

    # Prevent duplicate application
    if Application.objects.filter(job=job, applicant=request.user).exists():
        return redirect('home')

    if request.method == "POST":
        form = Applicationform(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('seeker_dashboard')
    else:
        form = Applicationform()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})
            