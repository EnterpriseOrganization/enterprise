from django.conf.urls import url
from . import views_warehouse
urlpatterns = [
    url(r'^new-inventory',views_warehouse.addInventory),
    url(r'^inventory$',views_warehouse.getInventory),
    url(r'^remove-record',views_warehouse.removeRecord),
    url(r'^modify-inventory',views_warehouse.modifyInventory)
]