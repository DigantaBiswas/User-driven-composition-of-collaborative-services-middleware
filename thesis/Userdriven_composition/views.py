from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from .data_processing_library1 import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
	action_motor("0")
	get_lowersensor()
	return render(request, 'index.html')
	

class ActuatorApi(viewsets.ModelViewSet):
	queryset = Actuator.objects.all()
	serializer_class = ActuatorSerializer

class LowerSensorApi(viewsets.ModelViewSet):
	queryset = LowerSensor.objects.all()
	serializer_class = LowerSensorSerializer






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