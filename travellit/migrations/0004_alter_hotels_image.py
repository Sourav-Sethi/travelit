# Generated by Django 5.0.3 on 2024-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellit', '0003_alter_hotels_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
