# Generated by Django 3.1.6 on 2021-02-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
