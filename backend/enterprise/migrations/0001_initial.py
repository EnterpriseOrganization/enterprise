# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enterprise.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelfnumber', models.CharField(blank=True, db_column='shelfNumber', max_length=45, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
                ('newestinwarehousedate', models.DateTimeField(auto_now=True, db_column='newestInWarehouseDate')),
            ],
            options={
                'managed': True,
                'db_table': 'inventorinformation',
            },
        ),
        migrations.CreateModel(
            name='InWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indate', models.DateTimeField(auto_now_add=True, db_column='inDate')),
                ('checker', models.CharField(max_length=45, null=True)),
                ('operator', models.CharField(max_length=45, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'inwarehouse',
            },
        ),
        migrations.CreateModel(
            name='InwareHouseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('inwarehouse', models.ForeignKey(db_column='inwarehouseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.InWarehouse')),
            ],
            options={
                'managed': True,
                'db_table': 'inwarehouseproduct',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='MaterialClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_field', models.CharField(db_column='class', default='the very based class', max_length=45)),
                ('parent_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.MaterialClass')),
            ],
            options={
                'managed': True,
                'db_table': 'materialclass',
            },
        ),
        migrations.CreateModel(
            name='MaterialRequistion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributiondate', models.DateTimeField(auto_now_add=True, db_column='distributionDate')),
                ('requistioner', models.CharField(blank=True, max_length=45, null=True)),
                ('checker', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'materialrequistion',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('indentor', models.CharField(max_length=45, null=True)),
                ('receiver', models.CharField(max_length=45, null=True)),
                ('checker', models.CharField(max_length=45, null=True)),
                ('recevieraddress', models.CharField(db_column='recevierAddress', max_length=200, null=True)),
                ('indentorphonenumber', models.CharField(db_column='indentorPhoneNumber', max_length=45, null=True)),
                ('totalprice', models.DecimalField(db_column='totalPrice', decimal_places=0, max_digits=3, null=True)),
                ('status', models.IntegerField(default=0)),
                ('deliverydate', models.DateTimeField(auto_now_add=True, db_column='deliveryDate')),
                ('paymentway', models.CharField(db_column='paymentWay', default='default paymentway', max_length=45)),
            ],
            options={
                'managed': True,
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('order', models.ForeignKey(db_column='orderID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Order')),
            ],
            options={
                'managed': True,
                'db_table': 'orderproduct',
            },
        ),
        migrations.CreateModel(
            name='OutProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('material', models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material')),
            ],
            options={
                'managed': True,
                'db_table': 'outproduct',
            },
        ),
        migrations.CreateModel(
            name='OutWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdate', models.DateTimeField(auto_now_add=True, db_column='outDate')),
                ('receiver', models.CharField(max_length=45, null=True)),
                ('checker', models.CharField(max_length=45, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'outwarehouse',
            },
        ),
        migrations.CreateModel(
            name='ProduceTaskBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personincharge', models.CharField(blank=True, db_column='personInCharge', max_length=45, null=True)),
                ('topic', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.IntegerField(default=0, validators=[enterprise.models.TaskStatusValidator])),
                ('archivedate', models.DateTimeField(blank=True, db_column='accurateDate', null=True)),
                ('number', models.IntegerField(default=0)),
                ('begindate', models.DateTimeField(auto_now_add=True, db_column='beginDate')),
                ('deadline', models.DateField(null=True)),
                ('material_getter', models.CharField(default='', max_length=100)),
                ('material_checker', models.CharField(default='', max_length=100)),
                ('material_distributon_date', models.DateTimeField(null=True)),
                ('order', models.ForeignKey(blank=True, db_column='orderID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Order')),
            ],
            options={
                'managed': True,
                'db_table': 'producetaskbasic',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3)),
            ],
            options={
                'managed': True,
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_field', models.CharField(db_column='class', default='the very based class', max_length=45)),
                ('parent_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.ProductClass')),
            ],
            options={
                'managed': True,
                'db_table': 'productclass',
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=800, null=True)),
                ('material', models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material')),
                ('product', models.ForeignKey(db_column='productID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Product')),
            ],
            options={
                'managed': True,
                'db_table': 'productmaterial',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser', models.CharField(max_length=45, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('checker', models.CharField(max_length=45, null=True)),
                ('totalprice', models.DecimalField(db_column='totalPrice', decimal_places=0, default=0, max_digits=3)),
            ],
            options={
                'managed': True,
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('material', models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material')),
                ('purchase', models.ForeignKey(db_column='purchaseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Purchase')),
            ],
            options={
                'managed': True,
                'db_table': 'purchaseproduct',
            },
        ),
        migrations.CreateModel(
            name='RequisitionMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('material', models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material')),
                ('requisition', models.ForeignKey(db_column='requisitionID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.MaterialRequistion')),
            ],
            options={
                'managed': True,
                'db_table': 'requisitionmaterial',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('permission', models.CharField(max_length=32, null=True)),
                ('positionname', models.CharField(db_column='positionName', max_length=45, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
                ('contact', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(db_column='phoneNumber', max_length=45, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='SupplierMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('material', models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material')),
                ('supplier', models.ForeignKey(db_column='supplierID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Supplier')),
            ],
            options={
                'managed': True,
                'db_table': 'suppliermaterial',
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=45)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(default='male', max_length=45)),
                ('dateofentry', models.DateTimeField(auto_now_add=True, db_column='dateOfEntry')),
                ('phonenumber', models.CharField(db_column='phoneNumber', max_length=45, null=True)),
                ('address', models.CharField(max_length=45, null=True)),
                ('position', models.ForeignKey(db_column='position', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Role')),
            ],
            options={
                'managed': True,
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True, unique=True)),
                ('product', models.ForeignKey(db_column='productID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Product')),
            ],
            options={
                'managed': True,
                'db_table': 'workshop',
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(db_column='supplier', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='class_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.ProductClass'),
        ),
        migrations.AddField(
            model_name='producetaskbasic',
            name='workshop',
            field=models.ForeignKey(blank=True, db_column='workshopID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Workshop'),
        ),
        migrations.AddField(
            model_name='outproduct',
            name='outwarehouse',
            field=models.ForeignKey(db_column='outwarehouseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.OutWarehouse'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(db_column='productID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Product'),
        ),
        migrations.AddField(
            model_name='materialrequistion',
            name='workshop',
            field=models.ForeignKey(blank=True, db_column='workshopID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Workshop'),
        ),
        migrations.AddField(
            model_name='material',
            name='class_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.MaterialClass'),
        ),
        migrations.AddField(
            model_name='inwarehouseproduct',
            name='material',
            field=models.ForeignKey(db_column='materialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material'),
        ),
        migrations.AddField(
            model_name='inventorinformation',
            name='material',
            field=models.OneToOneField(db_column='materialID', on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Material'),
        ),
        migrations.AlterUniqueTogether(
            name='suppliermaterial',
            unique_together=set([('supplier', 'material')]),
        ),
        migrations.AlterUniqueTogether(
            name='requisitionmaterial',
            unique_together=set([('requisition', 'material')]),
        ),
        migrations.AlterUniqueTogether(
            name='purchaseproduct',
            unique_together=set([('purchase', 'material')]),
        ),
        migrations.AlterUniqueTogether(
            name='productmaterial',
            unique_together=set([('product', 'material')]),
        ),
        migrations.AlterUniqueTogether(
            name='outproduct',
            unique_together=set([('outwarehouse', 'material')]),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together=set([('order', 'product')]),
        ),
    ]