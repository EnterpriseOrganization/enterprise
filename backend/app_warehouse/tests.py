from django.test import TestCase,Client
from enterprise.models import MaterialClass, Material,InventoryInformation
from .views_warehouse import *
from django.contrib.auth.models import User
# Create your tests here.
class InventoryInformationTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user('yanhua','2444870620@qq.com','yanhuapassword')
        self.device = Device(hostname="127.0.0.1:8000", mac="ff:ff:ff:ff:ff:ff", user=self.user).save()
        import time
        MaterialClass.objects.create(class_field = '0', parent_class = '0')
        MaterialClass.objects.create(class_field = '1', parent_class = '0')
        MaterialClass.objects.create(class_field = '2', parent_class = '1')
        material_class_hello = MaterialClass.objects.get(class_field = '0')
        material_class_world = MaterialClass.objects.get(class_field = '1')
        material_class_comma = MaterialClass.objects.get(class_field = '2')
        Material.objects.create(name = 'hello', class_obj = material_class_hello)
        Material.objects.create(name = 'world', class_obj = material_class_world)
        Material.objects.create(name = 'comma', class_obj = material_class_comma)
        material_hello = Material.objects.get(name = 'hello')
        material_world = Material.objects.get(name = 'world')
        material_comma = Material.objects.get(name = 'comma')
        InventoryInformation.objects.create(material = material_hello,
                                            shelfnumber = 'A-101',number = 100, threshold = 10,\
                                            newestinwarehousedate = time.localtime( ))
        InventoryInformation.objects.create(material = material_world,
                                            shelfnumber = 'A-102',number = 200, threshold = 20,\
                                            newestinwarehousedate = time.localtime( ))
        InventoryInformation.objects.create(material = material_comma,
                                            shelfnumber = 'A-103',number = 300, threshold = 30,\
                                            newestinwarehousedate = time.localtime( ))        
    #def test_getParams(self):
        #c = Client()
        #answer = c.post("/warehouse/test-request",{"material": "hello"})
        #answer = answer.json()
        #test_answer = {
            #'material' : 'hello',
        #}
        ##answer = getParams(req)
        #self.assertEqual(test_answer, answer)
        
    def test_getInventory(self):
        c = Client()
        res = c.post("/warehouse/get-inventory",{"material": "hello"})
        
        test_answer = {
            "material": "hello",
            "shelfnumber": "A-101",
            "number": "100",
            'threshold':'10'
        }
        self.asserEqual(res['material'],test_answer['material'])
        self.asserEqual(res['shelfnumber'],test_answer['shelfnumber'])
        self.asserEqual(res['number'],test_answer['number'])
        self.asserEqual(res['threshold'],test_answer['threshold'])        
        