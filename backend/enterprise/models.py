from django.db import models


class Apply(models.Model):
    id = models.IntegerField(primary_key=True)
    workshopid = models.ForeignKey('Workshop', models.DO_NOTHING, db_column='workshopID')  # Field name made lowercase.
    applier = models.CharField(max_length=45)
    date = models.DateTimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'apply'


class Applymaterial(models.Model):
    applyid = models.ForeignKey(Apply, models.DO_NOTHING, db_column='applyID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey('Material', models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'applymaterial'
        unique_together = (('applyid', 'materialid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inventorinformation(models.Model):
    materialid = models.ForeignKey('Material', models.DO_NOTHING, db_column='materialID', primary_key=True)  # Field name made lowercase.
    shelfnumber = models.CharField(db_column='shelfNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    newestinwarehousedate = models.DateTimeField(db_column='newestInWarehouseDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventorinformation'


class Inwarehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    indate = models.DateTimeField(db_column='inDate')  # Field name made lowercase.
    checker = models.CharField(max_length=45)
    operator = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'inwarehouse'


class Inwarehouseproduct(models.Model):
    inwarehouseid = models.ForeignKey(Inwarehouse, models.DO_NOTHING, db_column='inwarehouseID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey('Material', models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inwarehouseproduct'


class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    class_field = models.CharField(db_column='class', max_length=45)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'material'


class Materialrequistion(models.Model):
    id = models.IntegerField(primary_key=True)
    distributiondate = models.DateTimeField(db_column='distributionDate', blank=True, null=True)  # Field name made lowercase.
    requistioner = models.CharField(max_length=45, blank=True, null=True)
    checker = models.CharField(max_length=45, blank=True, null=True)
    workshopid = models.ForeignKey('Workshop', models.DO_NOTHING, db_column='workshopID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materialrequistion'


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    indentor = models.CharField(max_length=45)
    recevier = models.CharField(max_length=45)
    checker = models.CharField(max_length=45)
    recevieraddress = models.CharField(db_column='recevierAddress', max_length=200)  # Field name made lowercase.
    indentorphonenumber = models.CharField(db_column='indentorPhoneNumber', max_length=45)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=3, decimal_places=0)  # Field name made lowercase.
    status = models.CharField(max_length=45)
    deliverydate = models.DateTimeField(db_column='deliveryDate')  # Field name made lowercase.
    paymentway = models.CharField(db_column='paymentWay', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderproduct(models.Model):
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    number = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderproduct'
        unique_together = (('orderid', 'productid'),)


class Outproduct(models.Model):
    outwarehouseid = models.ForeignKey('Outwarehouse', models.DO_NOTHING, db_column='outwarehouseID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'outproduct'
        unique_together = (('outwarehouseid', 'materialid'),)


class Outwarehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    outdate = models.DateTimeField(db_column='outDate')  # Field name made lowercase.
    receiver = models.CharField(max_length=45)
    checker = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'outwarehouse'


class Producetask(models.Model):
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderID', primary_key=True)  # Field name made lowercase.
    produceid = models.ForeignKey('Producetaskbasic', models.DO_NOTHING, db_column='produceID')  # Field name made lowercase.
    number = models.IntegerField()
    begindate = models.DateTimeField(db_column='beginDate')  # Field name made lowercase.
    deadline = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'producetask'
        unique_together = (('orderid', 'produceid'),)


class Producetaskbasic(models.Model):
    id = models.IntegerField(primary_key=True)
    personincharge = models.CharField(db_column='personInCharge', max_length=45, blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(max_length=45, blank=True, null=True)
    producestatus = models.CharField(db_column='produceStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accuratedate = models.DateTimeField(db_column='accurateDate', blank=True, null=True)  # Field name made lowercase.
    workshopid = models.ForeignKey('Workshop', models.DO_NOTHING, db_column='workshopID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producetaskbasic'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    class_field = models.CharField(db_column='class', max_length=45)  # Field renamed because it was a Python reserved word.
    price = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Productmaterial(models.Model):
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    procedure = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productmaterial'
        unique_together = (('productid', 'materialid'),)


class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    purchaser = models.CharField(max_length=45)
    date = models.DateTimeField()
    checker = models.CharField(max_length=45)
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=3, decimal_places=0)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplier')

    class Meta:
        managed = False
        db_table = 'purchase'


class Purchaseproduct(models.Model):
    purchaseid = models.ForeignKey(Purchase, models.DO_NOTHING, db_column='purchaseID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'purchaseproduct'


class Requisitionmaterial(models.Model):
    requisitionid = models.ForeignKey(Materialrequistion, models.DO_NOTHING, db_column='requisitionID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requisitionmaterial'
        unique_together = (('requisitionid', 'materialid'),)


class Role(models.Model):
    position = models.IntegerField(primary_key=True)
    permission = models.CharField(max_length=32)
    positionname = models.CharField(db_column='positionName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45)  # Field name made lowercase.
    address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'supplier'


class Suppliermaterial(models.Model):
    supplierid = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='supplierID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    price = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliermaterial'
        unique_together = (('supplierid', 'materialid'),)


class UserTable(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45)
    dateofentry = models.DateTimeField(db_column='dateOfEntry')  # Field name made lowercase.
    position = models.ForeignKey(Role, models.DO_NOTHING, db_column='position')
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45)  # Field name made lowercase.
    address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_table'


class Workshop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'workshop'
