# Generated by Django 5.1.4 on 2025-01-28 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_manager_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_card', models.CharField(max_length=10)),
                ('aadhar_card', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('image', models.ImageField(default=True, null=True, upload_to='')),
                ('fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.manager_data')),
            ],
        ),
    ]
