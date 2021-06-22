from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.instruction, name="intructions"),
    path('patient/', views.patient_api.as_view(), name="patient-api"),
    path('doctor/', views.doctor_api.as_view(), name="doctor-api"),
    path('history/', views.history_api.as_view(), name="history-api"),
    path('details/', views.details_api.as_view(), name="details-api"),
    path('reports/', views.reports_api.as_view(), name="reports-api"),
    path('booking/', views.booking_api.as_view(), name="booking-api"),
    path('api-get-otp/', views.request_otp, name="forgot-otp"),
]

# this regex will match any url pattern and then render the 404 page.
urlpatterns += [
    re_path(r'.*', views.instruction, name="error"),
]
