from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^test$', views.testExample),
    url(r'^getallorder$', views.GetAllOrder),
]