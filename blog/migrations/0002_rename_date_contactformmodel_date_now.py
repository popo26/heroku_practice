# Generated by Django 4.0.4 on 2022-05-02 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactformmodel',
            old_name='date',
            new_name='date_now',
        ),
    ]