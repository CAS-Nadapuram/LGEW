from django.db import models


class Login(models.Model):
    UserId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    Type = models.CharField(max_length=25)

    def __str__(self):
        return self.Username


class Passenger(models.Model):
    UserId = models.AutoField(primary_key=True)
    LoginId = models.ForeignKey(Login, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20, null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)

    def __str__(self):
        return self.FirstName


class Route(models.Model):
    RouteId = models.AutoField(primary_key=True)
    StartingStop = models.CharField(max_length=50)
    EndingStop = models.CharField(max_length=50)

    def __str__(self):
        return self.StartingStop


class BusRegister(models.Model):
    BusId = models.AutoField(primary_key=True)
    BusRegisterNUmber = models.CharField(max_length=40)
    SeatCapacity = models.IntegerField()
    RouteId = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.BusRegisterNUmber


class Conductor(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20, null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)
    Bus = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    lid = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.FirstName


class Feedback(models.Model):
    User_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=120)
    Date = models.DateField()

    def __str__(self):
        return self.User_id


class Bank(models.Model):
    BankId = models.AutoField(primary_key=True)
    PassangerId = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    AccountNumber = models.IntegerField()
    IFSE_code = models.CharField(max_length=20)
    Amount = models.IntegerField()

    def __str__(self):
        return self.PassangerId


class BusLocation(models.Model):
    LocationId = models.AutoField(primary_key=True)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.BusId


class BusStop(models.Model):
    StopId = models.AutoField(primary_key=True)
    RouteId = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.CharField(max_length=30)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    TicketCharge = models.IntegerField()

    def __str__(self):
        return self.stop


class Bustime(models.Model):
    TimeId = models.AutoField(primary_key=True)
    StopId = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    Time = models.CharField(max_length=30)

    def __str__(self):
        return self.BusId


class PassengerBooking(models.Model):
    BookingId = models.AutoField(primary_key=True)
    PassengerId = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    StopId = models.ForeignKey(BusStop, on_delete=models.CASCADE)

    def __str__(self):
        return self.PassengerId


class payment(models.Model):
    PayId = models.AutoField(primary_key=True)
    Booking_Id = models.ForeignKey(PassengerBooking, on_delete=models.CASCADE)
    Amount = models.FloatField()
    Status = models.CharField(max_length=110)

    def __str__(self):
        return self.Booking_Id


class QRcode(models.Model):
    id = models.AutoField(primary_key=True)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)

    def __str__(self):
        return self.id