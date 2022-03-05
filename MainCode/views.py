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
    ob = BusStop.objects.all()
    if request.method == "POST":
        stop = request.POST['stop']
        time = request.POST['time']
        # obb = Bus
        print(stop)
    return render(request, "AddBusTime.html", {'data': ob})


def busmanagement(request):
    BusReg = BusRegister.objects.all()
    return render(request, "busManagement.html", {"busreg": BusReg})


def updatebus(request, id):
    BusReg = BusRegister.objects.all()
    busdetail = BusRegister.objects.get(BusRegisterNUmber=id)
    print(BusReg)
    return render(request, "BusManagement-add.html",)


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
    BusReg = Route.objects.all()
    if request.method == "POST":
        RegisterNUmber = request.POST['register_number']
        NumberOfSeats = request.POST['NumberOfSeats']
        route = request.POST['route']
        print(route)
        obb = Route.objects.get(RouteId=route)
        ob = BusRegister()
        ob.BusRegisterNUmber = RegisterNUmber
        ob.SeatCapacity = NumberOfSeats
        ob.RouteId = obb
        ob.save()
        return redirect("/busmanagement")
    return render(request, "BusManagement-add.html", {"route": BusReg})


def bustime(request):
    if request.method == "POST":
        BusName = request.POST['busname']
        print(BusName)
    BusData = Bustime.objects.all()
    # busTmeData = Bustime.objects.get(StopId = BusName)
    return render(request, "BusTime.html", {'busdetails': BusData})


def AddStop(request):
    ob = BusRegister.objects.all()
    if request.method == "POST":
        route = request.POST['Bus']
        Stop = request.POST['Stop']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        TicketCharge = request.POST['TicketCharge']
        obb = Route.objects.get(StartingStop=route)
        BusStop.objects.create(stop=Stop, Latitude=Latitude, Longitude=Longitude,
                               TicketCharge=TicketCharge, RouteId=obb)
        return redirect("/stopdetails")
    return render(request, "AddStop.html", {'busregisters': ob})


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
    if request.method == "POST":
        Bus = request.POST['busnumber']
        # id = BusStop.objects.get(RouteId=Bus)
        obb = BusRegister.objects.get(BusRegisterNUmber=Bus)
        # print(obb.RouteId.RouteId.Stop)
    return render(request, "stopdetails.html",
                  {'busregister': ob},
                  #  {'obb': obb}
                  )


def searchticket(request):
    ob = BusRegister.objects.all()
    if request.method == "POST":
        Bus = request.POST['busnumber']
        obb = BusRegister.objects.get(BusRegisterNUmber=Bus)
        obbs = BusStop.objects.filter(RouteId=obb.RouteId)
        print(Bus)
    return render(request, "stopdetails.html",
                  {'busregister': ob, "stop": obbs})


def track(request):
    obj = BusRegister.objects.all()
    if request.method == "POST":
        BusNumber = request.POST['BusNumber']
        ob = BusRegister.objects.get(BusRegisterNUmber=BusNumber)
        busstop = BusStop.objects.get(RouteId=ob.RouteId)
        # return redirect("https://www.google.com/maps?q={busstop.Latitude},{busstop.Longitude}")
        # return redirect("https://www.google.com/maps?q=37.819722,-122.478611")
        return redirect("/map")        
    else:
        pass
    return render(request, "track.html", {
        'busregisters': obj,
    })


def mapview(request):
    return render(request, "map.html")


# https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.7330220952845!2d-122.48079968468095!3d37.8197219797513!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x67540215e3e68cf0!2zMzfCsDQ5JzExLjAiTiAxMjLCsDI4JzQzLjAiVw!5e0!3m2!1sen!2sin!4v1646504378420!5m2!1sen!2sin" 
# 37.819722,-122.478611