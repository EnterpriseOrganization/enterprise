from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import *

class MaterialClass(models.Model):
    # id = models.AutoField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=45, default='the very based class')
    parent_class = models.ForeignKey('MaterialClass', models.DO_NOTHING, null=True)  #  on_delete暂时为DO_NOTHING 之后要级联删除； 字段暂时可以为空 之后设为基类ID
    class Meta:
        managed = True
        db_table = 'materialclass'


class Material(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    # class_field = models.CharField(db_column='class', max_length=45, default='the very based class')  # Field renamed because it was a Python reserved word.
    # class_id = models.OneToOneField(MaterialClass, models.DO_NOTHING, null=True)  # 暂时可以为空 之后设为基类ID
    class_obj = models.ForeignKey(MaterialClass, models.DO_NOTHING, null=True)
    class Meta:
        managed = True
        db_table = 'material'


class Order(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    indentor = models.CharField(max_length=45, null=True)
    receiver = models.CharField(max_length=45, null=True)
    checker = models.CharField(max_length=45, null=True)
    recevieraddress = models.CharField(db_column='recevierAddress', max_length=200, null=True)  # Field name made lowercase.
    indentorphonenumber = models.CharField(db_column='indentorPhoneNumber', max_length=45, null=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=3, decimal_places=0, null=True)  # Field name made lowercase.
    status = models.IntegerField(default=0)  # 0: 待生产 1: 生产中 2:配送中（生产完成） 3: 采购中
    deliverydate = models.DateTimeField(db_column='deliveryDate', auto_now_add=True)  # Field name made lowercase.
    paymentway = models.CharField(db_column='paymentWay', max_length=45, default='default paymentway')  # say 顺丰

    class Meta:
        managed = True
        db_table = 'order'

@receiver(pre_save, sender=Order)
def fillDeliveryDate(sender, instance, **kwargs):
    if instance.status == 2:
        instance.deliverydate = datetime.now().strftime("%Y-%m-%d %H:%I:%S")

class ProductClass(models.Model):
    # id = models.AutoField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=45, default='the very based class')
    parent_class = models.ForeignKey('ProductClass', models.DO_NOTHING, null=True) # on_delete之后要级联找到所有子类 删除之

    class Meta:
        managed = True
        db_table = 'productclass'

class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    # class_field =   # Field renamed because it was a Python reserved word.
    # class_id = models.OneToOneField(ProductClass, models.DO_NOTHING, null=True)
    class_obj = models.ForeignKey(ProductClass, models.DO_NOTHING, null=True)
    price = models.DecimalField(max_digits=3, decimal_places=0, blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'product'

class Workshop(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True, unique=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID', null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'workshop'

def TaskStatusValidator(value):
    if value < 0 or value > 2:
        raise ValidationError("status value out of range [0~2]", params={'value', value})


class ProduceTaskBasic(models.Model):
    # id = models.AutoField(primary_key=True)
    personincharge = models.CharField(db_column='personInCharge', max_length=45, blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(default=0, validators=[TaskStatusValidator]) # 0：已分配,待领料 1： 已领料,待生产 2: 生产完成
    # producestatus = models.IntegerField(db_column='produceStatus', blank=True, null=True, default=0)  # Field name made lowercase.
    archivedate = models.DateTimeField(db_column='accurateDate', blank=True, null=True)  # Field name made lowercase.
    workshop = models.ForeignKey(Workshop, models.DO_NOTHING, db_column='workshopID', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderID', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)
    begindate = models.DateTimeField(db_column='beginDate',auto_now_add=True)  # Field name made lowercase.
    done_checker = models.CharField(null=True, max_length=100, default="")
    # deadline = models.DateTimeField(null=True)
    deadline = models.DateField(null=True)
    material_getter = models.CharField(max_length=100, default="")
    material_checker = models.CharField(max_length=100, default="")
    material_distributon_date = models.DateTimeField(null=True)
    class Meta:
        managed = True
        db_table = 'producetaskbasic'


@receiver(pre_save, sender=ProduceTaskBasic)
def fillDoneDate(sender, instance, **kwargs):
    if instance.status == 1: # 添加领料时间
        instance.material_distributon_date = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    elif instance.status == 2:
        instance.archivedate = datetime.now().strftime("%Y-%m-%d %H:%I:%S") # 自动添加完成时间
        order = instance.order # 注册进度到订单里
        order.status = 2
        order.save()


class OutWarehouse(models.Model):
    # id = models.AutoField(primary_key=True)
    outdate = models.DateTimeField(db_column='outDate', auto_now_add=True)  # Field name made lowercase.
    receiver = models.CharField(max_length=45, null=True)
    checker = models.CharField(max_length=45, null=True)

    class Meta:
        managed = True
        db_table = 'outwarehouse'


class Supplier(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    contact = models.CharField(max_length=45, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = 'supplier'


class InventorInformation(models.Model):
    # id = models.AutoField(primary_key=True)
    material = models.OneToOneField(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    shelfnumber = models.CharField(db_column='shelfNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    newestinwarehousedate = models.DateTimeField(db_column='newestInWarehouseDate', blank=True, auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'inventorinformation'


class InWarehouse(models.Model):
    # id = models.AutoField(primary_key=True)
    indate = models.DateTimeField(db_column='inDate', auto_now_add=True)  # Field name made lowercase.
    checker = models.CharField(max_length=45, null=True)
    operator = models.CharField(max_length=45, null=True)

    class Meta:
        managed = True
        db_table = 'inwarehouse'


class Role(models.Model):
    position = models.IntegerField(default=0)
    permission = models.CharField(max_length=32, null=True)
    positionname = models.CharField(db_column='positionName', max_length=45, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'role'


class InwareHouseProduct(models.Model):
    # id = models.AutoField(primary_key=True) # django是否会自动生成 with managed=True？
    inwarehouse = models.ForeignKey(InWarehouse, models.DO_NOTHING, db_column='inwarehouseID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'inwarehouseproduct'


class MaterialRequistion(models.Model):
    # id = models.AutoField(primary_key=Tdjango select_related 多个字段rue)
    distributiondate = models.DateTimeField(db_column='distributionDate', blank=True, auto_now_add=True)  # Field name made lowercase.
    requistioner = models.CharField(max_length=45, blank=True, null=True)
    checker = models.CharField(max_length=45, blank=True, null=True)
    workshop = models.ForeignKey(Workshop, models.DO_NOTHING, db_column='workshopID', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, default=0, null=True) # 0：未领(申请中) 1：已领

    class Meta:
        managed = True
        db_table = 'materialrequistion'


class OrderProduct(models.Model):
    # id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderID', null=True)  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID', null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=3) # 单价  能否自动生成
    class Meta:
        managed = True
        db_table = 'orderproduct'
        unique_together = (('order', 'product'),)


class OutProduct(models.Model):
    # id = models.AutoField(primary_key=True)
    outwarehouse = models.ForeignKey(OutWarehouse, models.DO_NOTHING, db_column='outwarehouseID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'outproduct'
        unique_together = (('outwarehouse', 'material'),)


class ProductMaterial(models.Model):
    # id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    procedure = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'productmaterial'
        unique_together = (('product', 'material'),)


class Purchase(models.Model):
    # id = models.AutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    purchaser = models.CharField(max_length=45, null=True)
    date = models.DateTimeField(auto_now_add=True)
    checker = models.CharField(max_length=45, null=True)
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=3, decimal_places=0, default=0)  # Field name made lowercase.
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='supplier', null=True)

    class Meta:
        managed = True
        db_table = 'purchase'


class PurchaseProduct(models.Model):
    # id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, models.DO_NOTHING, db_column='purchaseID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    class Meta:
        managed = True
        db_table = 'purchaseproduct'
        unique_together = (('purchase', 'material'),)


class RequisitionMaterial(models.Model):
    # id = models.AutoField(primary_key=True)
    requisition = models.ForeignKey(MaterialRequistion, models.DO_NOTHING, db_column='requisitionID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'requisitionmaterial'
        unique_together = (('requisition', 'material'),)


class SupplierMaterial(models.Model):
    # id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='supplierID', null=True)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID', null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suppliermaterial'
        unique_together = (('supplier', 'material'),)


class UserTable(models.Model):
    # id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, default='male')
    dateofentry = models.DateTimeField(db_column='dateOfEntry', auto_now_add=True)  # Field name made lowercase.
    position = models.ForeignKey(Role, models.DO_NOTHING, db_column='position', null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=45, null=True)

    class Meta:
        managed = True
        db_table = 'user_table'



''' 暂时保留, 姑且认为物料申请表和领料表是一回事
反正别的组也不用
class Apply(models.Model):
    id = models.IntegerField(primary_key=True)
    workshopid = models.OneToOneField(Workshop, models.DO_NOTHING, db_column='workshopID')  # Field name made lowercase.
    applier = models.CharField(max_length=45)
    date = models.DateTimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'apply'


class Applymaterial(models.Model):
    applyid = models.OneToOneField(Apply, models.DO_NOTHING, db_column='applyID', primary_key=True)  # Field name made lowercase.
    materialid = models.OneToOneField(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'applymaterial'
        unique_together = (('applyid', 'materialid'),)

'''