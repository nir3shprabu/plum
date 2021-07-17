# Generated by Django 3.2.5 on 2021-07-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20191112_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='deliverable_file_size',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_method',
            field=models.CharField(choices=[('pypi', 'PyPI'), ('pip', 'Local python package index'), ('bundled', 'Bundled'), ('file', 'File')], max_length=190, verbose_name='Delivery method'),
        ),
        migrations.AlterField(
            model_name='product',
            name='package_name',
            field=models.CharField(help_text='Should be a valid Python package name. For free packages, this is the name the package should have on on PyPI.', max_length=190, null=True, unique=True, verbose_name='Package name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]