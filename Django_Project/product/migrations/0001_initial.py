# Generated by Django 4.1.5 on 2023-02-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_title', models.CharField(max_length=100)),
                ('pro_price', models.CharField(max_length=50)),
                ('pro_description', models.CharField(max_length=200)),
                ('pro_color', models.CharField(max_length=50)),
                ('pro_size', models.CharField(max_length=10)),
                ('pro_img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
