from django.conf.urls import url
from . import views_warehouse
urlpatterns = [
	url(r'^getInventor$',views_warehouse.getInventory),
]