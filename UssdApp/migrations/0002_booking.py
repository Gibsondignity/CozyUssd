# Generated by Django 3.2.7 on 2022-03-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UssdApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=65, null=True)),
                ('phoneNumber', models.CharField(max_length=65, null=True)),
                ('num_of_people', models.IntegerField(default=0, null=True)),
                ('num_of_adults', models.IntegerField(default=0, null=True)),
                ('num_of_children', models.IntegerField(default=0, null=True)),
                ('checkin', models.DateTimeField(auto_now_add=True)),
                ('checkout', models.DateTimeField(auto_now_add=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]