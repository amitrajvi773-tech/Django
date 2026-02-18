from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name="record_list"),
    path('add/', views.add_record, name="add_record"),
    path('edit/<int:id>/', views.edit_record, name="edit_record"),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register_user, name='register'),

]
