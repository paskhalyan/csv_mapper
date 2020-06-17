# Generated by Django 3.0.7 on 2020-06-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_doc', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('app_name', models.CharField(max_length=255)),
            ],
        ),
    ]