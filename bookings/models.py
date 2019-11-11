from django.db import models
from django.forms import ModelForm
from django import forms

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    address = models.TextField()
    phone_no = models.PositiveIntegerField(max_size=15)
    max_size = models.PositiveIntegerField()

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = models.PositiveIntegerField(max_size=15)
    email = models.EmailField(max_length=300)

#Account Model
class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Person = models.ForeignKey(Person)
    Restaurant = models.ForeignKey(Restaurant)

#Reservation Model
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True)
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField()
    time_of_booking = models.DateTimeField(unique=True)
    Person = models.ForeignKey(Person)

#Dish Model
class Dish(models.Model):
	dishID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=None, decimal_places=2)
    Restaurant = models.ForeignKey(Restaurant)

#Order Model
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    address = models.TextField()
    Dish = models.ForeignKey(Dish)

#Form to register staff
class RegisterStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=300, widget=forms.EmailInput)
    class Meta:
        model = StaffAccount
        fields = ('username','password','first_name','second_name', 'email')

    def __str__(self):
        return self.username

#Form to login staff
class LoginStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = StaffAccount
        fields = ('username','password')

    def __str__(self):
        return self.username