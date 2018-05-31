# Create your views here.
import json
from django.http import HttpResponse
from enterprise.models import *
from django.core import serializers

# 测试用的例子
def testExample(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# 获取到所有的订单信息
def GetAllOrder(request):
	Response=serializers.serialize("json", Order.objects.all());
	return HttpResponse(json.dumps(Response), content_type="application/json")

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