from django.http import JsonResponse
import time
from enterprise.models import InventorInformation,
from django.core import serializers
# Create your views here.
from collections import defaultdict

def getCost(req):
    
    return JsonResponse({'res':'zz'})