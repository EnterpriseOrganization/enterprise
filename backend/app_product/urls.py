from django.conf.urls import url
from django.urls import path
from app_product.Views import ProduceTaskView

urlpatterns = [
    # GET
    path('tasks', ProduceTaskView.getAllTasks),
    path('tasks/byorder/<order_id>', ProduceTaskView.getOrderTasks),
    path('tasks/history', ProduceTaskView.getHistoryTasks),
    path('tasks/undone', ProduceTaskView.getUndoneTasks),
    # POST
    path('task/done/<task_id>', ProduceTaskView.updateTaskDone), # POST nothing like /task/undone
    path('task/material-allocated/<task_id>', ProduceTaskView.updateTaskMaterialGet),  # POST
    path('task/create/<order_id>', ProduceTaskView.createTasks),

    # GET
    path('workshop', ProduceTaskView.getWorkshops),
    path('workshop/<product_id>', ProduceTaskView.getWorkshopByProduct)
]