from app_product.Views import ProduceTask
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_GET
def getAllTasks(request):
    """
        :arg: GET /product/tasks
        :return:
            {
                "unallocated":{
                    "order_id":{
                        "products": [{
                            "product_id": number,
                            "product_name": name,
                            "amount": number
                        }]
                    }
                },
                "allocated: {
                    same as above
                }
            }
    """

    res = {
        "allocated": ProduceTask.getAllocatedOrders(),
        "unallocated": ProduceTask.getUnallocatedOrders()
    }
    return JsonResponse(res)


@require_GET
def getOrderTasks(request, order_id=-1):
    """
    返回指定order的所有生产任务
    :param request: GET /product/tasks/byorder/<order_id>
    :param order_id:
    :return: {
        "tasks": [{ taskDTO }]
    }
    """
    if order_id != -1:
        tasks = ProduceTask.getTasksByOrderID(order_id)
        return JsonResponse({"tasks": tasks})
    else:
        return JsonResponse({}, status=401)


@require_GET
def getHistoryTasks(request):
    """
    获得所有生产完成的任务
    :param request:  GET /product/tasks/history
    :return: {
        "tasks": [taskDTO]
    }
    """
    tasks = ProduceTask.getTasksByTaskStatus(2, 2)
    return JsonResponse({"tasks": tasks})


@require_GET
def getUndoneTasks(request):
    """
    返回所有未完成的生产计划
    :param request:  GET /product/tasks/undone
    :return: {
        "tasks": [taskDTO]
    }
    """
    tasks = ProduceTask.getTasksByTaskStatus(0, 1)
    return JsonResponse({"tasks": tasks})


@require_GET
def getWorkshops(request):
    """
    返回所有车间, 按能做的产品分类
    :param request: GET /product/workshop
    :return: {
        "workshops": {
            "product_id": {
                "workshop_name": "workshop_id"
            }
        }
    }
    """
    workshops = ProduceTask.getWorkshops()
    return JsonResponse({"workshops": workshops})


@require_GET
def getWorkshopByProduct(request, product_id=-1):
    """
    返回可以生产指定成品的所有车间
    :param request:
    :param product_id:
    :return: {
        "workshops": {
            workshop_name: workshop_id,
        }
    }
    """
    workshops = ProduceTask.getWorkshops(product_id)
    return JsonResponse({"workshops": workshops})


@csrf_exempt
@require_POST
def createTasks(request, order_id=-1):
    """
    为指定订单创建生产任务
    :param request:  POST product/create
    :param order_id: 为哪个订单创建的请求
    :param json body: {
        "tasks": [{
            "workshop_id": id necessary,
            "amount": number necessary,
            "person_in_charge": string,
            "topic": string
            "deadline": datetime string
        }]
    }
    :return: {
        "tasks": [{
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
            "begin_date": datetime string
        }]
    }
    """
    body_unicode = request.body.decode('utf-8')
    params = json.loads(body_unicode)
    if order_id != -1:
        try:
            tasks = ProduceTask.createTasks(params["tasks"], order_id)
            return JsonResponse({"tasks": tasks})
        except Exception as e:
            return JsonResponse({"error message": e.args[0]}, status=401)
    else:
        return JsonResponse({}, status=401)


def checkUpdateInfo(form):
    if form["material_checker"] == None or form["material_getter"] == None :
        return False
    return True


@csrf_exempt
@require_POST
def updateTaskMaterialGet(request, task_id=-1):
    """
    更新生产任务状态为已领料 并更新审核人, 领取人
    :param request:
    :param task_id:
    :return: {
        "task": taskDTO
    }
    """
    body_unicode = request.body.decode('utf-8')
    params = json.loads(body_unicode)
    if task_id != -1 and checkUpdateInfo(params):
        params["status"] = 1
        task = ProduceTask.updateTask(task_id, params)
        return JsonResponse({"task": task})
    else:
        return JsonResponse({}, status=401)


@csrf_exempt
@require_POST
def updateTaskDone(request, task_id=-1):
    """
    更新指定任务为已完成
    :param request:
    :param task_id:
    :return: {
        "task": taskDTO
    }
    """
    if task_id != -1:
        params = {
            "status": 2
        }
        task = ProduceTask.updateTask(task_id, params)
        return JsonResponse({"task": task})
    else:
        return JsonResponse({}, status=401)