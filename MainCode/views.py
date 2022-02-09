from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import *


def main(request):
    global Username
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']
        user = Login.objects.filter(
            Username=Username, Password=Password, Type="admin")
        if len(user) == 0:
            messages.error(request, "invalid user")
            return redirect("/")
        else:
            return redirect("/adminhome")
    else:
        pass
    return render(request, "login.html")


def adminhome(request):
    return render(request, "AdminHome.html", 
    # {"user": Username}
    )


def AddBusTime(request):
    return render(request, "AddBusTime.html")


def busmanagement(request):
    BusReg = BusRegister.objects.all()
    return render(request, "busManagement.html", {"busreg": BusReg})


def updatebus(request, id):
    BusReg = BusRegister.objects.all()
    busdetail = BusRegister.objects.get(BusRegisterNUmber=id)
    print(BusReg)
    # return render(request, "BusManagement-add.html", {'busdetails' : busdetail,'route' : BusReg})


def addconductor(request):
    if request.method == "POST":
        FirstName = request.POST['firstname']
        LastName = request.POST['lastname']
        Place = request.POST['place']
        Post = request.POST['post']
        Contact = request.POST['contact']
        Pin = request.POST['pin']
        Bus = request.POST['bus']
        Username = request.POST['username']
        Password = request.POST['password']
        ob = Login.objects.create(
            Username=Username, Password=Password, Type="conductor")
        bob = BusRegister.objects.get(BusId=Bus)
        Conductor.objects.create(
            FirstName=FirstName, LastName=LastName, Place=Place,
            Post=Post, pin=Pin, Bus=bob, Contact=Contact, lid=ob
        )
        return redirect('/conductor')
    ob = BusRegister.objects.all()
    return render(request, "AddConductor.html", {"data": ob})


def deleteconductor(request, id):
    obc = Conductor.objects.get(UserId=id)
    lob = Login.objects.get(UserId=obc.lid.UserId)
    obc.delete()
    lob.delete()
    return redirect('/conductor')


def deleteroute(request, id):
    obc = Route.objects.get(RouteId=id)
    obc.delete()
    return redirect("/route")


def busmanagement_add(request,):
    BusReg = BusRegister.objects.all()
    if request.method == "POST":
        RegisterNUmber = request.POST['register_number']
        NumberOfSeats = request.POST['NumberOfSeats']
        StartingStop = request.POST['StartingStop']
        EndingStop = request.POST['endingstop']
        route = Route.objects.create(
            StartingStop=StartingStop, EndingStop=EndingStop)
        BusRegister.objects.create(
            BusRegisterNUmber=RegisterNUmber,
            SeatCapacity=NumberOfSeats,
            route=route
        )
        redirect("//busmanagement")
    return render(request, "BusManagement-add.html", {"route": BusReg})


def bustime(request):
    return render(request, "BusTime.html")


def AddStop(request):
    ob = BusRegister.objects.all()
    if request.method == "POST":
        Bus = request.POST['Bus']
        Stop = request.POST['Stop']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        TicketCharge = request.POST['TicketCharge']

        # routes = BusRegister.objects.get(RouteId = bus )
        # BusStop.objects.create(RouteId =  routes, stop = Stop, Latitude = Latitude, Longitude = Longitude
        # , TicketCharge = TicketCharge)
        redirect("/stopdetails")
    return render(request, "AddStop.html",{'busregisters': ob})


def conductor(request):
    object = Conductor.objects.all()
    return render(request, "conductor.html", {"data": object})


def deletebus(request, id):
    busdetail = BusRegister.objects.get(BusRegisterNUmber=id)
    busdetail.delete()
    return redirect('/busmanagement')


def feedback(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback.html", {'feedbacks': feedback})


def passenger(request):
    return render(request, "passenger.html")


def Routee(request):
    ob = Route.objects.all()
    return render(request, "Route.html", {"data": ob})


def RouteAdd(request):
    if request.method == "POST":
        StartingStop = request.POST['StartingStop']
        EndingStop = request.POST['EndingStop']
        rob = Route()
        rob.StartingStop = StartingStop
        rob.EndingStop = EndingStop
        rob.save()
        return redirect('/route')

    return render(request, "RouteAdd.html")


    
def stopdetailz(request):
    ob = BusRegister.objects.all()
    print(ob)
    if request.method == "POST":
               Bus = request.POST['busnumber']
               id = BusRegister.objects.get(BusRegisterNUmber = Bus )
               busdata = BusStop.objects.filter(RouteId = id.RouteId)
               print(busdata)
    return render(request, "stopdetails.html",{'busregister' : ob})


def track(request):
    if request.method == "POST":
        BusNumber = request.POST['BusNumber']
        print(BusNumber)
    else:
        pass
    return render(request, "track.html")
