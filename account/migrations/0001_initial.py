# Generated by Django 5.0.4 on 2024-05-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='ЭЛЕКТРОНДУК ДАРЕГИНИЗ')),
                ('name', models.CharField(max_length=50, verbose_name='АТЫНЫЗ')),
                ('last_name', models.CharField(max_length=70, verbose_name='ФАМИЛИЯНЫЗ')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('dateJoined', models.DateTimeField(auto_now_add=True)),
                ('activation_code', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
