# Generated by Django 3.1.7 on 2021-06-27 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_searched_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_product2',
            old_name='img_url1',
            new_name='query',
        ),
        migrations.RemoveField(
            model_name='new_product2',
            name='category',
        ),
        migrations.RemoveField(
            model_name='new_product2',
            name='price',
        ),
        migrations.RemoveField(
            model_name='new_product2',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='new_product2',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='new_product2',
            name='sub_category',
        ),
    ]