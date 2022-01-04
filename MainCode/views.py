from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def main(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username = Username , password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect("/adminhome")
        else:
             messages.error(request, "invalid user")
             print(messages)
             return redirect("/")
        
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
    
    
    return render(request, "AddConductor.html")


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
    return render(request, "conductor.html")


def feedback(request):
    return render(request, "feedback.html")


def login(request):
    return render(request, "login.html")


def passenger(request):
    return render(request, "passenger.html")


def Route(request):
    return render(request, "Route.html")


def RouteAdd(request):
    if request.method == "GET":
        StartingStop = request.GET['StartingStop']
        EndingStop = request.GET['EndingStop']
        print(
            "\n Starting stop = ", StartingStop,
            "\n Ending stop = ", EndingStop,
        )
    return render(request, "RouteAdd.html")


def stopdetails(request):
    return render(request, "stopdetails.html")


def track(request):
    return render(request, "track.html")