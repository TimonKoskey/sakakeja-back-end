# Generated by Django 2.1.4 on 2019-06-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailsofuploader',
            old_name='location',
            new_name='office_location',
        ),
        migrations.AddField(
            model_name='detailsofuploader',
            name='office_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
