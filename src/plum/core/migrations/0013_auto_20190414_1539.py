# Generated by Django 2.2 on 2019-04-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190414_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='package_name',
            field=models.CharField(blank=True, max_length=190, null=True, unique=True),
        ),
    ]