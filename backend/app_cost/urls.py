from django.conf.urls import url
from . import views_cost
urlpatterns = [
	url(r'^getAllCost$',views_cost.getAllCost),
	url(r'^newProduct$',views_cost.newProduct),
	url(r'^getCostByName$',views_cost.getCostByName)
]