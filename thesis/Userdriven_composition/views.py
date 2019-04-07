from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter)
from .serializers import *
from .models import *
from .data_processing_library1 import *

from django.db.models import Q
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
    all_service = requests.get("http://192.168.1.137:8000/api/serviceregistry/").json()
    #print(all_service)
    last_service = all_service[-1]

    print(last_service['id'])
    read_file = open('last-id.txt','r')
    a = read_file.read()
    read_file.close()
    name_id = last_service['name']
    sensor_tag = name_id
    name_id = name_id.replace(".","_")

    print(a)
    if int(a) < last_service['id']:
        print('a')
        write_file = open('last-id.txt','w+')
        write_file.write(str(last_service['id']))
        write_file.close()
        if last_service['service_type'] == 'sensor':
            automatic_writter.sensor_function_writter(name_id,sensor_tag)
            BlockGenerator.BlockGenerator(name_id,last_service['service_type'])
        elif last_service['service_type'] == 'actuator':
            automatic_writter.actuator_function_writter(name_id,sensor_tag)
            BlockGenerator.BlockGenerator(name_id,last_service['service_type'])

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



class ActuatorListApiView(generics.ListAPIView):
    serializer_class= ActuatorSerializer

    def get_queryset(self):
        qs=Actuator.objects.all()
        query = self.request.GET.get("q")

        if query is not None:
            qs= qs.filter(
                Q(topic__icontains=query)
                ).distinct()
        
        return qs


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