# Generated by Django 3.1.7 on 2021-05-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('Display', models.CharField(max_length=50)),
                ('Operating_System', models.CharField(max_length=50)),
                ('CPU', models.CharField(max_length=50)),
                ('Screen', models.CharField(max_length=50)),
                ('Processor', models.CharField(max_length=50)),
                ('battery', models.CharField(max_length=50)),
                ('Memory', models.CharField(max_length=50)),
            ],
        ),
    ]