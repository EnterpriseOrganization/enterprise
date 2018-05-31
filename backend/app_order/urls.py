from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^test$', views.testExample), # 测试用的url
    url(r'^getallorder$', views.GetAllOrder), # 获取到所有的订单信息，返回json
    url(r'^addorder',views.AddOrder), # 添加一条订单的信息
]
