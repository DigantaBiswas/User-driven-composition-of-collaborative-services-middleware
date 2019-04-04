from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter)
from .serializers import *
from .models import *
from .data_processing_library1 import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
import requests
from . import automatic_writter
from . import BlockGenerator

from rest_framework.response import Response


# Create your views here.
def home(request):
    action_motor("0")
    get_lowersensor()
    all_service = requests.get("http://127.0.0.1:8000/api/serviceregistry/").json()
    #print(all_service)
    last_service = all_service[-1]

    print(last_service['id'])
    read_file = open('last-id.txt','r')
    a = read_file.read()
    read_file.close()

    print(a)
    if int(a) < last_service['id']:
        print('a')
        write_file = open('last-id.txt','w+')
        write_file.write(str(last_service['id']))
        write_file.close()
        if last_service['service_type'] == 'sensor':
            automatic_writter.sensor_function_writter(last_service['name_id'], last_service['api_link'])
            BlockGenerator.BlockGenerator(last_service['name_id'],last_service['service_type'])
        elif last_service['service_type'] == 'actuator':
            automatic_writter.actuator_function_writter(last_service['name_id'], last_service['api_link'])
            BlockGenerator.BlockGenerator(last_service['name_id'],last_service['service_type'])

    return render(request, 'index.html')
	

class ActuatorApi(viewsets.ModelViewSet):
	queryset = Actuator.objects.all()
	serializer_class = ActuatorSerializer

class LowerSensorApi(viewsets.ModelViewSet):
	queryset = LowerSensor.objects.all()
	serializer_class = LowerSensorSerializer




class ServiceRegistryApi(viewsets.ModelViewSet):
    queryset = Service_registry.objects.all()
    serializer_class = ServiceRegistrySerializer






def getMotorStatus(request):
    #csrfContext = RequestContext(code)
    if request.is_ajax():
        code = request.POST['code']
        #function_call = request.POST['function_call']
        #motor_status = get_action_motor_status(function_call)
        print(code)
        exec(code)
    else:
        return HttpResponse('Use ajax format!')

    return JsonResponse({'code': code })