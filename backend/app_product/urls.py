from django.conf.urls import url
from app_product.Views import ProduceTaskView, MaterialListView


urlpatterns = [
    url(r'tasks$', ProduceTaskView.getAllTasks),
    url(r'tasks/real$', ProduceTaskView.getRealAllTasks),
    url(r'tasks/byorder$', ProduceTaskView.getOrderTasks),
    url(r'tasks/byworkshop$', ProduceTaskView.getWorkshopTasks),
    url(r'tasks/history$', ProduceTaskView.getHistoryTasks),
    url(r'tasks/undone$', ProduceTaskView.getUndoneTasks),
    url(r'task/create$', ProduceTaskView.createTasks),
    url(r'task/material-allocated$', ProduceTaskView.updateTaskMaterialGet),
    url(r'task/done$', ProduceTaskView.updateTaskDone),
    url(r'task/material-list$', MaterialListView.getMaterialList),
    url(r'workshop$', ProduceTaskView.getWorkshops),
    url(r'workshop/byproduct$', ProduceTaskView.getWorkshopByProduct),
]