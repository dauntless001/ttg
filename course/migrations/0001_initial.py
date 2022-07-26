# Generated by Django 4.0.5 on 2022-07-10 15:54

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
                ('level', models.CharField(choices=[('NDI', 'Ndi'), ('NDII', 'Ndii'), ('HNDI', 'Hndi'), ('HNDII', 'Hndii')], default='NDI', max_length=10)),
                ('lecturer', models.CharField(max_length=30)),
                ('department', auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'ordering': ['name', 'created_at'],
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
