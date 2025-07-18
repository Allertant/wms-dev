# Generated by Django 4.1.2 on 2025-07-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockBinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_name', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_qty', models.BigIntegerField(default=0, verbose_name='Binstock Qty')),
                ('pick_qty', models.BigIntegerField(default=0, verbose_name='BinPick Qty')),
                ('picked_qty', models.BigIntegerField(default=0, verbose_name='BinPicked Qty')),
                ('bin_size', models.CharField(max_length=255, verbose_name='Bin size')),
                ('bin_property', models.CharField(max_length=255, verbose_name='Bin Property')),
                ('t_code', models.CharField(max_length=255, verbose_name='Transaction Code')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('create_time', models.DateTimeField(verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Stock Bin',
                'verbose_name_plural': 'Stock Bin',
                'db_table': 'stockbin',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='StockListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_qty', models.BigIntegerField(default=0, verbose_name='Total Qty')),
                ('onhand_stock', models.BigIntegerField(default=0, verbose_name='On Hand Stock')),
                ('can_order_stock', models.BigIntegerField(default=0, verbose_name='Can Order Stock')),
                ('ordered_stock', models.BigIntegerField(default=0, verbose_name='Ordered Stock')),
                ('inspect_stock', models.BigIntegerField(default=0, verbose_name='Inspect Stock')),
                ('hold_stock', models.BigIntegerField(default=0, verbose_name='Holding Stock')),
                ('damage_stock', models.BigIntegerField(default=0, verbose_name='Damage Stock')),
                ('asn_stock', models.BigIntegerField(default=0, verbose_name='ASN Stock')),
                ('dn_stock', models.BigIntegerField(default=0, verbose_name='DN Stock')),
                ('pre_load_stock', models.BigIntegerField(default=0, verbose_name='Pre Load Stock')),
                ('pre_sort_stock', models.BigIntegerField(default=0, verbose_name='Pre Sort Stock')),
                ('sorted_stock', models.BigIntegerField(default=0, verbose_name='Sorted Stock')),
                ('pick_stock', models.BigIntegerField(default=0, verbose_name='Pick Stock')),
                ('picked_stock', models.BigIntegerField(default=0, verbose_name='Picked Stock')),
                ('back_order_stock', models.BigIntegerField(default=0, verbose_name='Back Order Stock')),
                ('supplier', models.CharField(default='', max_length=255, verbose_name='Goods Supplier')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Stock List',
                'verbose_name_plural': 'Stock List',
                'db_table': 'stocklist',
                'ordering': ['-id'],
            },
        ),
    ]
