# Generated by Django 2.1.4 on 2019-05-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_search', '0002_auto_20190523_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]