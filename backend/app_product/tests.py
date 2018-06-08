from django.test import TestCase
# from .Views import ProduceTask
# from ..enterprise.models import *
from enterprise.models import *
from app_product.Views import ProduceTask
from app_product.Views import MaterialList


class ProduceTaskModelTestCase(TestCase):
    def setUp(self):
        self.p1 = Product()
        self.p1.save()
        self.p2 = Product()
        self.p2.save()
        self.w1 = Workshop(product_id=self.p1.id, name="w1")
        self.w1.save()
        self.w2 = Workshop(product_id=self.p1.id, name="w2")
        self.w2.save()
        self.w3 = Workshop(product_id=self.p2.id, name="w3")
        self.w3.save()
        self.o1 = Order(status=0)
        self.o1.save()
        self.o2 = Order(status=0)
        self.o2.save()
        self.o3 = Order(status=1)
        self.o3.save()
        self.o4 = Order(status=2)
        self.o4.save()
        op1 = OrderProduct(order_id=self.o1.id, product_id=self.p1.id)
        op1.save()
        op2 = OrderProduct(order_id=self.o2.id, product_id=self.p2.id)
        op2.save()
        op3 = OrderProduct(order_id=self.o3.id, product_id=self.p1.id)
        op3.save()
        op4 = OrderProduct(order_id=self.o4.id, product_id=self.p1.id)
        op4.save()
        ptb = ProduceTaskBasic(order_id=self.o3.id, workshop_id=self.w1.id, number=1)
        ptb.save()
        ptb = ProduceTaskBasic(order_id=self.o3.id, workshop_id=self.w1.id, number=2)
        ptb.save()
        ptb = ProduceTaskBasic(order_id=self.o3.id, workshop_id=self.w1.id, number=3)
        ptb.save()
        ptb = ProduceTaskBasic(order_id=self.o4.id, workshop_id=self.w1.id, number=1)
        ptb.save()

    def test_getUnallocatedOrders(self):
        its_orders = ProduceTask.getUnallocatedOrders()
        my_orders = Order.objects.filter(status=0).count()

        self.assertEqual(len(its_orders), my_orders)

    def test_getAllocatedOrders(self):
        its_orders = ProduceTask.getAllocatedOrders()
        my_orders = Order.objects.filter(status__gte=1)

        self.assertEqual(len(its_orders), len(my_orders))


    def test_createProduceTasks(self):
        old_amount = ProduceTaskBasic.objects.count()
        tl = [{
            "workshop_id": self.w1.id,
            "amount": 100,
            "topic": "topic",
            "person_in_charge": "CQX1"
        },
        {
            "workshop_id": self.w2.id,
            "amount": 120,
            "topic": "topic",
            "person_in_charge": "CQX2"
        }]
        tasks = ProduceTask.createTasks(tl, self.o1.id)
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(old_amount+2, new_amount)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(type(tasks), type([]))
        self.assertEqual(type(tasks[0]), type({}))
        old_amount = new_amount
        tl = {
            "workshop_id": self.w1.id,
            "amount": 100,
            "topic": "topic",
            "person_in_charge": "CQX1"
        }
        tasks = ProduceTask.createTasks(tl, self.o1.id)
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(old_amount+1, new_amount)
        self.assertEqual(type(tasks), type({}))

    def test_get_workshops(self):
        workshops = ProduceTask.getWorkshops()
        self.assertEqual(type(workshops), type({}))
        self.assertEqual(type(workshops[self.p1.id]), type({}))
        self.assertEqual(len(workshops[self.p1.id]), 2)
        self.assertEqual(workshops[self.p2.id][self.w3.name], self.w3.id)

        workshops = ProduceTask.getWorkshops(self.p1.id)
        self.assertEqual(type(workshops), type({}))
        self.assertEqual(type(workshops[self.w1.name]), str(self.w1.id))
        self.assertEqual(len(workshops), 2)

        workshops = ProduceTask.getWorkshops(-1, True)
        self.assertEqual(type(workshops), type([]]))
        self.assertEqual(len(workshops), 3)


    def test_update_task(self):
        t = ProduceTaskBasic(personincharge="A", workshop=self.w1, number=200, topic="topic", order_id=self.o3.id)
        t.save()
        new_info = {
            "person_in_charge": "B",
            "workshop_id": self.w2.id,
            "amount": 100,
            "topic": "topic2",
            "status": 2,
        }
        task = ProduceTask.updateTask(t.id, new_info)

        self.assertEqual(type(task), type({}))
        self.assertEqual(task.get("amount"), 100)
        self.assertEqual(task.get("id"), t.id)
        self.assertEqual(task.get("topic"), "topic2")
        self.assertEqual(task.get("status"), "undone")
        self.assertEqual(task.get("person_in_charge"), "B")

    def test_delete_task(self):
        t = ProduceTaskBasic()
        t.save()
        old_amount = ProduceTaskBasic.objects.count()
        amount = ProduceTask.deleteTask(t.id)
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(1, amount)
        self.assertEqual(old_amount-1, new_amount)

    def test_query_task(self):
        my_amount = ProduceTaskBasic.objects.count()
        it_amount = len(ProduceTask.queryTasks())
        self.assertEqual(my_amount, it_amount)

        my_amount = ProduceTaskBasic.objects.count({"number": 2})
        it_amount = len(ProduceTask.queryTasks({"number": 2}))
        self.assertEqual(my_amount, it_amount)

        my_amount = ProduceTaskBasic.objects.count({"order_id": self.o3.id})
        it_amount = len(ProduceTask.queryTasks({"order_id": self.o3.id}))
        self.assertEqual(3, it_amount)




class MaterialListModelTestCase(TestCase):
    def setUp(self):
        self.p1 = Product()
        self.p1.save()
        self.p2 = Product()
        self.p2.save()
        self.m1 = Material(name='material001')
        self.m1.save()
        self.m2 = Material(name='material002')
        self.m2.save()
        self.m3 = Material(name='material003')
        self.m3.save()
        self.m4 = Material(name='material004')
        self.m4.save()
        self.m5 = Material(name='material005')
        self.m5.save()

        self.r1 = ProductMaterial(product=self.p1, material=self.m1, number=10)
        self.r1.save()
        self.r2 = ProductMaterial(product=self.p1, material=self.m3, number=30)
        self.r2.save()
        self.r3 = ProductMaterial(product=self.p1, material=self.m5, number=50)
        self.r3.save()
        self.r4 = ProductMaterial(product=self.p2, material=self.m2, number=20)
        self.r4.save()
        self.r5 = ProductMaterial(product=self.p2, material=self.m4, number=40)
        self.r5.save()

    def test_getMaterialList(self):
        my_list = MaterialList.getMaterialList(self.p1.id, 2)
        its_list = ProductMaterial.objects.filter(product=self.p1.id)

        array = my_list["material_requisition"]
        my_type = type(array[0])
        my_number = 0
        for a in array:
            if a["material_id"]==self.m3.id:
                my_number = a["material_num"]

        self.assertEqual(len(array), len(its_list))
        self.assertEqual(my_type, type({}))
        self.assertEqual(my_number, 60)