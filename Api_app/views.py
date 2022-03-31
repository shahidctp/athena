from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import Registerserializer, Teamserializer, Enquiryserializer, Postserializer, Commentserializer, \
    Likeserializer, Menuserializer, Categoryserializer, Bookingserializer, Otpserializer
from rest_framework.parsers import JSONParser
from Customerapp.models import Register, Team, Enquiry
from Blog_app.models import Post, Comments, Like
from Menuapp.models import Menu, Category
from Orderapp.models import Booking, Otp


# for_Customer_app
@csrf_exempt
def register_list(request):
    if request.method == 'GET':
        register = Register.objects.all()
        serializer = Registerserializer(register, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Registerserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def register_details(request, pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Registerserializer(register)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Registerserializer(register, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        register.delete()
        return HttpResponse(status=204)


@csrf_exempt
def team_list(request):
    if request.method == 'GET':
        team = Team.objects.all()
        serializer = Teamserializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Teamserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def team_details(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Teamserializer(team)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Teamserializer(team, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        team.delete()
        return HttpResponse(status=204)


@csrf_exempt
def enquiry_list(request):
    if request.method == 'GET':
        enquiry = Enquiry.objects.all()
        serializer = Enquiryserializer(enquiry, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Enquiryserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def enquiry_details(request, pk):
    try:
        enquiry = Enquiry.objects.get(pk=pk)
    except Enquiry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Enquiryserializer(enquiry)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Enquiryserializer(enquiry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        enquiry.delete()
        return HttpResponse(status=204)


# for_Blog_app
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = Postserializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Postserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_details(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Postserializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Postserializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)


@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comment = Comments.objects.all()
        serializer = Commentserializer(comment, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Commentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def comment_details(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Commentserializer(comment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Commentserializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comment.delete()
        return HttpResponse(status=204)


@csrf_exempt
def like_list(request):
    if request.method == 'GET':
        like = Like.objects.all()
        serializer = Likeserializer(like, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Likeserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def like_details(request, pk):
    try:
        like = Like.objects.get(pk=pk)
    except Like.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Likeserializer(like)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Likeserializer(like, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        like.delete()
        return HttpResponse(status=204)


# for_Menu_app
@csrf_exempt
def menu_list(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer = Menuserializer(menu, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Menuserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu_details(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Menuserializer(menu)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Menuserializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        menu.delete()
        return HttpResponse(status=204)


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = Categoryserializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Categoryserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_details(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Categoryserializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Categoryserializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)


# for_Order_app
@csrf_exempt
def booking_list(request):
    if request.method == 'GET':
        booking = Booking.objects.all()
        serializer = Bookingserializer(booking, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Bookingserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def booking_details(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Bookingserializer(booking)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Bookingserializer(booking, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        booking.delete()
        return HttpResponse(status=204)


@csrf_exempt
def otp_list(request):
    if request.method == 'GET':
        otp = Otp.objects.all()
        serializer = Otpserializer(otp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Otpserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def otp_details(request, pk):
    try:
        otp = Otp.objects.get(pk=pk)
    except Otp.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Otpserializer(otp)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Otpserializer(otp, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        otp.delete()
        return HttpResponse(status=204)
