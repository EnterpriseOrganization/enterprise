# -*- coding: utf-8 -*-
# Create your views here.
import json
from decimal import *
from django.http import HttpResponse
from django.http import JsonResponse
from enterprise.models import *
from django.core import serializers
from decimal import Decimal
from django.db import models
# by ymk
# �����õ�����
def testExample(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# by ymk
# ��ȡ�����еĶ�����Ϣ
def getAllOrder(request):
    Response = serializers.serialize("json", Order.objects.all());
    return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# ���µ�����Ϣ��״̬��0��1,1��0
def  updateOneOrder(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
        order_id=diction['order']
        o = Order.objects.filter(id = order_id)[0]
        if(o.status == 1):
            o.status = 0
        elif(o.status == 0):
            o.status = 1
        o.save()
        info="update order successfully"
        result  = 1
    else:
        info = "no permission"
        result = 2
    msg={"info": info, "result": result}
    return HttpResponse(json.dumps(msg), content_type = "application/json")

# by ymk
# ��ѡ��Ķ�����Ϣȫ����Ϊ���
def completeOrders(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
        for i in range(len(diction)):
            o_id = diction[i]['id']
            o = Order.objects.filter(id=o_id)[0]
            o.status=1
            o.save()
        info="update orders successfully"
        result = 1
    else:
        info="no permission"
        result = 2
    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# ��ѡ��Ķ�����Ϣȫ��ɾ���������jsonӦ����һ�����飬�����е�ÿһ��Ԫ��Ӧ���� id:1000000
def deleteOrders(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
        for i in range(len(diction)):
            id = diction[i]['id']
            o=Order.objects.get(id=int(id))
            OrderProduct.objects.filter(order=o).delete()
            Order.objects.filter(id=int(id)).delete() #����ɾ��
        info="update orders successfully"
        result = 1
    else:
        info="no permission"
        result = 2
    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# �����û�Ȩ�޿���
def updateOrderDetail(request):
    user=request.user
    if(user.has_perm('modify_Order')):
        info = ""
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
        print(diction)
        # ��ȡ��ص�keyֵ
        order_id = diction['order_data']['id']
        date = diction['order_data']['date']
        indentor = diction['order_data']['indentor']
        receiver = diction['order_data']['receiver']
        checker = diction['order_data']['checker']
        recevieraddress = diction['order_data']['recevieraddress']
        indentorphonenumber = diction['order_data']['indentorphonenumber']
        totalprice = diction['order_data']['totalprice']
        status = diction['order_data']['status']
        deliverydate = diction['order_data']['deliverydate']
        paymentway = diction['order_data']['paymentway']
        o = Order.objects.filter(id=order_id)[0]
        #��ȡ�� order����
        o.date = date
        o.indentor = indentor
        o.receiver = receiver
        o.checker = checker
        o.recevieraddress = recevieraddress
        o.indentorphonenumber = indentorphonenumber
        o.totalprice = totalprice
        o.status = status
        o.deliverydate = deliverydate
        o.paymentway = paymentway
        # ����޸�Ч��
        o.save()
        for dict_temp in range(len(diction['product'])):
            id = diction['product'][dict_temp]['product']#��ȡproduct��id
            product = Product.objects.get(id = id) #��ȡproduct����
            number = diction['product'][dict_temp]['number']#��ȡ����
            price = product.price#��ȡ����

            op_temp = OrderProduct.objects.filter(order=o)
            op =op_temp.filter()
            if(op_temp):
                op.number=number
                price=price
                info="update an order successfully"
                result = 1
            else: 
                # ��ѯ�Ƿ������Ӧ��order_product
                op = OrderProduct(
                    order = o,
                    product = product,
                    number = number,
                    price = price
                    )
                op.save()
                info="add an order successfully"
                result = 1
    else:
        info="no permission"
        result = 2

    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# ��ȡ������������Ϣ
def getOrderDetail(request):
    req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
    # req_str = '[{"id": 1000000000}]' ������
    id_diction = json.loads(req_str)
    order_id = id_diction['order']
    # ��ȡorder��id
    o_res = Order.objects.filter(id=order_id) # ��ȡ����
    # o_res = serializers.serialize("json", o);
    product_list = OrderProduct.objects.filter(order=order_id).values('product','number')
    # ��ȡ�������µĲ�Ʒid
    res=[] #�����б�
    
    # ������Ʒid
    for pro in range(len(product_list)):
        productID=product_list[pro]['product']
        product_item=Product.objects.filter(id=productID).values('id','name','price')
        # ��ȡ����Ʒ���б�͵���
        # price = str(product_item[0]['price'].quantize(Decimal('0.0')))
        # product_item[0]['price'] = price
        temp={} #�ϲ��ֵ�
        temp.update(product_list[pro])
        temp.update(product_item[0])
        res.append(temp) #���ֵ�������б�
        for item in res:
            item['price'] = float(item['price'])
            #��decimalת��Ϊfloat
    
    Response = serializers.serialize("json", o_res);
    res_dict={"product":res,"order":Response}
    return HttpResponse(json.dumps(res_dict))
        
# by ymk 
# ��ȡ���ض������µĶ�����Ϣ���أ����͵���ϢӦ�ð��� ����״̬ "status": 1,��ʼʱ�䣺"date": "2018-05-30T00:00:00Z",��ֹʱ��"deliverydate": "2018-06-20T00:00:00Z"��������"indentor": "jack"
# 0: ������ 1: ������ 2:�����У�������ɣ� 3: �ɹ���
def getSpecificOrder(request):
    req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
    #req_str = '[{"status": "","date":"","deliverydate":"2018-06-20T00:00:00Z", "indentor": ""}]' #����������
    diction = json.loads(req_str) #���ص���һ���ֵ�list����Ϊ1 {'deliverydate': '2018-06-20T00:00:00Z', 'date': '2018-05-30T00:00:00Z', 'indentor': 'jack', 'status': 1}
    o = Order.objects.all() #�Ȼ�ȡ���е���Ϣ
    #print(diction)
    # print(diction['indentor'])

    for key in diction:# ���α�����ѯ
        temp = o
        diction[key] = diction[key].strip()#ȥ�����еĿո�
        if(diction[key]!=""):
            if(key == 'status'):
                temp = o.filter(status=diction[key])
            elif(key == 'date'):
                temp = o.filter(date=diction[key])
            elif(key == 'deliverydate'):
                temp = o.filter(deliverydate=diction[key])
            elif(key == 'indentor'):
                temp = o.filter(indentor=diction[key])
        o = temp
    Response=serializers.serialize("json", o);#���л�����
    return HttpResponse(json.dumps(Response))	

# by ymk
# ��ȡ�����еĲ�Ʒ��Ϣ
# ��������"[{"model": "enterprise.product", "pk": 1, "fields": {"name": "testPro1", "class_obj": 1, "price": "20"}}, {"model": "enterprise.product", "pk": 2, "fields": {"name": "testPro2", "class_obj": 1, "price": "32"}}]"
def getAllProduct(request):
    Response = serializers.serialize("json", Product.objects.all());
    return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# ��ȡpost�õ���json�ļ���Ȼ��һ��order������ӵ����ݿ⣬�������Ƿ���ӳɹ�����Ϣ
def addOrder(request):
    info = "add order msg"
    o_id = "null"
    #���ڷ�����Ϣ���Ƿ����ӳɹ�
    # data = '[{"date": "2018-05-30T00:00:00Z", "indentor": "jack", "receiver": "nancy", "checker": "brad", "recevieraddress": "hsd", "indentorphonenumber": "1511468", "totalprice": "80", "status": 1, "deliverydate": "2018-06-20T00:00:00Z", "paymentway": "wechat"}]'
    # �����õ�����
    # if request.method == 'POST':
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
    if request.method == 'POST':
        user=request.user
        print(user)
        if(user.has_perm('modify_Order')):
            req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
            diction = json.loads(req_str)
            print(diction)
            # ��ȡ��ص�keyֵ
            date = diction['order_data']['date']
            indentor = diction['order_data']['indentor']
            receiver = diction['order_data']['receiver']
            checker = diction['order_data']['checker']
            recevieraddress = diction['order_data']['recevieraddress']
            indentorphonenumber = diction['order_data']['indentorphonenumber']
            totalprice = float(diction['order_data']['totalprice'])
            status = diction['order_data']['status']
            deliverydate = diction['order_data']['deliverydate']
            paymentway = diction['order_data']['paymentway']
            try:
                o = Order(
                    date=date,
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
            except Exception as e:
                print(e)
            # o.save()
            info = "add an order successfully"
            order = Order.objects.last()# ��ȡorder����
            o_id =order.id
            for dict_temp in range(len(diction['product'])):
                id = diction['product'][dict_temp]['product']#��ȡproduct��id
                product = Product.objects.get(id = id) #��ȡproduct����
                number = diction['product'][dict_temp]['number']#��ȡ����
                price = product.price#��ȡ����
                try:
                    op = OrderProduct(
                        order = order,
                        product = product,
                        number = number,
                        price = price
                    )
                    op.save()
                except Exception as e:
                    print(e)
                info="add an order successfully"
                result = 1
        else:
            info="no permission"
            result = 2

    else:
        info = "get no json data"
        result = 3
    msg={"info":info,"id":o_id, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk and �޸�ok
# ɾ��һ��������¼
# ͨ������idֵ��ɾ��
def deleteOrder(request):
    info = "Delete an Order"
    if request.method == 'POST':
        user=request.user
        if(user.has_perm('modify_Order')):
            req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
            diction = json.loads(req_str)
            print(diction)

            id = diction['order']
            o=Order.objects.get(id=int(id))
            OrderProduct.objects.filter(order=o).delete()
            Order.objects.filter(id=int(id)).delete()

            info = "delete an order successfully"
            result = 1
        else:
            info = "no permission"
            result = 2
    else:
        info = "get no json data"
        result = 3
    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by zlz
# �޸�һ��������¼
def updateOrder(request):
    info = "Update an Order"

    if request.method == 'POST':
        user=request.user
        if(user.has_perm('modify_Order')):
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
            # ����޸�Ч��
            o.save()
            info = "update an order successfully"
            result  = 1
        else:
            info = "no permission"
            result = 2
    else:
        info = 'get no json data'
        result = 3

    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by zlz
# ɾ��һ��������ĳ����Ʒ
# ���ǰ�˴洢 id �Ļ�ʹ�� id �õ�Ψһ��¼
# ����ʹ�� productID �� orderID ȷ��Ψһ��¼�����������ȷ��һ����¼��
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
    result = 1

    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by zlz
# ����޸�һ�������������Ĳ�Ʒ����
# �޸Ĳ�Ʒ�������������Ӧ�Ķ����� totalprice ���и���
def updateOrderProduct(request):
    info=""
    if request.method == 'POST':
        # raw_post_data = '[{"id": 2, "number": 5, "orderID": 1000000000, "productID": 55}]'
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
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
        result = 1
    else:
        info = 'get no json data'
        result = 2
    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# ��˷���һ�����������в�Ʒ���� 
# ��˷���һ�����������в�Ʒ���� ,����һ��json�ļ�����ȡ��������id����ʾ���ö��������еĲ�Ʒ
# ���ص��� ���� ��Ʒ���� ��Ʒid ��Ʒ���� �ܼ���ǰ�˼���
# �������� [{"name": "testPro1", "number": 5, "price": 20.0, "product": 1}, {"name": "testPro2", "number": 7, "price": 32.0, "product": 2}]
def showOrderProduct(request):
    # ����������
    # data = '[{"id" : 1000000000}]'
    if request.method == 'POST':
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
        order_id=id_diction[0]['id']
        #��ȡ��������id
        product_list =OrderProduct.objects.filter(order=order_id).values('product','number')
        # ��ȡ�������µĲ�Ʒid
        res=[] #�����б�
        # ������Ʒid
        for pro in range(len(product_list)):
            productID=product_list[pro]['product']
            product_item=Product.objects.filter(id=productID).values('name','price')
            # ��ȡ����Ʒ���б�͵���
            # price = str(product_item[0]['price'].quantize(Decimal('0.0')))
            # product_item[0]['price'] = price
            temp={} #�ϲ��ֵ�

            temp.update(product_list[pro])
            temp.update(product_item[0])
            res.append(temp) #���ֵ�������б�
            for item in res:
                item['price'] = float(item['price'])
                #��decimalת��Ϊfloat
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse("get no json")

# by ymk
# ���һ��OrderProduct��¼�����ܴ�ǰ�˷��ص�json��������order_id����Ʒ���ƣ����ۣ����������ܼۣ���
# �����json ÿһ��Ӧ�ð��������ݣ�����id order����Ʒ���� name
def addOrderProduct(request):
    info = "add OrderProduct msg"
    if request.method == 'POST':
        req_str = request.body.decode('utf-8')  # ����json�ļ�����jsonת��Ϊpython���ֵ��б�
        diction = json.loads(req_str)
    # data='[{"order": 1000000000, "name": "testPro1", "number": 5, "price": 20},{"order": 1000000000, "name": "testPro2", "number": 7, "price": 32}]'
    # t=1
    # if t==1:
    # 	diction = json.loads(data)#����json�ļ�����jsonת��Ϊpython���ֵ��б�
    # 	# ������
        for dict_temp in range(len(diction)):
            order_id =diction[dict_temp]['order']#��ȡ��id
            order=Order.objects.get(id=order_id)# ��ȡorder����
            name =diction[dict_temp]['name']#��ȡproduct������
            product=Product.objects.get(name=name) #��ȡproduct����
            number=diction[dict_temp]['number']#��ȡ����
            price=diction[dict_temp]['price']#��ȡ����
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
    
    msg={"info":info}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# ������
def getAllOrderProduct(request):
    Response=serializers.serialize("json", OrderProduct.objects.all());
    return HttpResponse(json.dumps(Response), content_type="application/json")