# Generated by Django 2.1.4 on 2019-05-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_search', '0004_auto_20190527_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='for_rent',
        ),
        migrations.RemoveField(
            model_name='property',
            name='for_sale',
        ),
        migrations.AddField(
            model_name='property',
            name='rent_or_sale',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]