# Generated by Django 4.1.1 on 2022-10-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_rating_date_customerrating_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerrating',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='customerrating',
            old_name='review',
            new_name='value',
        ),
    ]
