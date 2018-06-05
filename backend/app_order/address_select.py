from django.shortcuts import render
from django.http import JsonResponse
import codecs
import json

# Create your views here.


def getCity(req):
    req_str = req.body.decode('utf-8')
    print(req_str)
    req_json = json.loads(req_str)
    province_id = req_json['province_id']
    path = "F:/Enterprise/teamworkSpace/enterprise/enterprise/backend/app_order/area.json"
    with open(path, 'rb')as f:
        temp = json.loads(f.read().decode('utf-8'))
    for province in temp:
        if(province['code'] == province_id):            
            citys = province['children']
            return JsonResponse(citys, safe=False)

def getDistrict(req):
    req_str = req.body.decode('utf-8')
    req_json = json.loads(req_str)
    province_id = req_json['province_id']
    city_id = req_json['city_id']
    path = "F:/Enterprise/teamworkSpace/enterprise/enterprise/backend/app_order/area.json"
    with open(path, 'rb')as f:
        temp = json.loads(f.read().decode('utf-8'))
    for province in temp:
        if(province['code'] == province_id):
            citys = province['children']
            for city in citys:
                if(city['code'] == city_id):
                    district = city['children']
                    return JsonResponse(district, safe=False)
        
    