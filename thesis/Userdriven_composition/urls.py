from . import views
from .views import ActuatorListApiView
from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('actuators', views.ActuatorApi)
router.register('lowersensors', views.LowerSensorApi)
router.register('serviceregistry', views.ServiceRegistryApi)

urlpatterns = [
    # url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$',views.notice_detail, name ='notice_detail')
    path('',views.home, name = 'home_url'),
    path('api/',include(router.urls)),
	path('getMotorStatus/',views.getMotorStatus, name='status'),
	path('actuators/', ActuatorListApiView.as_view(),name="actuator_filter"),
# 	url(r'^dig/',views.LowerSensorAPI.as_view()),
]