# Generated by Django 4.0.3 on 2022-06-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('firstname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]