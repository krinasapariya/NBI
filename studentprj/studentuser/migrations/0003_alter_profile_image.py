# Generated by Django 5.0.2 on 2024-03-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentuser', '0002_profile_bio_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pic'),
        ),
    ]