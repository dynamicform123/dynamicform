from django.urls import path
from .views import *
# from .views import form_builder, save_form,load_form


urlpatterns = [
    # path('admin/login/', views.admin_login, name='admin_login'),
    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('admin/create-form/', views.create_form, name='create_form'),
    # path('admin/delete-form/<int:form_id>/', views.delete_form, name='delete_form'),
    # path('logout/', views.logout_view, name='logout'),


    # path('register/', views.user_register, name='user_register'),
    # path('login/', views.user_login, name='user_login'),
    # path('dashboard/', views.user_dashboard, name='user_dashboard'),
    # path('logout/', views.user_logout, name='user_logout'),

    # path('form/<int:form_id>/', views.fill_form, name='fill_form'),

    # path('download-pdf/<int:submission_id>/', views.download_pdf, name='download_pdf'),
    # path('send-email/<int:submission_id>/', views.send_submission_email, name='send_submission_email'),
    # path('print/<int:submission_id>/', views.print_submission, name='print_submission'),

    # path("admin/form-builder/", form_builder, name="form_builder"),

    # path("admin/save-form/", save_form, name="save_form"),

    # path("admin/load-form/<int:form_id>/", load_form, name="load_form"),

    # path('form_view/', views.form_view, name='form_view'),







]

from django.urls import path
# from .views import studentregister_view, studentlogin_view, studentdashboard_view, studentsubmit_student_form, studentlogout_view

urlpatterns = [
    path('studentregister/', studentregister_view, name='register'),
    path('studentlogin/', studentlogin_view, name='login'),
    path('studentdashboard/', studentdashboard_view, name='dashboard'),
    path('studentsubmit-student-form/', studentsubmit_student_form, name='submit_student_form'),
    path('studentlogout/', studentlogout_view, name='logout'),
]


from django.urls import path
# from .views import profile_form_view, profile_list_view

urlpatterns = [
#     path('profile/', profile_form_view, name='profile_form'),
#     path('profiles/', profile_list_view, name='profile_list'),
# 
]


from django.urls import path
from . import views 
from .views import *

urlpatterns = [

    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/create-form/', views.create_form, name='create_form'),
    path('admin/delete-form/<int:form_id>/', views.delete_form, name='delete_form'),
    path('logout/', views.logout_view, name='logout'),

    path('form/<int:form_id>/', views.fill_form, name='fill_form'),

    path('download-pdf/<int:submission_id>/', views.download_pdf, name='download_pdf'),
    path('send-email/<int:submission_id>/', views.send_submission_email, name='send_submission_email'),
    path('print/<int:submission_id>/', views.print_submission, name='print_submission'),

    


    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', views.user_logout, name='user_logout'),

    path('form/<int:form_id>/', views.fill_form, name='fill_form'),

    path('download-pdf/<int:submission_id>/', views.download_pdf, name='download_pdf'),
    path('send-email/<int:submission_id>/', views.send_submission_email, name='send_submission_email'),
    path('print/<int:submission_id>/', views.print_submission, name='print_submission'),

    path('profile/', profile_form_view, name='profile_form'),
    path('profiles/', profile_list_view, name='profile_list'),


    path('dynamic-forms/', form_dynamic_list, name='form_dynamic_list'),
    path('dynamic-forms/create/', form_dynamic_create, name='form_dynamic_create'),
    path('dynamic-forms/update/<int:pk>/', form_dynamic_update, name='form_dynamic_update'),
    path('dynamic-forms/delete/<int:pk>/', form_dynamic_delete, name='form_dynamic_delete'),


    path('createforms/', form_list, name='form_list'),
    path('createforms/create/', form_create, name='form_create'),
    path('createforms/<int:form_id>/', form_detail, name='form_detail'),
    path('createforms/fields/add/', form_field_add, name='form_field_add'),


    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/update/<int:contact_id>/', contact_update, name='contact_update'),
    path('contacts/delete/<int:contact_id>/', contact_delete, name='contact_delete'),


    path("dashboard/", user_dashboard, name="user_dashboard"),
    path("load-form/", load_form, name="load_form"),
]
