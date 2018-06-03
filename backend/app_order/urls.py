from django.conf.urls import url
from . import views
from . import address_select
from . import product_select

urlpatterns = [
    url(r'^province$', address_select.getCity),
    url(r'^city$', address_select.getDistrict),
    url(r'^product$', product_select.getProductInfo),
    #url(r'^getallorder$', views.GetAllOrder), # 鑾峰彇鍒版墍鏈夌殑璁㈠崟淇℃伅锛岃繑鍥瀓son
    #url(r'^addorder',views.AddOrder), # 娣诲姞涓�潯璁㈠崟鐨勪俊鎭�
]
