from enterprise.models import OrderProduct, ProduceTaskBasic, Workshop
from django.utils.dateparse import parse_date
from datetime import *
import app_product.util as util

# TODO: HyperMedia
def getUnallocatedOrders():
    each_order = getProductsByOrderStatus(0, 0)
    return each_order


def getAllocatedOrders():
    each_order = getProductsByOrderStatus(1, 3) # 先拿到所有已分配订单的货品信息
    return each_order


def getProductsByOrderStatus(gte, lte): # 想精确搜索就让 gte == lte
    """
    根据订单状态的范围返回相应每个订单包含的产品。要获取单一状态订单 只需使 gle=lte
    :param gte: 订单状态的最小值（大于等于）
    :param lte: 订单状态的最大值（小于等于）
    :return:
        {

        }
    """
    products = OrderProduct.objects.select_related('order', 'product') \
        .values('order_id', 'product_id','order__status','order__date', 'order__deliverydate', 'product__name', 'number') \
        .filter(order__status__gte=gte, order__status__lte=lte)
    orders = []
    for product in products:
        order_id = product["order_id"]
        # orders[order_id] = orders.get(order_id, {"products": []})
        # 拿到了每个订单下的产品列表
        orders.append({
            "order_id": order_id,
            "status": product["order__status"],
            #"deadline": product["order__deliverydate"],
            #"create_time": product["order__date"],
            "product_id": product['product_id'],
            "product_name": product['product__name'],
            "amount": product["number"],
            "tip": "comments",
            "detail": util.MyServer + "product/tasks/byorder?order_id={}".format(order_id)
        })
    return orders


def queryTasks(params=None):
    tasks = ProduceTaskBasic.objects.select_related('workshop').all()
    tasks_list = []
    for task in tasks:
        tasks_list.append(util.wrapTaskDTO(task))
    return tasks_list

def getTasksByTaskStatus(gte, lte):
    #tasks_list = queryTasks({"status__gte": gte, "status__lte": lte})
    tasks = ProduceTaskBasic.objects.filter(status__gte=gte, status__lte=lte)
    tasks_DTO = []
    for task in tasks:
        tasks_DTO.append(util.wrapTaskDTO(task))
    return tasks_list


def getTasksByOrderID(order_id):
    """
    获取某一订单的详细任务分配信息
    :param order_id:
    :return: [{
        taskDTO
    }]
    """
    # tasks_list = queryTasks({"order_id": order_id})
    tasks = ProduceTaskBasic.objects.select_related('workshop').filter(order_id=order_id)
    tasks_list = []
    for task in tasks:
        tasks_list.append(util.wrapTaskDTO(task))
    return tasks_list

def getTasksByWorkshopID(workshop_id):
    """
    获取某一车间的所有分配任务
    :param order_id:
    :return: [{
        taskDTO
    }]
    """
    #tasks_list = queryTasks({"workshop_id": workshop_id})
    tasks = ProduceTaskBasic.objects.select_related('workshop').filter(workshop_id=workshop_id)
    tasks_list = []
    for task in tasks:
        tasks_list.append(util.wrapTaskDTO(task))
    return tasks_list


def createTasks(tasks, order_id=-1, from_outside=True):
    """
    为一次订单创建多个生产任务
    :param
        tasks: list形式的任务详情,每个元素（任务详情）为dict形式:
        {
            "workshop_id": id necessary,
            "amount": number necessary,
            "person_in_charge": string,
            "topic": string
            "deadline": datetime string
        }
        order_id: 指明给哪个订单分配的任务
    :return: [{
        "task_id": id,
        "person_in_charge": string,
        "workshop_id": id,
        "workshop_name": string,
        "order_id": id,
        "topic": string,
        "status": string, 'done' or 'undone',
        "amount": number,
        "accurate_date": datetime string,
        "deadline": datetime string,
        "begin_date": datetime stringBasic
    }]

    """
    if order_id != -1:
        if from_outside:
            deleteTasksByOrderID(order_id)
        task_list = []
        if type(tasks) == type([]):
            for task in tasks:
                task_list.append(createTasks(task, order_id, False))
            return task_list
        elif type(tasks) == type({}):
            form = tasks
            task = ProduceTaskBasic()
            # columns client must send
            if form.get("workshop_id") == None or form.get("amount") == None:
                raise Exception(util.ErrMsg[0].format("missing important field: workshop_id or amount"))

            task.order_id = order_id
            task.workshop_id = form.get("workshop_id")
            task.number = form.get("amount")
            task.begindate = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
            # task.deadline = parse_date(form.get("deadline"))
            task.status = form.get("status", 0)
            task.personincharge = form.get("person_in_charge", "")
            task.topic = form.get("topic", "")
            task.save()
            return util.wrapTaskDTO(task)
        else:
            raise Exception(util.ErrMsg[0].format("need a list of tasks. create single task, please use 'createProduceTask'"))
    else:
        raise Exception(util.ErrMsg[0].format("need specify a order"))


def getWorkshops(product_id=-1, all=False):
    """
    返回所有车间 按能做的产品分组
    :param None
    :return: {
        "product_id":{
            "workshop_name": "workshop_id"
        }
    }
    """

    if product_id != -1:
        workshop_group = {}
        workshops = Workshop.objects.filter(product_id=product_id)
        for workshop in workshops:
            workshop_group[workshop.name] = workshop.id
        return workshop_group
    elif not all:
        product_group = {}
        workshops = Workshop.objects.all()
        for workshop in workshops:
            w_product = workshop.product
            product_group[w_product.id] = product_group.get(w_product.id, {})
            product_group[w_product.id][workshop.name] = workshop.id
        return product_group
    else:
        workshop_group = {}
        workshops = Workshop.objects.all()
        for workshop in workshops:
            workshop_group[workshop.name] = workshop.id
        return workshop_group



def updateTask(task_id, form):
    task =  ProduceTaskBasic.objects.get(pk=task_id)
    if type(form) == type({}):
        if form.get("person_in_charge"): task.personincharge = form.get("person_in_charge")
        if form.get("workshop_id"): task.workshop_id = form.get("workshop_id")
        if form.get("amount"): task.number = form.get("amount")
        if form.get("deadline"): task.deadline = parse_date(form.get("deadline"))
        if form.get("topic"): task.topic = form.get("topic")
        if form.get("status"): task.status = form.get("status")
        if form.get("material_getter"): task.material_getter = form.get("material_getter")
        if form.get("material_checker"): task.material_checker = form.get("material_checker")
        if form.get("material_distributon_date"): task.material_distributon_date = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        task.save()
        return util.wrapTaskDTO(task)
    else:
        raise Exception(util.ErrMsg[0].format("updates info must in dict format"))


def deleteTask(task_id):
    task = ProduceTaskBasic.objects.get(pk=task_id)
    amount_tuple = task.delete()
    return amount_tuple[0] # amounts of tasks being deleted


def deleteTasksByOrderID(order_id):
    tasks = ProduceTaskBasic.objects.filter(order_id=order_id)
    amount_tuple = tasks.delete()
    return amount_tuple[0]


# 貌似没人用
def deleteTasks(task_id_list):
    if(type(task_id_list)== type([])):
        for task_id in task_id_list:
            deleteTask(task_id)
    else:
        raise Exception(util.ErrMsg[0].format("using deleteTask to delete single task."))
