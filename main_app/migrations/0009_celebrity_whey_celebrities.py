# Generated by Django 4.1.1 on 2022-10-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_customerrating_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(choices=[('M', 'Musician'), ('A', 'Actor'), ('S', 'Athlete'), ('O', 'Other')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='whey',
            name='celebrities',
            field=models.ManyToManyField(to='main_app.celebrity'),
        ),
    ]