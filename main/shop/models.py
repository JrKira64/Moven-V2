from django.db import models

# Create your models here.

class Roadtrip(models.Model):
    From = models.CharField(max_length=200)
    to = models.CharField(max_length=200)
    Date= models.DateField(blank=True, null=True)


class Contact(models.Model):
    email = models.EmailField('email', max_length=100)
    name = models.CharField('name', max_length=200)

    def __str__(self):
      return self.name

class Booking(models.Model):
    created_at = models.DateTimeField("created at", auto_now_add=True)
    contacted = models.BooleanField('contacted ?', default=False)
    roadtrip = models.OneToOneField(Roadtrip, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contact.name

