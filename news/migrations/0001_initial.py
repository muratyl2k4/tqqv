# Generated by Django 5.0.3 on 2024-06-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Baslik', models.CharField(blank=True, max_length=200, null=True)),
                ('Aciklama', models.TextField(blank=True, null=True)),
                ('Resim', models.ImageField(blank=True, null=True, upload_to='djangouploads/news')),
                ('Resim2', models.ImageField(blank=True, null=True, upload_to='djangouploads/news')),
                ('Resim3', models.ImageField(blank=True, null=True, upload_to='djangouploads/news')),
            ],
        ),
    ]
