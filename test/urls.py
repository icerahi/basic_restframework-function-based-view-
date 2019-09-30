from django.urls import path

from test.views import contact_list, contact_details

urlpatterns = [
    path('contacts/',contact_list),
    path('contacts/<int:pk>/',contact_details),
]