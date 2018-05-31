from django.conf.urls import url
from app_product.Views import ProduceTaskView, MaterialListView


urlpatterns = [
    url(r'task/material-list', MaterialListView.getMaterialList),
]