# Generated by Django 3.2.11 on 2022-01-07 20:29

from django.db import migrations, models
import plum.core.models.product


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20210718_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='android_package_name',
            field=models.CharField(max_length=190, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=plum.core.models.product.icon_filename),
        ),
        migrations.AddField(
            model_name='productversion',
            name='android_index_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_method',
            field=models.CharField(choices=[('pypi', 'PyPI'), ('pip', 'Local python package index'), ('bundled', 'Bundled'), ('android', 'Android app'), ('file', 'File'), ('external', 'External store')], max_length=190, verbose_name='Delivery method'),
        ),
    ]
