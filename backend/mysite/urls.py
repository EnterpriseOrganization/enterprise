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
from django.conf.urls import url, include
from django.contrib import admin
from app_product.Views import ProduceTaskView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cost/', include('app_cost.urls')),
    url(r'^warehouse/', include('app_warehouse.urls')),
    url(r'^order/', include('app_order.urls')),
    url(r'^product/', include('app_product.urls')),
    url(r'^purchase/', include('app_purchase.urls')),
    url(r'^bom/', include('app_bom_permission.urls')),
    url(r'^user/', include('app_bom_permission.urls')),
]
