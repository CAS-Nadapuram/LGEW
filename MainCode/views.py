from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import *


def main(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']
        user = Login.objects.filter(Username=Username, Password=Password)
        if len(user) == 0:
            messages.error(request, "invalid user")
            return redirect("/")
        else:
            return redirect("/adminhome")
    else:
        pass
    return render(request, "login.html")


def adminhome(request):
    return render(request, "AdminHome.html")


def AddBusTime(request):
    return render(request, "AddBusTime.html")


def busmanagement(request):
    return render(request, "busManagement.html")


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
        ob=Login.objects.create(Username = Username, Password = Password, Type="conductor")
        bob=BusRegister.objects.get(BusId=Bus)
        Conductor.objects.create(
            FirstName=FirstName, LastName=LastName, Place=Place,
            Post=Post, pin=Pin, Bus=bob, Contact=Contact,lid=ob
        )
    ob=BusRegister.objects.all()
    return render(request, "AddConductor.html",{"data":ob})



def deleteconductor(request,id):
    obc=Conductor.objects.get(UserId=id)
    lob=Login.objects.get(UserId=obc.lid.UserId)
   
    obc.delete()
    lob.delete()
    return redirect('/conductor')

def deleteroute(request,id):
    obc = Route.objects.get(RouteId=id)
    obc.delete()
    return redirect("/route")
def busmanagement_add(request):
    if request.method == "POST":
        RegisterNUmber = request.POST['register_number']
        Route = request.POST['route']
        NumberOfSeats = request.POST['NumberOfSeats']
        print(
            "register number = ", RegisterNUmber,
            "\n Route = ",  Route,
            "\n number of seats = ", NumberOfSeats
        )

    return render(request, "BusManagement-add.html")


def bustime(request):
    return render(request, "BusTime.html")


def AddStop(request):
    if request.method == "POST":
        Bus = request.POST['Bus']
        Stop = request.POST['Stop']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        TicketCharge = request.POST['TicketCharge']
        print("\n Bus = ", Bus,
              "\n stop = ", Stop,
              "\n Latitude = ", Latitude,
              "\n longitude = ", Longitude,
              "\n Ticket charge = ", TicketCharge,
              )
    return render(request, "AddStop.html")


def conductor(request):
    object = Conductor.objects.all()
    return render(request, "conductor.html", {"data": object})


def feedback(request):
    feedback = Feedback.objects.all()
    # print(feedback.User_id)
    return render(request, "feedback.html", {'feedbacks': feedback})


# def login1(request):
#     return render(request, "login.html")


def passenger(request):
    return render(request, "passenger.html")


def Routee(request):
    ob=Route.objects.all()
    return render(request, "Route.html",{"data":ob})


def RouteAdd(request):
    if request.method == "POST":
        StartingStop = request.POST['StartingStop']
        EndingStop = request.POST['EndingStop']
        rob=Route()
        rob.StartingStop=StartingStop
        rob.EndingStop=EndingStop
        rob.save()
        return redirect('/route')
       
    return render(request, "RouteAdd.html")


def stopdetails(request):
    return render(request, "stopdetails.html")


def track(request):
    if request.method == "POST":
        BusNumber = request.POST['BusNumber']
        print(BusNumber)
    else:
        pass
    return render(request, "track.html")
