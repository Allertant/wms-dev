# Generated by Django 4.1.2 on 2025-07-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DispatchListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=255, verbose_name='Driver Name')),
                ('dn_code', models.CharField(max_length=255, verbose_name='DN Code')),
                ('contact', models.BigIntegerField(default=0, verbose_name='Contact Number')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Dispatch List',
                'verbose_name_plural': 'Dispatch List',
                'db_table': 'dispatchlist',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=255, verbose_name='Driver Name')),
                ('license_plate', models.CharField(max_length=255, verbose_name='License Plate')),
                ('contact', models.CharField(max_length=255, verbose_name='Contact Number')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Driver',
                'db_table': 'driver',
                'ordering': ['driver_name'],
            },
        ),
    ]
