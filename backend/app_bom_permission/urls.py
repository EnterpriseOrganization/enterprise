
from django.conf.urls import url,include
from django.contrib import admin
import app_bom_permission.views as bom_view

urlpatterns = [
    url(r'^material/$', bom_view.MaterialProcessor.process_material),
    url(r'^material/([0-9]*)/$', bom_view.MaterialProcessor.process_specific_material)
]