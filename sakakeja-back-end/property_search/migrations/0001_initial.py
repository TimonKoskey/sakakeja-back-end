# Generated by Django 2.1.4 on 2019-06-15 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('property_type', models.CharField(blank=True, max_length=50, null=True)),
                ('rent_or_sale', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_bedrooms', models.IntegerField(blank=True, null=True)),
                ('number_of_bathrooms', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('amount_to_be_paid', models.IntegerField(blank=True, null=True)),
                ('date_of_upload', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_accounts.Location')),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_accounts.DetailsOfUploader')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_search.Property')),
            ],
        ),
    ]
