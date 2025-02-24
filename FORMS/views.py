from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Form, FormDynamic, Contact
from .forms import AdminLoginForm, FormDynamicForm

def admin_login(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})

@login_required
def admin_dashboard(request):
    forms = Form.objects.all()
    return render(request, 'admin_dashboard.html', {'forms': forms})

@login_required
def create_form(request):
    if request.method == "POST":
        form = FormDynamicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FormDynamicForm()
    return render(request, 'create_form.html', {'form': form})

@login_required
def delete_form(request, form_id):
    form = Form.objects.get(id=form_id)
    form.delete()
    return redirect('admin_dashboard')

def logout_view(request):
    logout(request)
    return redirect('admin_login')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('userdashboard')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'userdashboard.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def user_dashboard(request):
    user_email = request.user.email
    available_forms = FormDynamic.objects.filter(accessible_users__icontains=user_email, status='Active')
    return render(request, 'userdashboard.html', {'forms': available_forms})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FormDynamic, FormSubmission

@login_required
@csrf_exempt
def fill_form(request, form_id):
    form = get_object_or_404(FormDynamic, id=form_id)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            FormSubmission.objects.create(user=request.user, form=form, data=data)
            return JsonResponse({"message": "Form submitted successfully!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return render(request, 'fill_form.html', {'form': form})


########

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import FormSubmission

def download_pdf(request, submission_id):
    submission = FormSubmission.objects.get(id=submission_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{submission.form.form.name}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Form Name: {submission.form.form.name}")
    p.drawString(100, 730, f"User: {submission.user.email}")
    p.drawString(100, 710, "Submitted Data:")

    y_position = 690
    for key, value in submission.data.items():
        p.drawString(120, y_position, f"{key}: {value}")
        y_position -= 20

    p.showPage()
    p.save()
    return response
######
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_submission_email(request, submission_id):
    submission = FormSubmission.objects.get(id=submission_id)
    subject = f"Form Submission: {submission.form.form.name}"
    html_message = render_to_string('email_template.html', {'submission': submission})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, 'your-email@gmail.com', [submission.user.email], html_message=html_message)
    return HttpResponse("Email sent successfully!")

#####

from django.shortcuts import render

def print_submission(request, submission_id):
    submission = FormSubmission.objects.get(id=submission_id)
    return render(request, 'print_submission.html', {'submission': submission})


def download_pdf(request, submission_id):
    submission = FormSubmission.objects.get(id=submission_id)
    if submission.user != request.user:
        return HttpResponse("Unauthorized", status=403)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{submission.form.form.name}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Form Name: {submission.form.form.name}")
    p.drawString(100, 730, f"User: {submission.user.email}")
    p.drawString(100, 710, "Submitted Data:")

    y_position = 690
    for key, value in submission.data.items():
        p.drawString(120, y_position, f"{key}: {value}")
        y_position -= 20

    p.showPage()
    p.save()
    return response


from django.shortcuts import render

def form_builder(request):
    return render(request, "admin_form_builder.html")
######

# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Form, DynamicField

# @csrf_exempt
# def save_form(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         form = Form.objects.create(name=data["name"], created_by=request.user)

#         for field in data["fields"]:
#             DynamicField.objects.create(form=form, field_label=field["label"], field_type=field["type"])

#         return JsonResponse({"message": "Form saved successfully!"})

# #

# def load_form(request, form_id):
#     form = Form.objects.get(id=form_id)
#     fields = form.fields.all()
#     field_data = [{"label": field.field_label, "type": field.field_type} for field in fields]
    
#     return JsonResponse({"name": form.name, "fields": field_data})


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Form, DynamicField, FormSubmission

def form_view(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    fields = DynamicField.objects.filter(form=form, is_active=True)  # Show only active fields
    
    if request.method == "POST":
        data = {field.field_label: request.POST.get(field.field_label, '') for field in fields}
        FormSubmission.objects.create(user=request.user, form=form, data=data)

        
        return JsonResponse({"message": "Form submitted successfully!"})
    
    return render(request, "form_template.html", {"form": form, "fields": fields})


from django.shortcuts import render
from .models import FormSubmission

def submission_list(request):
    submissions = FormSubmission.objects.all().order_by("-submitted_at")
    return render(request, "submission_list.html", {"submissions": submissions})

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

def edit_submission(request, submission_id):
    submission = get_object_or_404(FormSubmission, id=submission_id)
    
    if request.method == "POST":
        submission.data = request.POST.dict()  # Update data
        submission.save()
        return JsonResponse({"message": "Submission updated successfully!"})
    
    return render(request, "edit_submission.html", {"submission": submission})



#############3

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required

def studentregister_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})







from django.contrib.auth import authenticate, login, logout

def studentlogin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')


@login_required
def studentdashboard_view(request):
    if request.user.is_authenticated:
        form = StudentForm()
        students = Student.objects.filter(created_by=request.user)
        return render(request, 'accounts/dashboard.html', {'form': form, 'students': students})
    return redirect('login')


@login_required
def studentsubmit_student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            return redirect('dashboard')
    return redirect('dashboard')


def studentlogout_view(request):
    logout(request)
    return redirect('login')



from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

# Profile Form View
def profile_form_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    
    return render(request, 'formbuilder/profile_form.html', {'form': form})

# Profile List View
def profile_list_view(request):
    profiles = UserProfile.objects.all()
    return render(request, 'formbuilder/profile_list.html', {'profiles': profiles})



from django.shortcuts import render, redirect, get_object_or_404
from .models import FormDynamic
from .forms import FormDynamicForm

# 📌 List View for Dynamic Forms
def form_dynamic_list(request):
    forms = FormDynamic.objects.all().order_by('sort_order')
    return render(request, 'FORMS/form_dynamic_list.html', {'forms': forms})

# 📌 Create View for Dynamic Forms
def form_dynamic_create(request):
    if request.method == 'POST':
        form = FormDynamicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('form_dynamic_list')
    else:
        form = FormDynamicForm()
    return render(request, 'FORMS/form_dynamic_form.html', {'form': form})

# 📌 Update View for Dynamic Forms
def form_dynamic_update(request, pk):
    form_instance = get_object_or_404(FormDynamic, pk=pk)
    if request.method == 'POST':
        form = FormDynamicForm(request.POST, request.FILES, instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect('form_dynamic_list')
    else:
        form = FormDynamicForm(instance=form_instance)
    return render(request, 'FORMS/form_dynamic_form.html', {'form': form})

# 📌 Delete View for Dynamic Forms
def form_dynamic_delete(request, pk):
    form_instance = get_object_or_404(FormDynamic, pk=pk)
    if request.method == 'POST':
        form_instance.delete()
        return redirect('form_dynamic_list')
    return render(request, 'FORMS/form_dynamic_delete.html', {'form': form_instance})


#########3

from django.shortcuts import render, redirect
from .models import Form
from .forms import FormCreateForm, DynamicFormFieldForm

# List all forms
def form_list(request):
    forms = Form.objects.all()
    return render(request, 'form_list.html', {'forms': forms})

# Create a new form
def form_create(request):
    if request.method == 'POST':
        form = FormCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_list')
    else:
        form = FormCreateForm()
    return render(request, 'form_create.html', {'form': form})

# View form details
def form_detail(request, form_id):
    form = Form.objects.get(id=form_id)
    fields = DynamicFormFieldForm.objects.filter(form=form)
    return render(request, 'form_detail.html', {'form': form, 'fields': fields})

# Add fields to a form
def form_field_add(request):
    if request.method == 'POST':
        form = DynamicFormFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_list')
    else:
        form = DynamicFormFieldForm()
    return render(request, 'form_field_add.html', {'form': form})
########
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# List all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'formbuilder/contact_list.html', {'contacts': contacts})

# Create a new contact
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'formbuilder/contact_create.html', {'form': form})

# Update an existing contact
def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'formbuilder/contact_update.html', {'form': form})

# Delete a contact
def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'formbuilder/contact_delete.html', {'contact': contact})
###########

def load_form(request):
    form_type = request.GET.get("form_type")  # Get selected form type
    if form_type == "UserProfile":
        form = UserProfileForm()
    elif form_type == "contact":
        form = ContactForm()
    else:
        form = None

    return render(request, "form_partial.html", {"form": form})