from django.conf.urls import url
from . import views
urlpatterns = [
	# Order表
    url(r'^test$', views.testExample), # 测试用的url
    url(r'^getallorder$', views.GetAllOrder), # 获取到所有的订单信息，通过url访问，返回json文件
    url(r'^addorder',views.AddOrder), # 添加一条订单的信息，通过post发送json，接收后将该订单信息插入到模型中，返回一条状态语句
    url(r'^deleteorder',views.DeleteOrder), # 删除一条订单的信息，通过post发送json，解析id删除相应的order信息，返回一条状态语句
    url(r'^updateorder',views.UpdateOrder), # 更新一条订单的信息，通过post发送json，解析id删除相应的order信息，再添加相应信息，返回一条状态语句
    
    # OrderProduct表，这个功能主要用来显示订单的明细
    url(r'^showallorderproduct', views.ShowOrderProduct) #后端返回一个订单的所有产品函数 ,接收一个json文件，获取到订单的id，显示出该订单中所有的产品
    url(r'^deleteorderproduct', views.DeleteOrderProduct)  # 删除一个订单的某个产品
]
