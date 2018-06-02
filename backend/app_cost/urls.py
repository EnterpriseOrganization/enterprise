from django.conf.urls import url
from . import views_cost
urlpatterns = [
    url(r'^get-cost',views_cost.getCost),
]