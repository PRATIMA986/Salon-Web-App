# Generated by Django 5.0 on 2024-01-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50)),
                # ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                # ('country', models.Choices('Afganistan','India')),
                ('cname', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('yearofexperience', models.CharField(max_length=5)),
            ],
        ),
    ]
