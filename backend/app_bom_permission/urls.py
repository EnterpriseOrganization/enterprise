
from django.conf.urls import url,include
from django.contrib import admin
import app_bom_permission.views as bom_view

urlpatterns = [
    url(r'^material/$', bom_view.MaterialProcessor.processMaterial),
    url(r'^material/([0-9]*)/$', bom_view.MaterialProcessor.processSpecificMaterial),
    url(r'^product/$', bom_view.ProductProcessor.processProduct),
    url(r'^product/([0-9]*)/$', bom_view.ProductProcessor.processSpecificProduct),
    url(r'^materialclass/$', bom_view.MaterialClassProcessor.get),
    url(r'^productclass/$', bom_view.ProductClassProcessor.get),
    url(r'^productmaterial/product/[0-9]*/$', bom_view.ProductmaterialProcessor.processProductmaterialForCertainProduct), # get 
    url(r'^procuctmaterial/$', bom_view.ProductmaterialProcessor.processProductmaterial), # delete 批量删除 create
    url(r'^productmaterial/[0-9]*/$', bom_view.ProductmaterialProcessor.processSpecificProductmaterial), # (get) <- 可能不需要  put delete
]