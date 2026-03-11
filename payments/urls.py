from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,            name='home'),
    path('course/<int:course_id>/', views.course_detail,   name='course_detail'),
    path('pay/<int:course_id>/',    views.payment_page,    name='payment_page'),
    path('process/',                views.process_payment, name='process_payment'),
]