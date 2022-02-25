# Generated by Django 3.2.8 on 2022-02-25 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusRegister',
            fields=[
                ('BusId', models.AutoField(primary_key=True, serialize=False)),
                ('BusRegisterNUmber', models.CharField(max_length=40)),
                ('SeatCapacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('StopId', models.AutoField(primary_key=True, serialize=False)),
                ('stop', models.CharField(max_length=30)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('TicketCharge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=25)),
                ('Password', models.CharField(max_length=25)),
                ('Type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20, null=True)),
                ('LastName', models.CharField(max_length=20, null=True)),
                ('Contact', models.BigIntegerField(null=True)),
                ('Place', models.CharField(max_length=20, null=True)),
                ('Post', models.CharField(max_length=20, null=True)),
                ('pin', models.BigIntegerField(null=True)),
                ('LoginId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.login')),
            ],
        ),
        migrations.CreateModel(
            name='PassengerBooking',
            fields=[
                ('BookingId', models.AutoField(primary_key=True, serialize=False)),
                ('BusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busregister')),
                ('PassengerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.passenger')),
                ('StopId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('RouteId', models.AutoField(primary_key=True, serialize=False)),
                ('StartingStop', models.CharField(max_length=50)),
                ('EndingStop', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('BusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busregister')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('PayId', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Status', models.CharField(max_length=110)),
                ('Booking_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.passengerbooking')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.CharField(max_length=120)),
                ('Date', models.DateField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20, null=True)),
                ('LastName', models.CharField(max_length=20, null=True)),
                ('Contact', models.BigIntegerField(null=True)),
                ('Place', models.CharField(max_length=20, null=True)),
                ('Post', models.CharField(max_length=20, null=True)),
                ('pin', models.BigIntegerField(null=True)),
                ('Bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busregister')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.login')),
            ],
        ),
        migrations.CreateModel(
            name='Bustime',
            fields=[
                ('TimeId', models.AutoField(primary_key=True, serialize=False)),
                ('Time', models.CharField(max_length=30)),
                ('BusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busregister')),
                ('StopId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busstop')),
            ],
        ),
        migrations.AddField(
            model_name='busstop',
            name='RouteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.route'),
        ),
        migrations.AddField(
            model_name='busregister',
            name='RouteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.route'),
        ),
        migrations.CreateModel(
            name='BusLocation',
            fields=[
                ('LocationId', models.AutoField(primary_key=True, serialize=False)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('BusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.busregister')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('BankId', models.AutoField(primary_key=True, serialize=False)),
                ('AccountNumber', models.IntegerField()),
                ('IFSE_code', models.CharField(max_length=20)),
                ('Amount', models.IntegerField()),
                ('PassangerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainCode.passenger')),
            ],
        ),
    ]
