from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
import pyqrcode
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def logout(request):
    auth.logout(request)
    return redirect('/')


def lt(request):
    return HttpResponse('''<script>alert("please login");window.location="/"</script>''')


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
            oba = auth.authenticate(username='admin', password='admin')
            if oba is not None:
                auth.login(request, oba)
            return redirect("/adminhome")
    else:
        pass
    return render(request, "login1.html")


@login_required(login_url="/lt")
def adminhome(request):
    return render(request, "AdminHome.html",
                  # {"user": Username}
                  )


@login_required(login_url="/lt")
def AddBusTime(request):
    ob = BusRegister.objects.all()
    obs = BusStop.objects.all()
    if request.method == "POST":
        stop = request.POST['stop']
        bus = request.POST['bus']
        time = request.POST['time']
        busob = BusRegister.objects.get(BusId=bus)
        stopob = BusStop.objects.get(StopId=stop)
        obb = Bustime()
        obb.BusId = busob
        obb.StopId = stopob
        obb.Time = time
        obb.save()
        print(stop)
        return redirect('/bustimee')
    return render(request, "AddBusTime.html", {'data': ob, "bs": obs})


@login_required(login_url="/lt")
def busmanagement(request):
    BusReg = BusRegister.objects.all()
    return render(request, "busManagement.html", {"busreg": BusReg})


@login_required(login_url="/lt")
def updatebus(request, id):
    BusReg = BusRegister.objects.all()
    busdetail = BusRegister.objects.get(BusRegisterNUmber=id)
    print(BusReg)
    return render(request, "BusManagement-add.html",)


@login_required(login_url="/lt")
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


@login_required(login_url="/lt")
def deleteconductor(request, id):
    obc = Conductor.objects.get(UserId=id)
    lob = Login.objects.get(UserId=obc.lid.UserId)
    obc.delete()
    lob.delete()
    return redirect('/conductor')


@login_required(login_url="/lt")
def deleteroute(request, id):
    obc = Route.objects.get(RouteId=id)
    obc.delete()
    return redirect("/route")


@login_required(login_url="/lt")
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
        big_code = pyqrcode.create(
            str(ob.BusId), error='L', version=27, mode='binary')
        qrs = "C:/Users/00000/Desktop/LGEW-main/MainCode/static/qr_code/" + \
            str(ob.BusId) + ".png"
        big_code.png(qrs, scale=6, module_color=[
                     0, 0, 0, 128], background=[0xff, 0xff, 0xff])
        return redirect("/busmanagement")
    return render(request, "BusManagement-add.html", {"route": BusReg})


@login_required(login_url="/lt")
def bustimee(request):
    BusData = BusRegister.objects.all()
    if request.method == "POST":
        BusName = request.POST['busname']
        print(BusName)
        obbus = BusRegister.objects.get(BusId=BusName)
        ob = Bustime.objects.filter(BusId=obbus)
        return render(request, "BusTime.html", {'busdetails': BusData, "bd": ob})
    BusData = BusRegister.objects.all()
    # busTmeData = Bustime.objects.get(StopId = BusName)
    return render(request, "BusTime.html", {'busdetails': BusData})


@login_required(login_url="/lt")
def deletebustime(request, id):
    ob = Bustime.objects.get(TimeId=id)
    ob.delete()
    return redirect("/bustimee")


@login_required(login_url="/lt")
def AddStop(request):
    ob = Route.objects.all()
    if request.method == "POST":
        route = request.POST['Bus']
        Stop = request.POST['Stop']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        TicketCharge = request.POST['TicketCharge']
        obb = Route.objects.get(RouteId=route)
        BusStop.objects.create(stop=Stop, Latitude=Latitude, Longitude=Longitude,
                               TicketCharge=TicketCharge, RouteId=obb)
        return redirect("/stopdetails")
    return render(request, "AddStop.html", {'busregisters': ob})


@login_required(login_url="/lt")
def conductor(request):
    object = Conductor.objects.all()
    return render(request, "conductor.html", {"data": object})


@login_required(login_url="/lt")
def deletebus(request, id):
    busdetail = BusRegister.objects.get(BusRegisterNUmber=id)
    busdetail.delete()
    return redirect('/busmanagement')


@login_required(login_url="/lt")
def feedback(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback.html", {'feedbacks': feedback})


@login_required(login_url="/lt")
def passenger(request):
    obj = BusRegister.objects.all()
    if request.method == "POST":
        BusNumber = request.POST['BusNumber']
        ob = BusRegister.objects.get(BusRegisterNUmber=BusNumber)
        ob1 = PassengerBooking.objects.filter(
            BusId=ob.BusId).aggregate(Count('PassengerId'))
        # obb=PassengerBooking.objects.annotate(Count('PassengerId'),BusId=ob.BusId)
        # print(obb[0].PassengerId__count,"================================================================")
        # pno=ob1.PassengerId__count
        return render(request, "passenger.html", {
            'busregisters': obj, 'tno': ob1['PassengerId__count']})
    else:
        pass
    return render(request, "passenger.html", {
        'busregisters': obj,
    })


@login_required(login_url="/lt")
def Routee(request):
    ob = Route.objects.all()
    return render(request, "Route.html", {"data": ob})


@login_required(login_url="/lt")
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


@login_required(login_url="/lt")
def stopdetailz(request):
    ob = Route.objects.all()
    if request.method == "POST":
        Bus = request.POST['busnumber']
        # id = BusStop.objects.get(RouteId=Bus)
        obb = BusRegister.objects.get(BusRegisterNUmber=Bus)
        # print(obb.RouteId.RouteId.Stop)
    return render(request, "stopdetails.html",
                  {'busregister': ob},
                  #  {'obb': obb}
                  )


@login_required(login_url="/lt")
def searchticket(request):
    ob = Route.objects.all()
    if request.method == "POST":
        Bus = request.POST['busnumber']
        obb = Route.objects.get(RouteId=Bus)
        obbs = BusStop.objects.filter(RouteId=obb.RouteId)
        print(Bus)
        return render(request, "stopdetails.html",
                      {'busregister': ob, "stop": obbs})
    return render(request, "stopdetails.html",
                  {'busregister': ob})


@login_required(login_url="/lt")
def deletestop(request, id):
    ob = BusStop.objects.get(StopId=id)
    ob.delete()
    return redirect('/searchticket')


@login_required(login_url="/lt")
def track(request):
    obj = BusRegister.objects.all()
    if request.method == "POST":
        BusNumber = request.POST['BusNumber']
        ob = BusRegister.objects.get(BusRegisterNUmber=BusNumber)
        busstop = BusStop.objects.get(RouteId=ob.RouteId)
        return redirect("https://www.google.com/maps?q="+str(busstop.Latitude)+","+str(busstop.Longitude))
    else:
        pass
    return render(request, "track.html", {
        'busregisters': obj,
    })


@login_required(login_url="/lt")
def mapview(request):
    return render(request, "map.html")

# --------------------------------------------------------


def userlogin(request):
    username = request.POST['uname']
    passwd = request.POST['pass']
    print(username, passwd)
    try:
        ob = Login.objects.get(
            Username=username, Password=passwd, Type='conductor')
        print(ob)
        obu = Conductor.objects.get(lid=ob)
        data = {"task": 'valid', "lid": str(obu.UserId), "type": "conductor"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except Exception as e:
        try:
            ob = Login.objects.get(
                Username=username, Password=passwd, Type='user')
            print(ob)
            obu = Passenger.objects.get(LoginId=ob)
            data = {"task": 'valid', "lid": str(obu.UserId), "type": "user"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        except:
            pass
        print("qwerty", e)
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def userreg(request):
    username = request.POST['username']
    passwd = request.POST['password']

    fname = request.POST['fname']
    lname = request.POST['lname']
    cont = request.POST['contacts']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']

    ob = Login()

    ob.Username = username
    ob.Password = passwd
    ob.Type = "user"
    ob.save()

    obp = Passenger()
    obp.LoginId = ob
    obp.FirstName = fname
    obp.LastName = lname
    obp.Contact = cont
    obp.Place = place
    obp.Post = post
    obp.pin = pin
    obp.save()
    data = {"task": 'succes'}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def selectroute(request):
    ob = Route.objects.all()
    res1 = []
    for i in ob:
        r = {"rid": i.RouteId, "start_stop": i.StartingStop,
             "end_stop": i.EndingStop}
        res1.append(r)

    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def viewroutes(request):
    rid = request.POST['roid']

    ob = Route.objects.get(RouteId=rid)
    obb = BusRegister.objects.filter(RouteId=ob)

    res1 = []
    for i in obb:
        r = {"bregno": i.BusRegisterNUmber,
             "seatcapasity": i.SeatCapacity, "bid": i.BusId}

        ob1 = BusLocation.objects.filter(BusId=i)

        if(len(ob1) == 0):
            r['latitude'] = "11.1234"
            r['longitude'] = "75.12345"
        else:
            r['latitude'] = ob1[0].Latitude
            r['longitude'] = ob1[0].Longitude

        res1.append(r)

    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def androidbustime(request):
    bid = request.POST['bid']

    ob = BusRegister.objects.get(BusId=bid)
    obb = Bustime.objects.filter(BusId=ob)

    res1 = []
    for i in obb:
        r = {"stop": i.StopId.stop, "ticketchange": i.StopId.TicketCharge,
             "time": i.Time, "stopid": i.StopId.StopId}
        res1.append(r)
    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def seastops(request):
    bid = request.POST['sid']
    ob = BusRegister.objects.get(BusId=bid)
    obb = BusStop.objects.filter(RouteId=ob.RouteId)
    res1 = []
    for i in obb:
        r = {"stop": i.stop, "TicketCharge": i.TicketCharge, "StopId": i.StopId}
        res1.append(r)
    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def payment1(request):
    bid = request.POST['bid']
    sid = request.POST['sid']
    print(sid, "sss")
    uid = request.POST['lid']
    print(uid, "==================================")
    ob = BusRegister.objects.get(BusId=bid)
    obs = BusStop.objects.get(StopId=sid)
    obp = Passenger.objects.get(UserId=uid)
    obpb = PassengerBooking()
    obpb.StopId = obs
    obpb.BusId = ob
    obpb.PassengerId = obp
    obpb.save()
    res1 = {"result": "success", "bid": obpb.BookingId}
    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def afeedback(request):
    feed = request.POST['feedback']
    uid = request.POST['lid']
    obp = Passenger.objects.get(UserId=uid)
    obf = Feedback()
    obf.User_id = obp
    obf.Feedback = feed
    obf.Date = str(date.today())
    obf.save()
    res1 = {"result": "success"}
    r = json.dumps(res1)
    print(r)
    return HttpResponse(r)


def getalert(request):
    try:
        lati = request.POST['lati']
        uid = request.POST['uid']
        longi = request.POST['longi']
        import haversine as hs
        loc1 = (float(lati), float(longi))
        loc2 = (float(longi), float(lati))
        dist = hs.haversine(loc1, loc2)
        print(dist, "====gggggggggggggggggggggg")
        ob = PassengerBooking.objects.get(PassengerId=uid)
        print(ob.BookingId, "=====================================")
        ob1 = BusStop.objects.get(StopId=ob.StopId.StopId)
        lc1 = (float(ob1.Latitude), float(ob1.Longitude))
        lc2 = (float(ob1.Longitude), float(ob1.Latitude))
        dis = hs.haversine(lc1, lc2)
        print(dis, "====dddddddddddddddddddddddd")
        tot = dist-dis
        print(tot, "tottttttttttttttttttttt")
        if tot < 20.068:
            res1 = {"result": "success"}
            r = json.dumps(res1)
            print(r)
            return HttpResponse(r)
        else:
            res1 = {"result": "failed"}
            r = json.dumps(res1)
            print(r)
            return HttpResponse(r)
    except:
        lati = request.POST['lati']
        uid = request.POST['uid']
        longi = request.POST['longi']
        res1 = {"result": "failed"}
        r = json.dumps(res1)
        print(r)
        return HttpResponse(r)


def Bank1(request):
    bid = request.POST['bid']
    cno = request.POST['cno']
    pin = request.POST['pin']
    amt = request.POST['amt']
    uid = request.POST['pssid']
    ob = PassengerBooking.objects.get(BookingId=bid)
    obp = Passenger.objects.get(UserId=uid)
    obbank = Bank.objects.filter(
        PassangerId=obp, AccountNumber=cno, IFSE_code=pin)
    if len(obbank) == 0:
        res1 = {"result": "invalid"}
        r = json.dumps(res1)
        print(r)
        return HttpResponse(r)
    else:
        bal = obbank[0].Amount
        if bal < int(amt):
            res1 = {"result": "insufficient amount"}
            r = json.dumps(res1)
            print(r)
            return HttpResponse(r)
        else:
            obbank[0].Amount -= int(amt)
            obbank[0].save()
            obpay = payment()
            obpay.Booking_Id = ob
            obpay.Amount = amt
            obpay.Status = "payed"
            obpay.save()
            res1 = {"result": "success"}
            r = json.dumps(res1)
            print(r)
            return HttpResponse(r)


def locationupdate(request):
    try:
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        lid = request.POST['lid']
        print(lid, "===========================================")
        pob = Conductor.objects.get(UserId=lid)
        print(pob, "=======pobbbbbbbbbbbbbbbbbbbbbbb")
        ob1 = BusLocation.objects.filter(BusId=pob.Bus)
        print(ob1, "============obbbbb")
        if len(ob1) == 0:
            print("lennnnnnnnnnnnnnnnnnn")
            ob = BusLocation()
            ob.BusId = pob.Bus
            ob.Latitude = latitude
            ob.Longitude = longitude
            ob.save()
            data = {"task": "success"}
            r = json.dumps(data)
            return HttpResponse(r)
        else:
            print("elseeeeeeeeeeeeeeeeeee")
            obb = BusLocation.objects.get(BusId=pob.Bus)
            obb.Latitude = latitude
            obb.Longitude = longitude
            obb.save()
            data = {"task": "success"}
            r = json.dumps(data)
            return HttpResponse(r)
    except Exception as e:
        print(e, "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        obb = BusLocation.objects.get(BusId=pob.Bus)
        obb.Latitude = latitude
        obb.Longitude = longitude
        obb.save()
        data = {"task": "success"}
        r = json.dumps(data)
        return HttpResponse(r)
