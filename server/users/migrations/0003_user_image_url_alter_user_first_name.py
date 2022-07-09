# Generated by Django 4.0.5 on 2022-07-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(blank=True, default='https://avatars.dicebear.com/api/bottts/pandeu.svg?scale=97&colors[]=blue', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='broken fire', max_length=30),
        ),
    ]
