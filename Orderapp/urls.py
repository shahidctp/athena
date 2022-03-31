from django.urls import path

from .views import booking, table_details, delete, email_otp

app_name = 'Orderapp'

urlpatterns = [
        path('booking/', booking, name='booking'),
        path('table_details/', table_details, name='table_details'),
        path('table_detail/delete/<int:pk>/', delete, name='delete'),
        path('email_otp/', email_otp, name='email_otp'),

]
