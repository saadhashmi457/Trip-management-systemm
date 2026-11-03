from django.urls import path
from reservations import views

urlpatterns = [
    path('reservation/international/', views.international_reservation_view, name='international_reservation'),
    path('reservation/domestic/', views.domestic_reservation_view, name='domestic_reservation'),
    path('reservation/success/', views.success_page, name='reservation_success'),  # optional
]