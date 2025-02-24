from django.urls import path
from . import views 
from .views import *

urlpatterns = [

    ## Admin Login url

    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/create-form/', views.create_form, name='create_form'),
    path('admin/delete-form/<int:form_id>/', views.delete_form, name='delete_form'),
    path('logout/', views.logout_view, name='logout'),

    
 ## User Login url

    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
    path("user_dashboard/", user_dashboard, name="user_dashboard"),
    path("load-form/", load_form, name="load_form"),


# Basic forms url
    path('profile/', profile_form_view, name='profile_form'),
    path('profiles/', profile_list_view, name='profile_list'),
    path('profiles/<int:pk>/edit/', profile_update_view, name='profile_update'),
    path('profiles/<int:pk>/delete/', profile_delete_view, name='profile_delete'),
    path('download-pdf/<int:submission_id>/', views.download_pdf, name='download_pdf'),
    path('send-email/<int:submission_id>/', views.send_submission_email, name='send_submission_email'),
    path('print/<int:submission_id>/', views.print_submission, name='print_submission'),
    path('form/<int:form_id>/', views.fill_form, name='fill_form'),


## Basic Forms valid url

    path('dynamic-forms/', form_dynamic_list, name='form_dynamic_list'),
    path('dynamic-forms/create/', form_dynamic_create, name='form_dynamic_create'),
    path('dynamic-forms/update/<int:pk>/', form_dynamic_update, name='form_dynamic_update'),
    path('dynamic-forms/delete/<int:pk>/', form_dynamic_delete, name='form_dynamic_delete'),



## Contacts Forms url
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/update/<int:contact_id>/', contact_update, name='contact_update'),
    path('contacts/delete/<int:contact_id>/', contact_delete, name='contact_delete'),


   
## Forms Urls
    path('createforms/', form_list, name='form_list'),
    path('createforms/create/', form_create, name='form_create'),
    path('createforms/<int:form_id>/', form_detail, name='form_detail'),
    path('createforms/fields/add/', form_field_add, name='form_field_add'),
]
