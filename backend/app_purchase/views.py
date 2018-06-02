from django.shortcuts import render
from django.http import JsonResponse
import json


def hello(request):
	res = {'title':'hello', 'content':'test'}
	return JsonResponse(res)



def history_list(request):
	print(request.body)
	return JsonResponse({})
