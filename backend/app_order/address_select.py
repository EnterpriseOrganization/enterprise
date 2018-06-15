# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
import codecs
import json
import os
# Create your views here.
def getCity(req):
    current_path = os.getcwd()
    req_str = req.body.decode('utf-8')
    req_json = json.loads(req_str)
    print(req_json)
    province_id = req_json['province_id']
    path = current_path + "\\app_order\\area.json"
    with open(path, 'rb')as f:
        temp = json.loads(f.read().decode('utf-8'))
    for province in temp:
        if(province['code'] == province_id):            
            citys = province['children']
            return JsonResponse(citys, safe=False)

def getDistrict(req):
    current_path = os.getcwd()
    req_str = req.body.decode('utf-8')
    req_json = json.loads(req_str)
    province_id = req_json['province_id']
    city_id = req_json['city_id']
    path = current_path + "\\app_order\\area.json"
    with open(path, 'rb')as f:
        temp = json.loads(f.read().decode('utf-8'))
    for province in temp:
        if(province['code'] == province_id):
            citys = province['children']
            for city in citys:
                if(city['code'] == city_id):
                    district = city['children']
                    return JsonResponse(district, safe=False)
        
    