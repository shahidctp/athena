from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Register, Team, Enquiry
from Menuapp.models import Menu
from Orderapp.views import generate_otp
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    try:
        obj1 = Menu.objects.filter(category_id=1)
        obj2 = Menu.objects.filter(category_id=2)
        obj3 = Menu.objects.filter(category_id=3)
        obj5 = Team.objects.all()
        return render(request, 'index.html', {'obj1': obj1, 'obj2': obj2, 'obj3': obj3, 'obj5': obj5})
    except:
        return render(request, 'index.html', {'obj1': obj1, 'obj2': obj2, 'obj3': obj3, 'obj5': obj5})


def about(request):
    return render(request, 'about.html')


def feature(request):
    return render(request, 'feature.html')


def team(request):
    try:
        obj5 = Team.objects.all()
        return render(request, 'team.html', {'obj5': obj5})
    except:
        return render(request, 'team.html', {'obj5': obj5})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Enquiry.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def cus_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        email = request.POST.get('email')
        request.session['email'] = email
        password = request.POST.get('password')
        request.session['password'] = password
        confirm_password = request.POST.get('confirm_password')
        request.session['confirm_password'] = confirm_password
        otp2 = generate_otp()
        request.session['otp2'] = otp2
        print(otp2)
        html_gen = '<p>Your OTP is <strong>' + otp2 + '</strong></p>'
        print(html_gen)
        subject = 'Mail from Burgerking'
        send_mail(subject, otp2, settings.EMAIL_HOST_USER, [email], fail_silently=False, html_message=html_gen)

        return render(request, 'register_otp.html')
    else:
        return render(request, 'register.html')


def register_otp(request):
    if request.method == 'POST':
        username = request.session['username']
        email = request.session['email']
        password = request.session['password']
        confirm_password = request.session['confirm_password']
        otp2 = request.session['otp2']
        print(otp2, 'otp22')
        current_otp = request.POST.get('current_otp')
        print(current_otp, 'current_otp22')
        if current_otp == otp2:
            Register.objects.create(username=username, email=email)
            User.objects.create_user(username=username, email=email, password=password)
            del request.session['username']
            del request.session['email']
            del request.session['password']
            del request.session['confirm_password']
            del request.session['otp2']
            messages.warning(request, "Account created succesfully")
            return redirect('Customerapp:home')
        else:
            messages.warning(request, "invalid otp")
            return render(request, 'register_otp.html')
    else:
        return render(request, 'register_otp.html')


def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # messages.info(request, user.username)
            return redirect('Customerapp:home')
        else:
            messages.error(request, "invalid user")
            return redirect('Customerapp:login_request')
    else:
        return render(request, 'cus-login.html')


def logout_request(request):
    logout(request)
    return redirect('Customerapp:home')
