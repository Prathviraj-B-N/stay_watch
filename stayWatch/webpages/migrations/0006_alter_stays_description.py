# Generated by Django 3.2.6 on 2021-08-21 18:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_stays_isfeatured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stays',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
