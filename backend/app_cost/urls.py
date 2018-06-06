from django.conf.urls import url
from . import views_cost
urlpatterns = [
	url(r'^get-all-cost$',views_cost.getAllCost),
	url(r'^new-product$',views_cost.newProduct),
	url(r'^get-cost-by-name$',views_cost.getCostByName)
]