from django.test import TestCase
from .models import *
from datetime import time
# Create your tests here.

class MaterialClassTestCase(TestCase):
    def setUp(self):
        self.MC = MaterialClass(class_field="Base Class")
        self.MC.save()
        #self.MC = MaterialClass()

    def test_create_MC(self):
        MC = MaterialClass()
        old_amount = MaterialClass.objects.count()
        MC.class_field = "Material Class A"
        MC.parent_class_id = self.MC.id
        MC.save()
        new_amount = MaterialClass.objects.count()
        self.assertNotEqual(old_amount, new_amount)

    def test_duplicate_MC(self):
        old_amount = MaterialClass.objects.count()
        first = MaterialClass()
        first.class_field = "A"
        first.parent_class_id = self.MC.id
        first.save()
        second = MaterialClass(class_field="B", parent_class_id=self.MC.id)
        second.save()
        self.assertEqual(MaterialClass.objects.count(), old_amount + 2)


class MaterialTestCase(TestCase):
    def setUp(self):
        self.MC = MaterialClass()
        self.MC.save()
        self.M = Material(name="Material 1", class_obj_id=self.MC.id)
        self.M.save()

    def test_create_M(self):
        self.assertEqual(1, Material.objects.count())
        m = Material.objects.first()
        self.assertEqual(self.MC.id, m.class_obj.id)

    def test_duplicate_M(self):
        m2 = Material(class_obj_id=self.MC.id)
        m2.save()
        self.assertEqual(2, Material.objects.count())


class OrderTestCase(TestCase):
    def test_create_order(self):
        o = Order(indentor="CQX", receiver="ZXX", checker="SXY")
        o.save()
        self.assertEqual(1, Order.objects.count())
        temp = Order.objects.get()
        self.assertEqual(0, temp.status)

    def test_duplicate_order(self):
        old_amount = Order.objects.count()
        o1 = Order(indentor="CQX", receiver="ZXX", checker="SXY")
        o1.save()
        o2 = Order(indentor="CQX", receiver="ZXX", checker="SXY")
        o2.save()
        new_amount = Order.objects.count()
        self.assertEqual(old_amount+2,new_amount)


class ProductClassTestCase(TestCase):
    def setUp(self):
        self.base = ProductClass(class_field="Base Class")
        self.base.save()

    def test_create_pc(self):
        pc = ProductClass(class_field="test1", parent_class=self.base)
        pc.save()

        pc = ProductClass(class_field="sad", parent_class_id=self.base.id)
        pc.save()


class ProductTestCase(TestCase):
    def setUp(self):
        self.pc = ProductClass()
        self.pc.save()

    def test_create_p(self):
        old_amount = Product.objects.count()
        p1 = Product(name="name", price=12.1, class_obj_id=self.pc.id)
        p1.save()

        p2 = Product(name="name", price=12.1, class_obj=self.pc)
        p2.save()
        new_amount = Product.objects.count()
        self.assertEqual(old_amount+2, new_amount)

    def test_duplicate_p(self):
        old_amount = Product.objects.count()
        p1 = Product(name="name", price=12.1, class_obj=self.pc)
        p1.save()
        p2 = Product(name="name", price=12.1, class_obj=self.pc)
        p2.save()
        p3 = Product(name="name", price=12.1, class_obj=self.pc)
        p3.save()
        new_amount = Product.objects.count()
        self.assertEqual(old_amount + 3, new_amount)


class WorkshopTestCase(TestCase):
    def setUp(self):
        self.pc = ProductClass()
        self.pc.save()
        self.p = Product(class_obj=self.pc)
        self.p.save()

    def test_create_workshop(self):
        old_amount = Workshop.objects.count()
        w = Workshop(name="Asd", product=self.p)
        w.save()
        w = Workshop(name="Asd", product_id=self.p.id)
        w.save()
        new_amount = Workshop.objects.count()
        self.assertEqual(old_amount+2, new_amount)

class ProduceTaskBasicTestCase(TestCase):
    def setUp(self):
        self.pc = ProductClass()
        self.pc.save()
        self.p = Product(class_obj=self.pc)
        self.p.save()
        self.w = Workshop(name="Asd", product=self.p)
        self.w.save()
        self.o = Order()
        self.o.save()

    def test_create_producetaskbasic(self):
        old_amount = ProduceTaskBasic.objects.count()
        ptb = ProduceTaskBasic(personincharge="CQX", workshop = self.w, order=self.o)
        ptb.save()
        ptb = ProduceTaskBasic(personincharge="CQX", workshop_id=self.w.id, order_id=self.o.id)
        ptb.save()
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(old_amount+2, new_amount)

class OutWarehouseTestCase(TestCase):
    def test_create_ow(self):
        old_amount = OutWarehouse.objects.count()
        ow = OutWarehouse(receiver="CQX", checker="ASLDJ")
        ow.save()
        new_amount = OutWarehouse.objects.count()
        self.assertEqual(old_amount+1, new_amount)


class SupplierTestCase(TestCase):
    def test_create_supplier(self):
        old_amount = Supplier.objects.count()
        s = Supplier(name="ASD", contact="adsc", phonenumber="21eed2", address="asdc")
        s.save()
        new_amount = Supplier.objects.count()
        self.assertEqual(old_amount+1, new_amount)


class InventorTestCase(TestCase):
    def setUp(self):
        self.m = Material()
        self.m.save()

    def test_create_inventor(self):
        old_amount = InventorInformation.objects.count()
        i = InventorInformation(material=self.m, shelfnumber="A3057", number=100, threshold=10)
        i.save()
        new_amount = InventorInformation.objects.count()
        self.assertEqual(old_amount+1, new_amount)


class InwarehouseTestCase(TestCase):
    def test_create_inwarehouse(self):
        i = InWarehouse(checker="qwd", operator="cdsz")
        i.save()


class InWarehouseProductTestCase(TestCase):
    def setUp(self):
        self.inwarehouse = InWarehouse()
        self.inwarehouse.save()
        self.material = Material()
        self.material.save()

    def test_create_iwhp(self):
        old_amount = InwareHouseProduct.objects.count()
        iwhp = InwareHouseProduct(inwarehouse=self.inwarehouse, material=self.material, number=500)
        iwhp.save()
        new_amount = InwareHouseProduct.objects.count()
        self.assertEqual(old_amount+1, new_amount)


class MaterialRequistionTestCase(TestCase):
    def setUp(self):
        self.w = Workshop()
        self.w.save()

    def test_create_MR(self):
        old_amount = MaterialRequistion.objects.count()
        mr = MaterialRequistion(workshop=self.w, requistioner="wa", checker="Asdcsa", status=1)
        mr.save()
        mr = MaterialRequistion(workshop_id=self.w.id, requistioner="test", checker="Asdcsa", status=1)
        mr.save()
        new_amount = MaterialRequistion.objects.count()
        self.assertEqual(old_amount+2, new_amount)
        self.assertEqual(MaterialRequistion.objects.get(requistioner="test").workshop_id, self.w.id)


class OrderProductTestCase(TestCase):
    def setUp(self):
        self.o = Order()
        self.o.save()
        self.p1 = Product()
        self.p1.save()
        self.p2 = Product()
        self.p2.save()

    def test_create_op(self):
        old_amount = OrderProduct.objects.count()
        op = OrderProduct(order=self.o, product=self.p1, number=100, price=123.53)
        op.save()
        op = OrderProduct(order_id=self.o.id, product_id=self.p2.id, number=99, price=91)
        op.save()
        new_amount = OrderProduct.objects.count()
        self.assertEqual(old_amount+2, new_amount)
        self.assertEqual(OrderProduct.objects.get(price=91).order.id, self.o.id)

class OutProductTestCase(TestCase):

    def setUp(self):
        self.ow = OutWarehouse()
        self.m = Material()
        self.m2 = Material()
        self.ow.save()
        self.m.save()
        self.m2.save()

    def test_create_OutProduct(self):
        old_amount = OutProduct.objects.count()
        op = OutProduct(outwarehouse = self.ow, material=self.m, number=100)
        op.save()
        op = OutProduct(outwarehouse_id=self.ow.id, material_id=self.m2.id, number=100)
        op.save()
        new_amount = OutProduct.objects.count()
        self.assertEqual(old_amount+2, new_amount)


class ProductMaterialTestCase(TestCase):
    def setUp(self):
        self.p = Product()
        self.p.save()
        self.m = Material()
        self.m.save()
        self.m2 = Material()
        self.m2.save()

    def test_create_pm(self):
        old_amount = ProductMaterial.objects.count()
        pm = ProductMaterial(product=self.p, material=self.m, procedure=1, number=12, comments="adsc")
        pm.save()
        pm = ProductMaterial(product_id=self.p.id, material_id=self.m2.id, procedure=1, number=12, comments="adsc")
        pm.save()
        new_amount = ProductMaterial.objects.count()
        self.assertEqual(old_amount+2, new_amount)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.s = Supplier()
        self.s.save()

    def test_create_purchase(self):
        old_amount = Purchase.objects.count()
        p = Purchase(supplier=self.s, checker="Ads", purchaser="asd", totalprice=123)
        p.save()
        p = Purchase(supplier_id=self.s.id, checker="Ads", purchaser="asd", totalprice=123)
        p.save()
        new_amount = Purchase.objects.count()
        self.assertEqual(old_amount + 2, new_amount)


class PurchaseProductTestCase(TestCase):
    def setUp(self):
        self.m = Material()
        self.m2 = Material()
        self.p = Purchase()
        self.m.save()
        self.m2.save()
        self.p.save()

    def test_create_purchaseproduct(self):
        old_amount = PurchaseProduct.objects.count()
        pp = PurchaseProduct(material=self.m, purchase=self.p, number=10, price=12)
        pp.save()
        pp = PurchaseProduct(material_id=self.m2.id, purchase_id=self.p.id, number=10, price=12)
        pp.save()
        new_amount = PurchaseProduct.objects.count()
        self.assertEqual(old_amount+2, new_amount)


class UserTableTestCase(TestCase):
    def setUp(self):
        self.r = Role(position=1)
        self.r.save()

    def test_create_usertable(self):
        old_amount = UserTable.objects.count()
        ut = UserTable(name="admin", password="pw", gender="male", position=self.r)
        ut.save()
        ut = UserTable(name="admin", password="pw", gender="male", position_id=self.r.id, phonenumber="2er2112er", address="sacdafr")
        ut.save()
        new_amount = UserTable.objects.count()
        self.assertEqual(old_amount+2, new_amount)

