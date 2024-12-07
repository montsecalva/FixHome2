from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required  # Decorador que asegura que solo los usuarios autenticados pueden acceder a esta vista
def home(request):
    # Crear un diccionario de contexto que contiene el rol del usuario autenticado
    context = {
        'role': request.user.role if request.user.is_authenticated else None  # Si el usuario está autenticado, añade su rol al contexto
    }
    # Renderiza la plantilla 'appointments/home.html' con el contexto proporcionado
    return render(request, 'appointments/home.html', context)


@login_required
def create_appointment(request):
    if request.user.role != 'tenant':
        return redirect('home')

    if request.method == 'POST':
        repair_type = request.POST['repair_type']
        date = request.POST['date']
        time = request.POST['time']
        description = request.POST['description']
        Appointment.objects.create(
            tenant=request.user,
            repair_type=repair_type,
            date=date,
            time=time,
            description=description
        )
        return redirect('appointment_list')

    return render(request, 'appointments/create_appointment.html')


@login_required
def manage_appointments(request):
    if request.user.role != 'admin':
        return redirect('home')

    appointments = Appointment.objects.all()
    return render(request, 'appointments/manage_appointments.html', {'appointments': appointments})



@login_required
def appointment_list(request):
    if request.user.role != 'tenant':
        return render(request, 'appointments/access_denied.html')

    appointments = Appointment.objects.filter(tenant=request.user)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})
