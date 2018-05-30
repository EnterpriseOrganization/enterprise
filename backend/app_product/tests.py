from django.test import TestCase
# from .Views import ProduceTask
# from ..enterprise.models import *
from enterprise.models import *
from app_product.Views import ProduceTask


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
        ptb = ProduceTaskBasic(order_id=self.o3.id, workshop_id=self.w1.id, number=1)
        ptb.save()
        ptb = ProduceTaskBasic(order_id=self.o3.id, workshop_id=self.w1.id, number=1)
        ptb.save()
        ptb = ProduceTaskBasic(order_id=self.o4.id, workshop_id=self.w1.id, number=1)
        ptb.save()

    def test_getUnallocatedOrders(self):
        its_orders = ProduceTask.getUnallocatedOrders()
        my_orders = Order.objects.filter(status=0).count()

        first_order = Order.objects.filter(status=0)[0]
        id = first_order.id

        its_products_array = its_orders.get(id)["products"]
        true_products_array = OrderProduct.objects.filter(order_id=id)
        self.assertEqual(len(its_orders), my_orders)
        self.assertEqual(len(its_products_array), len(true_products_array))

    def test_getAllocatedOrders(self):
        its_orders = ProduceTask.getAllocatedOrders()
        my_orders = Order.objects.filter(status__gte=1)

        id = my_orders[0].id
        its_products_array = its_orders.get(id)["products"]
        my_products_array = OrderProduct.objects.filter(order_id=id)


        self.assertEqual(len(its_orders), len(my_orders))
        self.assertEqual(len(its_products_array), len(my_products_array))


    def test_createProduceTasks(self):
        old_amount = ProduceTaskBasic.objects.count()
        tl = [{
            "workshop_id": self.w1.id,
            "order_id": self.o1.id,
            "amount": 100,
            "topic": "topic",
            "person_in_charge": "CQX1"
        },
        {
            "workshop_id": self.w2.id,
            "order_id": self.o1.id,
            "amount": 120,
            "topic": "topic",
            "person_in_charge": "CQX2"
        }]
        tasks = ProduceTask.createTasks(tl)
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(old_amount+2, new_amount)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(type(tasks), type([]))
        self.assertEqual(type(tasks[0]), type({}))
        old_amount = new_amount
        tl = {
            "workshop_id": self.w1.id,
            "order_id": self.o1.id,
            "amount": 100,
            "topic": "topic",
            "person_in_charge": "CQX1"
        }
        tasks = ProduceTask.createTasks(tl)
        new_amount = ProduceTaskBasic.objects.count()
        self.assertEqual(old_amount+1, new_amount)
        self.assertEqual(type(tasks), type({}))

    def test_get_workshops(self):
        workshops = ProduceTask.getWorkshopsByProduct()
        self.assertEqual(type(workshops), type({}))
        self.assertEqual(type(workshops[self.p1.id]), type({}))
        self.assertEqual(len(workshops[self.p1.id]), 2)
        self.assertEqual(workshops[self.p2.id][self.w3.name], self.w3.id)

    def test_update_task(self):
        t = ProduceTaskBasic(personincharge="A", workshop=self.w1, number=200, topic="topic", order_id=self.o3.id)
        t.save()
        new_info = {
            "person_in_charge": "B",
            "workshop_id": self.w2.id,
            "amount": 100,
            "topic": "topic2",
            "status": "done",
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

