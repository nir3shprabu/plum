# Generated by Django 3.2.5 on 2021-07-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210717_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='productversion',
            options={'ordering': ('-release_date', '-pk')},
        ),
        migrations.AddField(
            model_name='product',
            name='external_store_url',
            field=models.URLField(blank=True, verbose_name='External store URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_method',
            field=models.CharField(choices=[('pypi', 'PyPI'), ('pip', 'Local python package index'), ('bundled', 'Bundled'), ('file', 'File'), ('external', 'External store')], max_length=190, verbose_name='Delivery method'),
        ),
    ]