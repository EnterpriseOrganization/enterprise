# Create your views here.
import json
from django.http import HttpResponse
from enterprise.models import *
from django.core import serializers

def testExample(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
    # 测试用的例子

def GetAllOrder(request):
	Response=serializers.serialize("json", Order.objects.all());
	return HttpResponse(json.dumps(Response), content_type="application/json")
	# 获取到所有的订单信息

def AddOrder(request):
	info = "add order msg"
	if request.method == 'post':
		req = simplejson.loads(request.raw_post_data)
		date = req['date']
		indentor = req['indentor']
		receiver = req['receiver']
		checker = req['checker']
		recevieraddress = req['recevieraddress']
		indentorphonenumber = req['indentorphonenumber']
		totalprice = req['totalprice']
		status = req['status']
		deliverydate = req['deliverydate']
		paymentway= req['paymentway']
	return HttpResponse(info)