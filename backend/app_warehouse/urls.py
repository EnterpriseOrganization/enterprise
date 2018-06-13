from django.conf.urls import url
from . import views_warehouse
urlpatterns = [
    url(r'^new-inventory',views_warehouse.addInventory),
    url(r'^inventory$',views_warehouse.getInventory),
    url(r'^remove-record',views_warehouse.removeRecord),
    url(r'^modify-inventory',views_warehouse.modifyInventory),
    url(r'^get-inwarehouse-record',views_warehouse.getInWarehouseRecord),
    url(r'^get-outwarehouse-record',views_warehouse.getOutWarehouseRecord),
]