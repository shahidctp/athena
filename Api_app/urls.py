from django.urls import path
from .views import register_list, register_details, team_list, team_details, enquiry_list, enquiry_details, post_list, \
    post_details, comment_list, comment_details, like_list, like_details, menu_list, menu_details, category_list, \
    category_details, booking_details, booking_list, otp_details, otp_list

app_name = 'Api_app'

urlpatterns = [
    path('register_list/', register_list),
    path('register_details/<int:pk>/', register_details),
    path('team_list/', team_list),
    path('team_details/<int:pk>/', team_details),
    path('enquiry_list/', enquiry_list),
    path('enquiry_details/<int:pk>/', enquiry_details),
    path('post_list/', post_list),
    path('post_details/<int:pk>/', post_details),
    path('comment_list/', comment_list),
    path('comment_details/<int:pk>/', comment_details),
    path('like_list/', like_list),
    path('like_details/<int:pk>/', like_details),
    path('menu_list/', menu_list),
    path('menu_details/<int:pk>/', menu_details),
    path('category_list/', category_list),
    path('category_details/<int:pk>/', category_details),
    path('booking_list/', booking_list),
    path('booking_details/<int:pk>/', booking_details),
    path('otp_list/', otp_list),
    path('otp_details/<int:pk>/', otp_details),

]
