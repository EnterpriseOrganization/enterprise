from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^get_quotation_list', views.get_quotation_list),
	url(r'^add_quotation', views.add_quotation),
	url(r'^delete_quotation', views.delete_quotation),
	url(r'^update_quotation_price', views.update_quotation_price),
	url(r'^quotation_query', views.quotation_query),
	url(r'^add_suppler', views.add_supplier),
	url(r'^get_lack_list', views.get_lack_list),
	url(r'^add_purchase', views.add_purchase),
	url(r'^delete_purchases', views.delete_purchases),
	url(r'^get_purchase_list', views.get_purchase_list),
	url(r'^get_purchase_detail', views.get_purchase_detail),
	url(r'^purchase_query', views.purchase_query),
]