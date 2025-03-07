from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Pet, Booking, UploadForm
from .forms import ClientForm, PetForm, BookingForm, UploadFormForm
from django.http import JsonResponse
from django.core.serializers import serialize

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'dashboard/client_list.html', {'clients': clients})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'dashboard/pet_list.html', {'pets': pets})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'dashboard/booking_list.html', {'bookings': bookings})

def upload_form_list(request):
    upload_forms = UploadForm.objects.all()
    return render(request, 'dashboard/upload_form_list.html', {'upload_forms': upload_forms})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'dashboard/add_client.html', {'form': form})

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'dashboard/add_pet.html', {'form': form})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'dashboard/add_booking.html', {'form': form})

def add_upload_form(request):
    if request.method == 'POST':
        form = UploadFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_form_list')
    else:
        form = UploadFormForm()
    return render(request, 'dashboard/add_upload_form.html', {'form': form})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'dashboard/client_detail.html', {'client': client})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'dashboard/pet_detail.html', {'pet': pet})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'dashboard/booking_detail.html', {'booking': booking})

def upload_form_detail(request, upload_form_id):
    upload_form = get_object_or_404(UploadForm, id=upload_form_id)
    return render(request, 'dashboard/upload_form_detail.html', {'upload_form': upload_form})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.delete()
    return redirect('pet_list')

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('booking_list')

def delete_upload_form(request, upload_form_id):
    upload_form = get_object_or_404(UploadForm, id=upload_form_id)
    upload_form.delete()
    return redirect('upload_form_list')

def calendar_view(request):
    return render(request, 'dashboard/calendar.html')

def booking_events(request):
    bookings = Booking.objects.all()
    events = []
    for booking in bookings:
        events.append({
            'title': booking.pet.name,
            'start': booking.check_in.strftime('%Y-%m-%d'),
            'end': booking.check_out.strftime('%Y-%m-%d'),
        })
    return JsonResponse(events, safe=False)