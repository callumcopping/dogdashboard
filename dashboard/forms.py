from django import forms
from .models import Client, Pet, Booking, UploadForm

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'name', 'breed', 'age', 'notes']

class BookingForm(forms.ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['pet', 'check_in', 'check_out']

class UploadFormForm(forms.ModelForm):
    class Meta:
        model = UploadForm
        fields = ['client', 'pet', 'document']