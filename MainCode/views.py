from django.shortcuts import render


def main(request):
    return render(request,"login.html")

def adminhome(request):
    return render(request,"AdminHome.html")

def AddBusTime(request):
    return render(request,"AddBusTime.html")

def busmanagement(request):
    return render(request,"busManagement.html")

def addconductor(request):
    return render(request,"AddContuctor.html")

def busmanagement_add(request):
    return render(request,"Busmanagement-add.html")

def bustime(request):
    return render(request,"BusTime.html")

def AddStop(request):
    return render(request,"AddStop.html")

def conductor(request):
    return render(request,"conductor.html")

def feedback(request):
    return render(request,"feedback.html")

def login(request):
    return render(request,"login.html")

def passenger(request):
    return render(request,"passenger.html")

def Route(request):
    return render(request,"Route.html")

def RouteAdd(request):
    return render(request,"RouteAdd.html")

def stopdetails(request):
    return render(request,"stopdetails.html")

def track(request):
    return render(request,"track.html")





















