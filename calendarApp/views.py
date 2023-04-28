from django.shortcuts import render
from .models import Appointment
from django.db.models import Q

# Create your views here.

def index(request):
    appointments = Appointment.objects.filter(Q(user= request.user) | Q(business__user= request.user)).order_by('-start_time')

    context = {
        "appointments" : appointments
    }
    
    return render(request, "calendar.html", context)