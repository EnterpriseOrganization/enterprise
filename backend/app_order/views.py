# Create your views here.
import json
from decimal import *
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
def getAllOrder(request):
	Response = serializers.serialize("json", Order.objects.all());
	return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# 获取post得到的json文件，然后将一条order数据添加到数据库，并返回是否添加成功的信息
def addOrder(request):
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
		diction = json.loads(request.raw_post_data)  # 加载json文件，将json转化为python的字典列表
		# 获取相关的key值
		date = diction[0]['date']
		indentor = diction[0]['indentor']
		receiver = diction[0]['receiver']
		checker = diction[0]['checker']
		recevieraddress = diction[0]['recevieraddress']
		indentorphonenumber = diction[0]['indentorphonenumber']
		totalprice = diction[0]['totalprice']
		status = diction[0]['status']
		deliverydate = diction[0]['deliverydate']
		paymentway = diction[0]['paymentway']

		o = Order(date=date,
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
		info = "add an order successfully"
	else:
		info = "get no json data"
	return HttpResponse(info)

# by ymk
# 删除一条订单记录
# 通过主键id值来删除
def deleteOrder(request):
	info = "Delete an Order"
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)

		id = diction[0]['id']
		Order.objects.filter(id=id).delete()
		info = "delete an order successfully"
	else:
		info = "get no json data"
	return HttpResponse(info)

# by zlz
# 修改一条订单记录
def updateOrder(request):
	info = "Update an Order"

	if request.method == 'post':
		diction = json.loads(request.raw_post_data)

		id = diction[0]['id']
		date = diction[0]['date']
		indentor = diction[0]['indentor']
		receiver = diction[0]['receiver']
		checker = diction[0]['checker']
		recevieraddress = diction[0]['recevieraddress']
		indentorphonenumber = diction[0]['indentorphonenumber']
		totalprice = diction[0]['totalprice']
		status = diction[0]['status']
		deliverydate = diction[0]['deliverydate']
		paymentway = diction[0]['paymentway']

		o = Order.objects.filter(id=id)

		o.date = date,
		o.indentor = indentor,
		o.receiver = receiver,
		o.checker = checker,
		o.recevieraddress = recevieraddress,
		o.indentorphonenumber = indentorphonenumber,
		o.totalprice = totalprice,
		o.status = status,
		o.deliverydate = deliverydate,
		o.paymentway = paymentway
		# 提高修改效率
		o.save()
		info = "update an order successfully"
	else:
		info = 'get no json data'

	return HttpResponse(info)

# by zlz
# 删除一个订单的某个产品
# 如果前端存储 id 的话使用 id 得到唯一记录
# 否则使用 productID 和 orderID 确定唯一记录（如果两者能确定一条记录）
def deleteOrderProduct(request):
	raw_post_data = '[{"id": 2, "orderID": 1000000000, "productID": 55}]'
	diction = json.loads(raw_post_data)
	id = diction[0]['id']
	order_id = diction[0]['orderID']
	product_id = diction[0]['productID']

	op = OrderProduct.objects.get(id=id)
	order_id = op.order.id
	price = op.price
	number = op.number
	op.delete()

	o = Order.objects.get(id=order_id)
	o.totalprice -= price * number
	o.save()
	info = 'delete an order product successfully'

	return HttpResponse(info)


# by zlz
# 后端修改一个订单所订购的产品数量
# 修改产品订购数量后对相应的订单的 totalprice 进行更新
def updateOrderProduct(request):
	info=""
	if request.method == 'post':
		# raw_post_data = '[{"id": 2, "number": 5, "orderID": 1000000000, "productID": 55}]'
		diction = json.loads(request.raw_post_data)
		id = diction[0]['id']
		number = diction[0]['number']
		order_id = diction[0]['orderID']
		product_id = diction[0]['productID']	

		op = OrderProduct.objects.get(id=id)
		price = op.price
		number_before = op.number
		op.number = number
		op.save()

		o = Order.objects.get(id=order_id)
		o.totalprice += (number - number_before) * price
		o.save()
		info = 'update an order product successfully'
	else:
		info = 'get no json data'
	return HttpResponse(info)




# by ymk
# 后端返回一个订单的所有产品函数 
# 后端返回一个订单的所有产品函数 ,接收一个json文件，获取到订单的id，显示出该订单中所有的产品
# 返回的是 单价 货品名字 货品id 货品数量 总价在前端计算
# 返回样例 {'price': Decimal('20'), 'name': 'testPro1', 'product': 1, 'number': 1}{'price': Decimal('30'), 'name': 'testPro2', 'product': 2, 'number': 1}
def showOrderProduct(request):
	# 测试用样例
	# data = '[{"id" : 1000000000}]'
	if request.method == 'post':
		id_diction=json.loads(request.raw_post_data)
		order_id=id_diction[0]['id']
		#获取到订单的id
		product_list =OrderProduct.objects.filter(order=order_id).values('product','number')
		# 获取到订单下的产品id
		res=[] #创建列表
		# 遍历产品id
		for pro in range(len(product_list)):
			productID=product_list[pro]['product']
			product_item=Product.objects.filter(id=productID).values('name','price')
			# 获取到产品的列表和单价
			# price = str(product_item[0]['price'].quantize(Decimal('0.0')))
			# product_item[0]['price'] = price
			temp={} #合并字典

			temp.update(product_list[pro])
			temp.update(product_item[0])
			res.append(temp) #将字典添加入列表
			for item in res:
				item['price'] = float(item['price'])
				#将decimal转换为float
		return HttpResponse(json.dumps(res))
	else:
		return HttpResponse("get no json")


# by ymk
# 测试用
def getAllOrderProduct(request):
	Response=serializers.serialize("json", OrderProduct.objects.all());
	return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# 添加一条orderproduct记录，接受从前端返回的json，订单的order_id，商品名称，单价，数量，（总价）？
# 传入的json 每一条应该包含的内容：订单id order，产品名字 name
def addOrderProduct(request):
	info = "add orderproduct msg"
	if request.method == 'post':
		diction = json.loads(request.raw_post_data)#加载json文件，将json转化为python的字典列表
		获取相关的key值
	# data='[{"order": 1000000000, "name": "testPro1", "number": 5, "price": 20},{"order": 1000000000, "name": "testPro2", "number": 7, "price": 32}]'
	# t=1
	# if t==1:
	# 	diction = json.loads(data)#加载json文件，将json转化为python的字典列表
	# 	# 测试用
		for dict_temp in range(len(diction)):
			order_id =diction[dict_temp]['order']#获取表单id
			order=Order.objects.get(id=order_id)# 获取order对象
			name =diction[dict_temp]['name']#获取product的名字
			product=Product.objects.get(name=name) #获取product对象
			number=diction[dict_temp]['number']#获取数量
			price=diction[dict_temp]['price']#获取单价
			op =OrderProduct(
				order=order,
				product=product,
				number=number,
				price=price
				)
			op.save()
			info="add an order successfully"
	else:
		info="get no json data"
	
	return HttpResponse(info)

