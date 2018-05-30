from .models import *
from datetime import date

def generateMaterialClass():
    bmr = MaterialClass(class_field="Base Material Class")
    bmr.save()
    for i in range(10):
        id = bmr.id if i<4 else i-1
        mr = MaterialClass(parent_class_id=id)
        mr.save()

def generateMaterial():
    name = "Material {}"
    MC = MaterialClass.objects.first()
    for i in range(50):
        m = Material(name=name.format(i), class_obj_id= MC.id)
        m.save()

def generateOrder():
    indentor = "indentor {}"
    receiver = "reveiver {}"
    checker = "checker {}"
    for i in range(13):
        o = Order(indentor=indentor.format(i), receiver=receiver.format(i), checker=checker.format(i), status=i%4)
        o.save()

def generateProductClass():
    bpc = ProductClass(class_field="BaseClass")
    bpc.save()
    pc_name = "ProductClass {}"
    for i in range(10):
        id = bpc.id if i<3 else i - 1
        pc = ProductClass(class_field=pc_name.format(i), parent_class_id=id)
        pc.save()

def generateProduct():
    name = "Product {}"
    pc = ProductClass.objects.first()
    for i in range(23):
        p = Product(name=name.format(i), class_obj=pc, price=10*i)
        p.save()

def generateWorkshop():
    products = Product.objects.all()
    name = "Workshop {}"
    for i in range(10):
        w = Workshop(name=name.format(i), product=products[i%3])
        w.save()


def generateProductTaskBasic():
    charger = "charger {}"
    topic = "topic {}"

    for i in range(30):
        ptb = ProduceTaskBasic()
        ptb.personincharge = charger.format(i)
        ptb.topic = topic.format(i)
        ptb.producestatus = i%2
        ptb.workshop = Workshop.objects.get(id=1+i%4)
        ptb.order = Order.objects.get(id=1+i%4)
        ptb.number = i*7
        ptb.deadline = date(2018, 5+i%6, 1+i%15)
        ptb.save()

def generateOutWarehouse():
    receiver = "receiver {}"
    checker = "checker {}"
    for i in range(10):
        o = OutWarehouse(receiver=receiver.format(i), checker=checker.format(i))
        o.save()


def generateSupplier():
    name = "name {}"
    contact = "1352691183{}"
    phonenumber= "1352691183{}"
    address = "Nankai Uni. TianJin Province"
    for i in range(10):
        s = Supplier(name=name.format(i), contact=contact.format(i), phonenumber=phonenumber.format(i), address=address)
        s.save()


def generateInventorInformation():
    ms = Material.objects.all()
    shelf = "AE{}3{}"
    for i in range(12):
        ii = InventorInformation()
        ii.material = ms[i]
        ii.shelfnumber = shelf.format(i, i*10)
        ii.number = i*10
        ii.threshold = i*2
        ii.save()


def generateInWarehouse():
    checker = "checker {}"
    operator = "operator {}"
    for i in range(5):
        iw = InWarehouse(checker=checker.format(i), operator=operator.format(i))
        iw.save()


def generateRole():
    permission = "permission {}"
    position = "positoin {}"
    for i in range(10):
        r = Role()
        r.position = (i+1)%3
        r.permission = permission.format((i+1)%3)
        r.positionname = position.format((i+1)%3)
        r.save()


def generateInWarehouseProduct():
    iwhs = InWarehouse.objects.all()
    ms = Material.objects.all()
    for i in range(10):
        iwp = InwareHouseProduct()
        iwp.inwarehouse = iwhs[i%5]
        iwp.material = ms[i]
        iwp.number = i*10
        iwp.save()


def generateMaterialRequisition():
    requistioner = "requistioner {}"
    checker = "checker {}"
    workshops = Workshop.objects.all()
    for i in range(10):
        mr = MaterialRequistion()
        mr.status = i%2
        mr.workshop = workshops[i%3]
        mr.requistioner = requistioner.format(i)
        mr.checker = checker.format(i)
        mr.save()


def generateOrderProduct():
    orders = Order.objects.all()
    products = Product.objects.all()
    for i in range(100):
        op = OrderProduct()
        op.order = orders[int(i/10)]
        op.product = products[i%10]
        op.number = i*3
        op.price = i*0.9
        op.save()

def generateOutProduct():
    outwarehouse = OutWarehouse.objects.all()
    materials = Material.objects.all()
    for i in range(20):
        op = OutProduct()
        op.outwarehouse = outwarehouse[int(i/5)]
        op.material = materials[i]
        op.save()


def generateProductMaterial():
    products = Product.objects.all()
    materials = Material.objects.all()
    for i in range(200):
        pm = ProductMaterial()
        pm.product = products[int(i/10)]
        pm.material = materials[i%30]
        pm.procedure = i%3
        pm.number = i
        pm.save()


def generatePurchase():
    suppliers = Supplier.objects.all()
    purchaser = "purchaser {}"
    checker = "checker {}"
    for i in range(7):
        p = Purchase()
        p.supplier = suppliers[i%3]
        p.purchaser = purchaser.format(i)
        p.checker = checker.format(i)
        p.totalprice = i*100
        p.save()


def generatePurchaseProduct():
    purchases = Purchase.objects.all()
    materials = Material.objects.all()
    for i in range(20):
        pp = PurchaseProduct()
        pp.purchase = purchases[int(i/4)]
        pp.material = materials[i%7]
        pp.number = i*3
        pp.price = i*19
        pp.save()

def generateUserTable():
    positions = Role.objects.all()
    name = "username {}"
    pw = "password"
    for i in range(10):
        user = UserTable()
        user.name = name.format(i)
        user.password = pw
        user.position = positions[i%3]
        user.gender = "male" if i %2 ==0 else "female"
        user.save()