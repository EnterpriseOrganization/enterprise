"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^cost/', include('app_cost_warehouse.urls',namespace = "app_cost_warehouse")),
    # url(r'^warehouse/',include('app_cost_warehouse.urls',namespace = "app_cost_warehouse")),
    # url(r'^order/',include('app_order.urls',namespace = "app_order")),
    # url(r'^product/',include('app_product.urls',namespace = "app_product")),
    # url(r'^purchase/',include('app_purchase.urls',namespace = "app_purchase")),
    url(r'^login/',include('app_bom_permission.urls',namespace = "app_bom_permission")),
    # url(r'^permission/',include('app_bom_permission.urls',namespace = "app_bom_permission")),
]
