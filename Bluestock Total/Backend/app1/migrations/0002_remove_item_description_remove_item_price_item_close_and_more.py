# Generated by Django 5.0.7 on 2024-07-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='item',
            name='Close',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='Issue_Type',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='Issue_size',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='Listing_Date',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='Open',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='Price_Band',
            field=models.CharField(default='Not Issued', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Not Issued', max_length=255),
        ),
    ]
