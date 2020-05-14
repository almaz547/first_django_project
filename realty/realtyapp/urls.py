from realtyapp import views
from django.urls import path

app_name = 'realtyapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('sale/', views.sale, name='sale'),
    path('rent/', views.rent, name='rent'),
    path('new_buildings/', views.new_buildings, name='new_buildings'),
    path('message/', views.message, name='message'),
    path('apartment/<int:id>/', views.apartment, name='apartment')
]
