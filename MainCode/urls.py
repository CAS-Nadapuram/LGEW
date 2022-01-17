from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('adminhome', views.adminhome),
    path('addbustime', views.AddBusTime),
    path('busmanagement', views.busmanagement),
    path('addconductor', views.addconductor),
    path('busmanagement_add', views.busmanagement_add),
    path('bustime', views.bustime),
    path('addstop', views.AddStop),
    path('conductor', views.conductor),
    path('feedback', views.feedback),
    path('login', views.main),
    path('passenger', views.passenger),
    path('route', views.Route),
    path('routeadd', views.RouteAdd),
    path('stopdetails', views.stopdetails),
    path('track', views.track),
]