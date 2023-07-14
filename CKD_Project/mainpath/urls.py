from django.urls import path
from . import views

urlpatterns=[
    path('main/',views.say_hello),
    path('form/',views.patient_form)
]