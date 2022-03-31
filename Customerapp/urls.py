from django.urls import path
from .views import home, about, feature, team, cus_signup, login_request, logout_request, contact, register_otp

app_name = 'Customerapp'

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('feature/', feature, name='feature'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
    path('cus_signup/', cus_signup, name='cus_signup'),
    path('login_request/', login_request, name='login_request'),
    path('logout_request/', logout_request, name='logout_request'),
    path('register_otp/', register_otp, name='register_otp'),

]
