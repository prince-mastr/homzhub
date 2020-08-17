from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Request_type(models.Model):
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description


class State(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.name

class Status(models.Model):
    condition = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.condition

class Request(models.Model):
    id = models.AutoField
    requested_by_user = models.ForeignKey(to = User,blank=False, null= False, on_delete=models.CASCADE)
    request_type = models.ManyToManyField(Request_type)
    request_desc = models.CharField(max_length=100, blank=False, null=False)
    request_date = models.DateField(max_length=100, blank=False, null=False)
    Status = models.ForeignKey(to = Status,blank=False, null= False, on_delete=models.CASCADE)
    Remarks = models.CharField(max_length=100, blank=False, null=False)
    City = models.CharField(max_length=100, blank=False, null=False)
    state = models.ForeignKey(to = State,blank=False, null= False, on_delete=models.CASCADE)
    pincode = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)], blank=False, null=False)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)], blank=False, null=False)
    def __str__(self):
        return str(self.id)