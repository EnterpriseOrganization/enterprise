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
# 更新单条信息的状态，0变1,1变0
def  updateOneOrder(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
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
# 将选择的订单信息全部改为完成
def completeOrders(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
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
# 将选择的订单信息全部删除，传入的json应该是一个数组，数组中的每一个元素应该是 id:1000000
def deleteOrders(request):
    user=request.user
    info="no permission"
    if(user.has_perm('modify_Order')):
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
        diction = json.loads(req_str)
        for i in range(len(diction)):
            id = diction[i]['id']
            o=Order.objects.get(id=int(id))
            OrderProduct.objects.filter(order=o).delete()
            Order.objects.filter(id=int(id)).delete() #级联删除
        info="update orders successfully"
        result = 1
    else:
        info="no permission"
        result = 2
    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# 增加用户权限控制
def updateOrderDetail(request):
    user=request.user
    if(user.has_perm('modify_Order')):
        info = ""
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
        diction = json.loads(req_str)
        print(diction)
        # 获取相关的key值
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
        #获取到 order对象
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
        # 提高修改效率
        o.save()
        for dict_temp in range(len(diction['product'])):
            id = diction['product'][dict_temp]['product']#获取product的id
            product = Product.objects.get(id = id) #获取product对象
            number = diction['product'][dict_temp]['number']#获取数量
            price = product.price#获取单价

            op_temp = OrderProduct.objects.filter(order=o)
            op =op_temp.filter()
            if(op_temp):
                op.number=number
                price=price
                info="update an order successfully"
                result = 1
            else: 
                # 查询是否存在相应的order_product
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
# 获取单条订单的信息
def getOrderDetail(request):
    req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
    # req_str = '[{"id": 1000000000}]' 测试用
    id_diction = json.loads(req_str)
    order_id = id_diction['order']
    # 获取order的id
    o_res = Order.objects.filter(id=order_id) # 获取订单
    # o_res = serializers.serialize("json", o);
    product_list = OrderProduct.objects.filter(order=order_id).values('product','number')
    # 获取到订单下的产品id
    res=[] #创建列表
    
    # 遍历产品id
    for pro in range(len(product_list)):
        productID=product_list[pro]['product']
        product_item=Product.objects.filter(id=productID).values('id','name','price')
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
    
    Response = serializers.serialize("json", o_res);
    res_dict={"product":res,"order":Response}
    return HttpResponse(json.dumps(res_dict))
        
# by ymk 
# 获取到特定条件下的订单信息返回，发送的信息应该包括 订单状态 "status": 1,开始时间："date": "2018-05-30T00:00:00Z",截止时间"deliverydate": "2018-06-20T00:00:00Z"，订货商"indentor": "jack"
# 0: 待生产 1: 生产中 2:配送中（生产完成） 3: 采购中
def getSpecificOrder(request):
    req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
    #req_str = '[{"status": "","date":"","deliverydate":"2018-06-20T00:00:00Z", "indentor": ""}]' #测试用数据
    diction = json.loads(req_str) #返回的是一个字典list长度为1 {'deliverydate': '2018-06-20T00:00:00Z', 'date': '2018-05-30T00:00:00Z', 'indentor': 'jack', 'status': 1}
    o = Order.objects.all() #先获取所有的信息
    #print(diction)
    # print(diction['indentor'])

    for key in diction:# 依次遍历查询
        temp = o
        diction[key] = diction[key].strip()#去掉所有的空格
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
    Response=serializers.serialize("json", o);#序列化对象
    return HttpResponse(json.dumps(Response))	

# by ymk
# 获取到所有的产品信息
# 返回样例"[{"model": "enterprise.product", "pk": 1, "fields": {"name": "testPro1", "class_obj": 1, "price": "20"}}, {"model": "enterprise.product", "pk": 2, "fields": {"name": "testPro2", "class_obj": 1, "price": "32"}}]"
def getAllProduct(request):
    Response = serializers.serialize("json", Product.objects.all());
    return HttpResponse(json.dumps(Response), content_type="application/json")

# by ymk
# 获取post得到的json文件，然后将一条order数据添加到数据库，并返回是否添加成功的信息
def addOrder(request):
    info = "add order msg"
    o_id = "null"
    #用于返回信息，是否增加成功
    # data = '[{"date": "2018-05-30T00:00:00Z", "indentor": "jack", "receiver": "nancy", "checker": "brad", "recevieraddress": "hsd", "indentorphonenumber": "1511468", "totalprice": "80", "status": 1, "deliverydate": "2018-06-20T00:00:00Z", "paymentway": "wechat"}]'
    # 测试用的数据
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
            req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
            diction = json.loads(req_str)
            print(diction)
            # 获取相关的key值
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
            order = Order.objects.last()# 获取order对象
            o_id =order.id
            for dict_temp in range(len(diction['product'])):
                id = diction['product'][dict_temp]['product']#获取product的id
                product = Product.objects.get(id = id) #获取product对象
                number = diction['product'][dict_temp]['number']#获取数量
                price = product.price#获取单价
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

# by ymk and 修改ok
# 删除一条订单记录
# 通过主键id值来删除
def deleteOrder(request):
    info = "Delete an Order"
    if request.method == 'POST':
        user=request.user
        if(user.has_perm('modify_Order')):
            req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
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
# 修改一条订单记录
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
            # 提高修改效率
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
    result = 1

    msg={"info":info, "result": result}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by zlz
# 后端修改一个订单所订购的产品数量
# 修改产品订购数量后对相应的订单的 totalprice 进行更新
def updateOrderProduct(request):
    info=""
    if request.method == 'POST':
        # raw_post_data = '[{"id": 2, "number": 5, "orderID": 1000000000, "productID": 55}]'
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
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
# 后端返回一个订单的所有产品函数 
# 后端返回一个订单的所有产品函数 ,接收一个json文件，获取到订单的id，显示出该订单中所有的产品
# 返回的是 单价 货品名字 货品id 货品数量 总价在前端计算
# 返回样例 [{"name": "testPro1", "number": 5, "price": 20.0, "product": 1}, {"name": "testPro2", "number": 7, "price": 32.0, "product": 2}]
def showOrderProduct(request):
    # 测试用样例
    # data = '[{"id" : 1000000000}]'
    if request.method == 'POST':
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
        diction = json.loads(req_str)
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
# 添加一条OrderProduct记录，接受从前端返回的json，订单的order_id，商品名称，单价，数量，（总价）？
# 传入的json 每一条应该包含的内容：订单id order，产品名字 name
def addOrderProduct(request):
    info = "add OrderProduct msg"
    if request.method == 'POST':
        req_str = request.body.decode('utf-8')  # 加载json文件，将json转化为python的字典列表
        diction = json.loads(req_str)
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
    
    msg={"info":info}
    return HttpResponse(json.dumps(msg), content_type="application/json")

# by ymk
# 测试用
def getAllOrderProduct(request):
    Response=serializers.serialize("json", OrderProduct.objects.all());
    return HttpResponse(json.dumps(Response), content_type="application/json")