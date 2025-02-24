from django.contrib import admin

# Register your models here.


# <script>
#     function loadForm(formId) {
#         $.get(`/admin/load-form/${formId}/`, function (data) {
#             $("#drop-area").html(""); // Clear existing fields
#             data.fields.forEach(field => {
#                 let newField = `<div class="form-group"><label>${field.label}</label>`;
#                 if (field.type === "text") {
#                     newField += `<input type="text" class="form-control"></div>`;
#                 } else if (field.type === "date") {
#                     newField += `<input type="date" class="form-control"></div>`;
#                 }
#                 $("#drop-area").append(newField);
#             });
#         });
#     }
# </script>

from django.contrib import admin
from .models import DynamicField

@admin.register(DynamicField)
class DynamicFieldAdmin(admin.ModelAdmin):
    list_display = ("field_label", "field_type", "is_active")
    list_editable = ("is_active",)  # Allow enabling/disabling fields in the admin panel
