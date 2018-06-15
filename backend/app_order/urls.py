
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from . import address_select
from . import product_select
from . import page_open

urlpatterns = [
    #Product��
    url(r'^get-all-product$',views.getAllProduct),#��ȡ���еĻ�Ʒ��Ϣ

	# Order��
    url(r'^test$', views.testExample), # �����õ�url
    url(r'^get-all-order$', views.getAllOrder), # ��ȡ�����еĶ�����Ϣ��ͨ��url���ʣ�����json�ļ�
    url(r'^add-order$',views.addOrder), # ���һ����������Ϣ��ͨ��post����json�����պ󽫸ö�����Ϣ���뵽ģ���У�����һ��״̬���
    url(r'^delete-order$',views.deleteOrder), # ɾ��һ����������Ϣ��ͨ��post����json������idɾ����Ӧ��order��Ϣ������һ��״̬���
    url(r'^update-order$',views.updateOrder), # ����һ����������Ϣ��ͨ��post����json������idɾ����Ӧ��order��Ϣ���������Ӧ��Ϣ������һ��״̬���
    url(r'^get-specific-order$',views.getSpecificOrder), # ��ѯ�ض�����Ķ�����Ϣ��ͨ��post����json����ȡ���������ѯ����Ӧ�Ķ�����Ϣ����
    url(r'^get-order-detail$',views.getOrderDetail), # ��ѯ��������Ϣ�������ض�������Ϣ�Լ���Ʒ����Ϣ
    url(r'^update-order-detail$',views.updateOrderDetail), # ���µ�������Ϣ�����³ɹ����
    url(r'^update-one-order$',views.updateOneOrder), # ���µ�����Ϣ��״̬��0��1,1��0
    url(r'^complete-orders$',views.completeOrders), # ��ѡ��Ķ�����Ϣȫ����Ϊ���
    url(r'^delete-orders$',views.deleteOrders), # ��ѡ��Ķ���ȫ��ɾ��
    # OrderProduct�����������Ҫ������ʾ��������ϸ
    url(r'^get-all-order-product$',views.getAllOrderProduct),# ��ȡ���еĶ�����Ʒ��Ϣ
    url(r'^add-order-product$',views.addOrderProduct), # ��Ӷ����Ļ�Ʒ��Ϣ��ͨ��post����json�����ܶ��������л�Ʒ��Ϣ������һ��״̬���
    url(r'^show-all-order-product$', views.showOrderProduct), #��˷���һ�����������в�Ʒ���� ,����һ��json�ļ�����ȡ��������id����ʾ���ö��������еĲ�Ʒ
    url(r'^delete-order-product$', views.deleteOrderProduct), # ɾ��һ��������ĳ����Ʒ
    url(r'^update-order-product$', views.updateOrderProduct),  # # ����޸�һ�������������Ĳ�Ʒ����
    
    # ǰ�˶�������
    url(r'^province$', address_select.getCity),#��ȡ����������-������Ϣ
    url(r'^city$', address_select.getDistrict),#��ȡ����������-������Ϣ
    url(r'^product$', product_select.getProductInfo),#��ȡ������-��Ʒ��Ϣ
    url(r'^add$',page_open.orderAdd),#������ҳ��iframe-orderaddҳ��
    url(r'^list$',page_open.orderList),#������ҳ��iframe-ordermodifyҳ��
]


