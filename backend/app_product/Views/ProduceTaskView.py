from app_product.Views import ProduceTask
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_GET
def getAllTasks(request):
    """
        非真正意义的生产任务，还包括订单中未被分配的产品生产任务
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

    l = ProduceTask.getAllocatedOrders()
    l.extend(ProduceTask.getUnallocatedOrders())
    return JsonResponse({"tasks": l})


@require_GET
def getOrderTasks(request):
    """
    返回指定order的所有生产任务
    :param request: GET /product/tasks/byorder/<order_id>
    :param order_id:
    :return: {
        "tasks": [{ taskDTO }]
    }
    """
    order_id = request.GET.get("order_id")
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
    tasks = ProduceTask.getTasksByTaskStatus(1, 1)
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
def getWorkshopByProduct(request):
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
    product_id = request.GET.get("product_id")
    workshops = ProduceTask.getWorkshops(product_id)
    return JsonResponse({"workshops": workshops})


@csrf_exempt
@require_POST
def createTasks(request):
    """
    为指定订单创建生产任务
    :param request:  POST product/task/create
    :param json body: {
        "order_id": id
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
    order_id = params["order_id"]
    if order_id != -1:
        try:
            tasks = ProduceTask.createTasks(params["tasks"], order_id)
            return JsonResponse({"tasks": tasks})
        except Exception as e:
            return JsonResponse({"error message": e}, status=500)
    else:
        return JsonResponse({}, status=401)


def checkUpdateInfo(form):
    #if form["material_checker"] == None or form["material_getter"] == None :
        #return False
    return True


@csrf_exempt
@require_POST
def updateTaskMaterialGet(request):
    """
    更新生产任务状态为已领料 并更新审核人, 领取人 POST /product/task/material-allocated
    :param request body:{
        "task_id":
        "info":{
            "material_getter":
            "material_checker":
        }
    }
    :return: {
        "task": taskDTO
    }
    """
    body_unicode = request.body.decode('utf-8')
    params = json.loads(body_unicode)
    task_id = params["task_id"]
    info = params["info"]
    if task_id != -1 and checkUpdateInfo(info):
        info["status"] = 1
        task = ProduceTask.updateTask(task_id, info)
        return JsonResponse({"task": task})
    else:
        return JsonResponse({}, status=401)


@csrf_exempt
@require_POST
def updateTaskDone(request):
    """
    更新指定任务为已完成  POST /product/task/done
    :param request:
    :param task_id:
    :return: {
        "task": taskDTO
    }
    """
    body_unicode = request.body.decode('utf-8')
    params = json.loads(body_unicode)
    task_id = params["task_id"]
    if task_id:
        params = {
            "status": 2
        }
        task = ProduceTask.updateTask(task_id, params)
        return JsonResponse({"task": task})
    else:
        return JsonResponse({}, status=401)
