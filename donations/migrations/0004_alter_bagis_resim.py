# Generated by Django 5.0.3 on 2024-06-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_alter_bagis_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagis',
            name='Resim',
            field=models.ImageField(blank=True, null=True, upload_to='djangouploads/donations'),
        ),
    ]
