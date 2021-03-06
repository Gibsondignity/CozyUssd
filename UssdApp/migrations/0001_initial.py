# Generated by Django 3.2.7 on 2022-03-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppartmentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=65, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=15, null=True)),
                ('firstName', models.CharField(max_length=65, null=True)),
                ('secondNumber', models.CharField(max_length=65, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=65, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
