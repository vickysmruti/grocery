# Generated by Django 3.1.1 on 2021-03-03 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total_items',
        ),
    ]
