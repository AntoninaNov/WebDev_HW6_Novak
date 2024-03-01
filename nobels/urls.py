from django.urls import path
from .views import home, laureates_list, laureate_detail, create_laureate, delete_laureate

urlpatterns = [
    path('', home, name='home'),
    path('nobels/', laureates_list, name='laureates_list'),
    path('nobels/<int:id>/', laureate_detail, name='laureate_detail'),
    path('nobel/', create_laureate, name='create_laureate'),
    path('nobel/<int:id>/', delete_laureate, name='delete_laureate'),
]