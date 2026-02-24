from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
    path('recruiter-dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('seeker-dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('apply/<int:id>/', views.apply_job, name='apply_job'),
]