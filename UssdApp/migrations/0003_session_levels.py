# Generated by Django 3.2.7 on 2022-03-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UssdApp', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='session_levels',
            fields=[
                ('session_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=25, null=True)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
    ]