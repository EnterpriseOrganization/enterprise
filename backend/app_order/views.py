# Create your views here.
import json
from django.http import HttpResponse
from enterprise.models import *
from django.core import serializers
# by ymk
# 测试用的例子 
def testExample(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# by ymk
# 获取到所有的订单信息
def GetAllOrder(request):
	Response=serializers.serialize("json", Order.objects.all());
	return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# 获取post得到的json文件，然后将一条order数据添加到数据库，并返回是否添加成功的信息 
def AddOrder(request):
	info = "add order msg"
	#用于返回信息，是否增加成功
	# data = '[{"date": "2018-05-30T00:00:00Z", "indentor": "jack", "receiver": "nancy", "checker": "brad", "recevieraddress": "hsd", "indentorphonenumber": "1511468", "totalprice": "80", "status": 1, "deliverydate": "2018-06-20T00:00:00Z", "paymentway": "wechat"}]'
	# 测试用的数据
	# if request.method == 'post':
		# req = json.loads(request.raw_post_data)
		# date = req['date']
		# indentor = req['indentor']
		# receiver = req['receiver']
		# checker = req['checker']
		# recevieraddress = req['recevieraddress']
		# indentorphonenumber = req['indentorphonenumber']
		# totalprice = req['totalprice']
		# status = req['status']
		# deliverydate = req['deliverydate']
		# paymentway= req['paymentway']
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)#加载json文件，将json转化为python的字典列表
		# 获取相关的key值
		date =diction[0]['date']
		indentor =diction[0]['indentor']
		receiver = diction[0]['receiver']
		checker =diction[0]['checker']
		recevieraddress =diction[0]['recevieraddress']
		indentorphonenumber =diction[0]['indentorphonenumber']
		totalprice =diction[0]['totalprice']
		status =diction[0]['status']
		deliverydate =diction[0]['deliverydate']
		paymentway =diction[0]['paymentway']

		o=Order(date=date,
			indentor=indentor,
			receiver=receiver,
			checker=checker,
			recevieraddress=recevieraddress,
			indentorphonenumber=indentorphonenumber,
			totalprice=totalprice,
			status=status,
			deliverydate=deliverydate,
			paymentway=paymentway
			)
		o.save()
		info="add an order successfully"
	else:
		info="get no json data"
	return HttpResponse(info)

# by ymk
# 删除一条订单记录
# 通过主键id值来删除
def DeleteOrder(request):
	info="Delete an Order"
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)

		id = diction[0]['id']
		Order.objects.filter(id=id).delete()
		info="delete an order successfully"
	else:
		info="get no json data"
	return HttpResponse(info)

# by zlz
# 修改一条订单记录
def UpdateOrder(request):
	info = "Update an Order"
	
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)

		id = diction[0]['id']
		date =diction[0]['date']
		indentor =diction[0]['indentor']
		receiver = diction[0]['receiver']
		checker =diction[0]['checker']
		recevieraddress =diction[0]['recevieraddress']
		indentorphonenumber =diction[0]['indentorphonenumber']
		totalprice =diction[0]['totalprice']
		status =diction[0]['status']
		deliverydate =diction[0]['deliverydate']
		paymentway = diction[0]['paymentway']

		o = Order.objects.filter(id=id)
		
		o.date=date,
		o.indentor=indentor,
		o.receiver=receiver,
		o.checker=checker,
		o.recevieraddress=recevieraddress,
		o.indentorphonenumber=indentorphonenumber,
		o.totalprice=totalprice,
		o.status=status,
		o.deliverydate=deliverydate,
		o.paymentway=paymentway
		# 提高修改效率
		o.save()
		info = "update an order successfully"
	else:
		info = 'get no json data'

	return HttpResponse(info)

# by zlz
# 删除一个订单的某个产品
def DeleteOrderProduct(request):
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)
		id = diction[0]['id']  # orderproduct primary key

		order_product = OrderProduct.objects.get(id=id)
		order_id = order_product.orderID
		price = order_product.price
		order_product.delete()

		o = Order.objects.get(id=order_id)
		o.totalprice -= price
		o.save()
		info = 'delete an order product successfully'
	else:
		info = 'get no json data'
	
	return HttpResponse(info)




# by zlz
# 后端修改一个订单的
def UpdateOrderProduct(request):
	# if request.method == 'post':
	# 	diction = json.loads(request.raw_post_data)




# by ymk
# 后端返回一个订单的所有产品函数 
# 后端返回一个订单的所有产品函数 ,接收一个json文件，获取到订单的id，显示出该订单中所有的产品
# 返回的是 单价 货品名字 货品id 货品数量 总价在前端计算
# 返回样例 {'price': Decimal('20'), 'name': 'testPro1', 'product': 1, 'number': 1}{'price': Decimal('30'), 'name': 'testPro2', 'product': 2, 'number': 1}
def ShowOrderProduct(request):
	data = '[{"id" : 1000000000}]'
	id_diction=json.loads(data)
	order_id=id_diction[0]['id']
	#获取到订单的id
	product_list =OrderProduct.objects.filter(order=order_id).values('product','number')


	res=[] #创建列表
	for pro in range(len(product_list)):
		productID=product_list[pro]['product']
		product_item=Product.objects.filter(id=productID).values('name','price')
		price = float(product_item[0]['price'])
		product_item[0]['price'] = price
		temp={} #合并字典
		temp.update(product_list[pro])
		temp.update(product_item[0])
		res.append(temp) #将字典添加入列表
	return HttpResponse(res)


