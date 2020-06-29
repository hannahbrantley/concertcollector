# Generated by Django 3.0.5 on 2020-06-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='concert',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='concert',
            name='artists',
            field=models.ManyToManyField(to='main_app.Artist'),
        ),
    ]
