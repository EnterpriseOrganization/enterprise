from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello/', views.hello),
	url(r'^get_quotation_list/', views.get_quotation_list),
]