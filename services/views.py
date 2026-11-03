from django.shortcuts import render
from services.models import Services

# Create your views here.
def services_view(request):
    services=Services.objects.all()
    
    return render(request,"services/services.html",{'services':services})
