from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getProductInfo(req):
    context = [
            {            
                'name' : 'luosi',
                'price' : '2.5'
            },
            {
                'name' : 'LUOMU',
                'price' : '3.5'
            
            }
    ]
    return JsonResponse(context, safe=False)