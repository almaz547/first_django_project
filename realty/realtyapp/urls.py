from realtyapp import views
from django.urls import path

app_name = 'realtyapp'

urlpatterns = [
    # path('', views.main_view, name='index'),
    path('', views.IndexListView.as_view(), name='index'),
    # path('sale/', views.sale, name='sale'),
    path('sale/', views.SaleListView.as_view(), name='sale'),
    # path('rent/', views.rent, name='rent'),
    path('rent/', views.RentListView.as_view(), name='rent'),
    # path('new_buildings/', views.new_buildings, name='new_buildings'),
    path('new_buildings/', views.New_buildingsListView.as_view(), name='new_buildings'),
    # path('message/', views.message, name='message'),
    path('message/', views.MessageCreateView.as_view(), name='message'),
    # path('apartment/<int:id>/', views.apartment, name='apartment'),
    path('apartment/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment'),
    # path('personal_area/', views.personal_area, name='pers_area'),
    path('personal_area/', views.PersonalListView.as_view(), name='pers_area'),
    path('create_apart/', views.ApartmentCreateFormView.as_view(), name='create_apart'),
    path('updata_apart/<int:pk>/', views.ApartmentUpdataView.as_view(), name='updata_apart'),
    path('delete_confirm/<int:pk>/', views.ApartmentDeleteView.as_view(), name='delete_apart'),
    path('delete_image_confirm/<int:pk>', views.ImageDeleteView.as_view(), name='delete_image')
]
