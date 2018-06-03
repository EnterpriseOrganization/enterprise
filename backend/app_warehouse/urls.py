from django.conf.urls import url
from . import views_warehouse
urlpatterns = [
	url(r'^get-inventor$',views_warehouse.getInventory),
        url(r'^new-inventory',views_warehouse.addInventory),
]