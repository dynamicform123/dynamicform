from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    class Meta:
        model =FormUser
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['profile', 'mobile', 'email', 'address', 'zipcode', 'country']

class FormSubmission(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = '__all__'
        
class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Hide password field

    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'dob', 'designation', 'experience', 'preferred_location', 'brief', 'username', 'password', 'form_banner']


class FormDynamicForm(forms.ModelForm):
    class Meta:
        model = FormDynamic
        fields = [
            'form', 'banner_image', 'validity', 'status', 'accessible_users',
            'field_name', 'field_type', 'options', 'is_required',
            'is_public', 'is_prioritize', 'sort_order'
        ]
        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
            'accessible_users': forms.Textarea(attrs={'rows': 2}),
            'options': forms.Textarea(attrs={'rows': 2}),
        }

class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name']

class DynamicFormFieldForm(forms.ModelForm):
    class Meta:
        model = DynamicField
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'phone']

