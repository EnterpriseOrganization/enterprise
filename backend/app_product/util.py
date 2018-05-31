ErrMsg = [
    "Format Error, {}"
]

def wrapTaskDTO(task): # task should be querySet object
    # 0: 未分配 1：已分配,待领料 2： 已领料,待生产 3: 生产完成
    if task.status == 0: status = "等待领料"
    elif task.status == 1: status = "生产中"
    else : status = "生产完成"

    taskDTO = {
        "task_id": task.id,
        "person_in_charge": task.personincharge,
        "workshop_id": task.workshop.id,
        "workshop_name": task.workshop.name,
        "order_id": task.order.id,
        "topic": task.topic,
        "status": task.status,
        "amount": task.number,
        "archive_date": task.archivedate,
        "deadline": task.deadline,
        "begin_date": task.begindate,
        "material_getter": task.material_getter,
        "material_checker": task.material_checker,
        "material_distribute_date": task.material_distributon_date,
        "done_url": "http://localhost:8000/product/task/done/{}".format(task.workshop.id), # TODO: get server address
        "update_getmaterial_url": "http://localhost:8000/product/task/material-allocated/{}".format(task.workshop.id)
    }
    return taskDTO

