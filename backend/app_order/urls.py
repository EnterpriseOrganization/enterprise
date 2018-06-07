from django.conf.urls import url
from . import views
from . import address_select
from . import product_select
from . import page_open

urlpatterns = [
    #Product表
    url(r'^get-all-product$',views.getAllProduct),#获取所有的货品信息

	# Order表
    url(r'^test$', views.testExample), # 测试用的url
    url(r'^get-all-order$', views.getAllOrder), # 获取到所有的订单信息，通过url访问，返回json文件
    url(r'^add-order$',views.addOrder), # 添加一条订单的信息，通过post发送json，接收后将该订单信息插入到模型中，返回一条状态语句
    url(r'^delete-order$',views.deleteOrder), # 删除一条订单的信息，通过post发送json，解析id删除相应的order信息，返回一条状态语句
    url(r'^update-order$',views.updateOrder), # 更新一条订单的信息，通过post发送json，解析id删除相应的order信息，再添加相应信息，返回一条状态语句
    url(r'^get-specific-order$',views.getSpecificOrder), # 查询特定具体的订单信息，通过post发送json，获取到条件后查询到相应的订单信息返回
    # OrderProduct表，这个功能主要用来显示订单的明细
    url(r'^get-all-order-product$',views.getAllOrderProduct),# 获取所有的订单货品信息
    url(r'^add-order-product$',views.addOrderProduct), # 添加订单的货品信息，通过post发送json，接受订单的所有货品信息，返回一条状态语句
    url(r'^show-all-order-product$', views.showOrderProduct), #后端返回一个订单的所有产品函数 ,接收一个json文件，获取到订单的id，显示出该订单中所有的产品
    url(r'^delete-order-product$', views.deleteOrderProduct), # 删除一个订单的某个产品
    url(r'^update-order-product$', views.updateOrderProduct),  # # 后端修改一个订单所订购的产品数量
    
    # 前端额外所需
    url(r'^province$', address_select.getCity),#获取二级下拉框-城市信息
    url(r'^city$', address_select.getDistrict),#获取三级下拉框-地区信息
    url(r'^product$', product_select.getProductInfo),#获取下拉框-产品信息
    url(r'^add$',page_open.orderAdd),#弹出子页面iframe-orderadd页面
    url(r'^list$',page_open.orderList),#弹出子页面iframe-ordermodify页面
]


