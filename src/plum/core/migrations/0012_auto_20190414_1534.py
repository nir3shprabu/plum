# Generated by Django 2.2 on 2019-04-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190414_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pypi_name',
            new_name='package_name',
        ),
        migrations.AlterField(
            model_name='license',
            name='servers',
            field=models.ManyToManyField(related_name='licenses', to='core.Server'),
        ),
    ]