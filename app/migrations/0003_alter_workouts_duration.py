# Generated by Django 5.1.2 on 2024-12-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts',
            name='duration',
            field=models.CharField(max_length=30),
        ),
    ]
