from django.db import models
from datetime import date
from .choices import GENDER_CHOICES


class Record(models.Model):

    creation_date = models.DateField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    Sex = models.CharField(choices= GENDER_CHOICES, max_length=1)

    Nationality = models.CharField(max_length=255)

    Birth_date = models.DateField(max_length=255)

    Age = models.IntegerField()

    Passport = models.CharField(max_length=20)

    Arrival_date = models.DateField(max_length=300)

    Departure_date = models.DateField(max_length=255)

    Stay = models.DateField(max_length=255)

    Purpose = models.CharField(max_length=200)

    Hotel = models.CharField(max_length=125)

    Id_document = models.ImageField(upload_to='customer/')

    DisplayFields = ['first_name','last_name',' Nationality','Sex','Birth_date','Age','Passport','Arrival_date','Departure_date','Stay','Purpose','Hotel','creation_date','Id_document']
    
    def __str__(self):

        return self.first_name + "   " + self.last_name
    
    @property
    def Age(self):
        Age = (self.Arrival_date.year - self.Birth_date.year)
        return Age
    
    def Stay(self):
        Stay = self.Departure_date - self.Arrival_date
        return Stay

class Product(models.Model):
    Hotel = models.CharField(max_length=100, null=False, blank=False)
    num_of_User = models.IntegerField()

    def __str__(self):
        return f'{self.Hotel} - {self.num_of_User}'
    
class Nation(models.Model):
    country = models.CharField(max_length=100, null=False, blank=False)
    num_of_visiter = models.IntegerField()

    def __str__(self):
        return f'{self.country} - {self.num_of_visiter}'
    
class Sex(models.Model):
    gender = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.gender} - {self.number}'
    
class Purpose(models.Model):
    Kind_visit = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.Kind_visit} - {self.count}'
