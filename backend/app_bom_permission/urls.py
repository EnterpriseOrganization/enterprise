
from django.conf.urls import url,include
from django.contrib import admin
import app_bom_permission.views as bom_view

urlpatterns = [
    url(r'^material/$', bom_view.MaterialProcessor.process_material),
    url(r'^material/([0-9]*)/$', bom_view.MaterialProcessor.process_specific_material),
    url(r'^product/$', bom_view.ProductProcessor.process_product),
    url(r'^product/([0-9]*)/$', bom_view.ProductProcessor.process_specific_product),
    url(r'^materialclass/$', bom_view.MaterialClassProcessor.get),
    url(r'^productclass/$', bom_view.ProductClassProcessor.get),
]