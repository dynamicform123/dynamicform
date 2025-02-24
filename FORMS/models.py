from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=255)  
    created_at = models.DateField(auto_now_add=True)  
    updated_at = models.DateField(auto_now=True)  

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    LOCATION_CHOICES = [('Chennai', 'Chennai'), ('Pune', 'Pune'), ('Coimbatore', 'Coimbatore')]
    
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    designation = models.CharField(max_length=255)
    experience = models.CharField(max_length=20)
    preferred_location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    brief = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  
    form_banner = models.ImageField(upload_to='form_banners/', blank=True, null=True)

    def __str__(self):
        return self.name

class FormDynamic(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='dynamic_forms')
    banner_image = models.ImageField(upload_to='banners/', blank=True, null=True)
    validity = models.DateField()
    
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    accessible_users = models.TextField(help_text='Comma-separated email addresses')

    FIELD_CHOICES = [
        ('Text', 'Text'),
        ('Date', 'Date'),
        ('MultiSelect', 'MultiSelect'),
        ('HTML', 'HTML'),
    ]

    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_CHOICES)
    options = models.TextField(blank=True, null=True, help_text='Comma-separated values for dropdowns')
    is_required = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    is_prioritize = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.form.name} - {self.field_name}"

class Contact(models.Model):
    profile = models.CharField(max_length=255) 
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    zipcode = models.CharField(max_length=6)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.profile

from django.contrib.auth.models import AbstractUser
from django.db import models

class FormUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class FormSubmission(models.Model):
    user = models.ForeignKey(FormUser, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    data = models.JSONField()  
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.form.name}"

  



class DynamicField(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="fields", blank=True)
    field_type = models.CharField(
        max_length=50, 
        choices=[("Text", "Text"), ("Number", "Number"), ("Date", "Date"), ("Dropdown", "Dropdown")]
    )
    field_label = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.field_label


    #######
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    created_by = models.ForeignKey(FormUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

######





