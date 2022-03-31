from django.shortcuts import render, redirect, HttpResponse
from .models import Booking, Otp
from django.contrib.auth.models import User
from django.db.models import F
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import math, random
from django.db.models import Q


def generate_otp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


def booking(request):
    if request.method == 'POST':
        booking_for = request.POST.get('booking_for')
        request.session['booking_for'] = booking_for
        name = request.POST.get('name')
        request.session['name'] = name
        email = request.POST.get('email')
        request.session['email'] = email
        mobile_number = request.POST.get('mobile_number')
        request.session['mobile_number'] = mobile_number
        date = request.POST.get('date')
        request.session['date'] = date
        print(date)
        print('hiiiii')
        preferred_time = request.POST.get('preferred_time')
        request.session['preferred_time'] = preferred_time
        date_time_count = Booking.objects.filter((Q(date=date) & Q(preferred_time=preferred_time))).count()
        date_time_count123 = date_time_count + 1
        print(date_time_count123)
        if date_time_count123 <= 10:
            user = User.objects.get(id=request.user.id)
            o = generate_otp()
            print(o)
            html_gen = '<p>Your OTP is <strong>' + o + '</strong></p>'
            print(html_gen)
            subject = 'Mail from Burgerking'
            send_mail(subject, o, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=html_gen)
            if Otp.objects.filter(user_id=request.user.id).exists():
                exist1 = Otp.objects.filter(user_id=user.id).update(current_otp=o)
                print(exist1, 'exist1')
                return redirect('Orderapp:email_otp')
            else:
                exist2 = Otp.objects.create(current_otp=o, user_id=user.id)
                print(exist2, 'exist2')
                return redirect('Orderapp:email_otp')
        else:
            messages.info(request, "No tables are available on selected date")
            return redirect('Orderapp:booking')
    else:
        print('kkkkkk')
        return render(request, 'booking.html')


def email_otp(request):
    if request.method == 'POST':
        booking_for = request.session['booking_for']
        name = request.session['name']
        email = request.session['email']
        mobile_number = request.session['mobile_number']
        date = request.session['date']
        preferred_time = request.session['preferred_time']
        current_otp = request.POST.get('current_otp')
        print(current_otp)
        print(type(current_otp))
        user123 = Otp.objects.get(user_id=request.user.id)
        print(user123.current_otp)
        print(type(user123.current_otp))
        if user123.current_otp == int(current_otp):
            user = User.objects.get(id=request.user.id)
            print(user)
            Booking.objects.create(booking_for=booking_for, name=name, email=email, mobile_number=mobile_number,
                                   date=date, preferred_time=preferred_time, user_id=user.id)
            del request.session['name']
            del request.session['email']
            del request.session['mobile_number']
            del request.session['date']
            del request.session['preferred_time']
            del request.session['booking_for']
            messages.warning(request, "Table booked succesfully")
            return redirect('Orderapp:booking')
        else:
            messages.error(request, 'invalid otp')
            return render(request, 'email_otp.html')
    else:
        return render(request, 'email_otp.html')


def table_details(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        obj11 = Booking.objects.filter(date=date)
        return render(request, 'table.html', {'obj11': obj11})
    else:
        obj11 = Booking.objects.all()
        return render(request, 'table.html', {'obj11': obj11})


def delete(request, pk):
    Booking.objects.filter(id=pk).delete()
    # Table.objects.update(table_count=F('table_count') + 1)
    return redirect('Orderapp:table_details')
