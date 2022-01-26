from collections import namedtuple
from datetime import time
from django.db import models
from django.utils.translation import templatize
from numpy import mod

class AddDepartment(models.Model):
    Department = models.CharField(max_length=255, blank=False)

    def __str__(self):
        template = '{0.Department}'
        return template.format(self)

class AdminLogin(models.Model):
    AdminEmail = models.EmailField()
    password = models.CharField(max_length=100)



class AddDoctors(models.Model):
    doc_name = models.CharField(max_length=75)
    doc_post = models.CharField(max_length=255)
    doc_timming = models.CharField(max_length=19)
    doc_ranking = models.CharField(max_length=3)
    doc_department = models.ForeignKey(AddDepartment, on_delete=models.CASCADE)
    doc_room = models.IntegerField()
    doc_specialization = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    doc_email_address = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        template = '{0.doc_name} , {0.doc_specialization}'
        return template.format(self)


class MakeAppointment(models.Model):
    Your_Name = models.CharField(max_length=80)
    Age = models.CharField(max_length=2)
    Disease = models.CharField(max_length=50)
    email_address = models.EmailField()
    Doctor = models.ForeignKey(AddDoctors , on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.Your_Name} , {0.Disease}'
        return template.format(self)

class PatientRecord(models.Model):
    patient_name = models.CharField(max_length=50)
    problem = models.CharField(max_length=20)
    time = models.DurationField(max_length=11)
    doctor = models.ForeignKey(AddDoctors  , on_delete=models.CASCADE)
    def __str__(self):
            template = '{0.patient_name} , {0.problem}'
            return template.format(self)

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        template = '{0.email}'
        return template.format(self)


class Signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    password = models.CharField(max_length=12)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        template = '{0.first_name} , {0.email_address}'
        return template.format(self)

class AI_Chatbot(models.Model):
    msg_operator = models.CharField(max_length = 200)
    msg_visitor = models.CharField(max_length =1000)

    def __str__(self):
        template = '{0.msg_operator} , {msg_visitor}'
        return template.format(self)
    

class SymptoInsert(models.Model):
    s1 = models.CharField(max_length= 150)
    s2 = models.CharField(max_length= 150)
    s3 = models.CharField(max_length= 150)
    s4 = models.CharField(max_length= 150)



