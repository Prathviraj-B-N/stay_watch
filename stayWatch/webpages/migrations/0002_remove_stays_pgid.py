# Generated by Django 3.2.6 on 2021-08-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stays',
            name='pgid',
        ),
    ]
