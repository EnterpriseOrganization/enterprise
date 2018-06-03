
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
]