from django.test import TestCase
from .models import Client, Pet, Booking, UploadForm

class ClientModelTest(TestCase):
    def test_string_representation(self):
        client = Client(name="John Doe")
        self.assertEqual(str(client), client.name)

class PetModelTest(TestCase):
    def test_string_representation(self):
        client = Client.objects.create(name="John Doe")
        pet = Pet(name="Buddy", owner=client)
        self.assertEqual(str(pet), pet.name)

class BookingModelTest(TestCase):
    def test_string_representation(self):
        client = Client.objects.create(name="John Doe")
        pet = Pet.objects.create(name="Buddy", owner=client)
        booking = Booking(pet=pet, check_in="2025-03-01", check_out="2025-03-05")
        self.assertEqual(str(booking), f"Booking for {pet.name} from {booking.check_in} to {booking.check_out}")

class UploadFormModelTest(TestCase):
    def test_string_representation(self):
        client = Client.objects.create(name="John Doe")
        pet = Pet.objects.create(name="Buddy", owner=client)
        upload_form = UploadForm(client=client, pet=pet, document="path/to/document")
        self.assertEqual(str(upload_form), f"Form for {client.name} on {upload_form.submitted_at}")