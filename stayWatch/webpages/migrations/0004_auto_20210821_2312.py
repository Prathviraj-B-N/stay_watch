# Generated by Django 3.2.6 on 2021-08-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_owner_staydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='staydetails',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='staydetails',
            name='sid',
        ),
        migrations.AddField(
            model_name='stays',
            name='addr_line1',
            field=models.CharField(default='na', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stays',
            name='addr_line2',
            field=models.CharField(default='na', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stays',
            name='description',
            field=models.TextField(default='na'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stays',
            name='pincode',
            field=models.CharField(default='na', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stays',
            name='state',
            field=models.CharField(default='na', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='owner',
        ),
        migrations.DeleteModel(
            name='StayDetails',
        ),
        migrations.AddField(
            model_name='tenant',
            name='stay',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpages.stays'),
        ),
        migrations.AddField(
            model_name='stays',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpages.landlord'),
        ),
    ]