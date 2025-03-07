from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class Booking(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.pet.name}: {self.check_in} to {self.check_out}"

class UploadForm(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    document = models.FileField(upload_to='uploads/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Form for {self.client.name} on {self.submitted_at}"
