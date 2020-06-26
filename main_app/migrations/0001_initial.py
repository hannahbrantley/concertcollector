# Generated by Django 3.0.5 on 2020-06-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('bestsongs', models.TextField(max_length=250)),
                ('notes', models.TextField(max_length=250)),
            ],
        ),
    ]