# Generated by Django 5.0.7 on 2024-07-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_item_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='box',
            field=models.CharField(default='', max_length=6),
        ),
    ]
