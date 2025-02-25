# Generated by Django 5.1.5 on 2025-02-23 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FORMS', '0002_formsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(max_length=50)),
                ('field_label', models.CharField(max_length=255)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='FORMS.form')),
            ],
        ),
    ]
