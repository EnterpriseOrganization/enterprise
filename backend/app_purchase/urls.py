from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello/', views.hello),
	url(r'^history_list/', views.history_list),
]