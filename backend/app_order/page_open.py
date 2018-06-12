from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def orderList(req):
    with open('F:/Enterprise/teamworkSpace/enterprise/frontend/WeAdmin/pages/order/OrderList.html', 'rb') as f:
        html = f.read()
    return HttpResopense(html)

def orderAdd(req):
    with open('F:/Enterprise/teamworkSpace/enterprise/frontend/WeAdmin/pages/order/OrderAdd.html', 'rb') as f:
        html = f.read()
    return HttpResopense(html)