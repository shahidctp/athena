from rest_framework import serializers
from Customerapp.models import Register, Team, Enquiry
from Blog_app.models import Post, Comments, Like
from Menuapp.models import Menu, Category
from Orderapp.models import Booking, Otp


# for_Customer_app
class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['username', 'email']


class Teamserializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'role', 'image']


class Enquiryserializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'subject', 'message']


# for_Blog_app
class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_name', 'title', 'date', 'image', 'category', 'description', 'user', 'liked']


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'website', 'message', 'commented_in']


class Likeserializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post', 'value']


# for_Menu_app
class Menuserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['item_name', 'price', 'description', 'image', 'category']


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


# for_Order_app
class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'mobile_number', 'preferred_time', 'date', 'booking_for', 'user']


class Otpserializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ['user', 'current_otp']
