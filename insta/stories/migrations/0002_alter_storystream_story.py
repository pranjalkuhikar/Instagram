# Generated by Django 4.1.4 on 2023-01-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storystream',
            name='story',
            field=models.ManyToManyField(related_name='storiess', to='stories.story'),
        ),
    ]
