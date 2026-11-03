from django.shortcuts import render, redirect
from .models import InternationalReservation, DomesticReservation
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def international_reservation_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        cnic = request.POST.get('cnic')
        passport_id = request.POST.get('passport_id')
        destination = request.POST.get('destination')
        travel_date = request.POST.get('travel_date')
        additional_requests = request.POST.get('additional_requests')

        InternationalReservation.objects.create(
            name=name,
            email=email,
            cnic=cnic,
            passport_id=passport_id,
            destination=destination,
            travel_date=travel_date,
            additional_requests=additional_requests
        )
        return redirect('reservation_success')  # make this URL or page
        
    return render(request, 'reservations/international_form.html')

@login_required(login_url='login')
def domestic_reservation_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        cnic = request.POST.get('cnic')
        destination = request.POST.get('destination')
        travel_date = request.POST.get('travel_date')
        additional_requests = request.POST.get('additional_requests')

        DomesticReservation.objects.create(
            name=name,
            email=email,
            cnic=cnic,
            destination=destination,
            travel_date=travel_date,
            additional_requests=additional_requests
        )
        return redirect('reservation_success')

    return render(request, 'reservations/domestic_form.html')


def success_page(request):
    return render(request,"reservations/reservation_success.html")
