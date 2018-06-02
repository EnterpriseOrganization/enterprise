from django.conf.urls import url
from . import views
from . import address_select
from . import product_select

urlpatterns = [
    url(r'^province$', address_select.getCity),
    url(r'^city$', address_select.getDistrict),
    url(r'^product$', product_select.getProductInfo),
    url(r'^test$', views.testExample), # 测试用的url
    url(r'^getallorder$', views.GetAllOrder), # 获取到所有的订单信息，返回json
    url(r'^addorder',views.AddOrder), # 添加一条订单的信息
]
