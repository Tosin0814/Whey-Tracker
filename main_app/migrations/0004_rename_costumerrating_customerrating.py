# Generated by Django 4.1.1 on 2022-10-10 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_costumerrating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CostumerRating',
            new_name='CustomerRating',
        ),
    ]