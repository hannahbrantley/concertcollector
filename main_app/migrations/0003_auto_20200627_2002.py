# Generated by Django 3.0.5 on 2020-06-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200627_1958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artist',
            new_name='Opener',
        ),
        migrations.RenameField(
            model_name='concert',
            old_name='artists',
            new_name='openers',
        ),
    ]
