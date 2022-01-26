from django import forms
import django
from django.db.models import fields
from django.forms import widgets
from django.shortcuts import render
from django.utils import tree
from .models import *
from django.core import validators


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = AddDepartment
        fields = '__all__'
        widgets = {
            'Department' : forms.TextInput(attrs={'class':'form-control'}),
        }


class AddDoctorsForm(forms.ModelForm):
    doc_name = forms.CharField(required=True)
    doc_post = forms.CharField(required=True)
    doc_specialization = forms.CharField(required=True)
    doc_room = models.IntegerField()
    doc_timming = forms.CharField(required=True)
    # doc_name = models.CharField()
    # doc_post = models.CharField()
    # doc_timming = models.CharField()
    # doc_ranking = models.CharField()
    # doc_department = models.ForeignKey(AddDepartment, on_delete=models.CASCADE)
    # doc_room = models.IntegerField()
    # doc_specialization = models.CharField()
    # phone_number = models.PositiveIntegerField()
    # doc_email_address = models.EmailField()
    # password = models.CharField()

    class Meta:
        model = AddDoctors
        fields = '__all__'
        # widgets = {
        #     'doc_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'doc_post' : forms.TextInput(attrs={'class':'form-control'}),
        #     'doc_timming' : forms.TextInput(attrs={'class':'form-control'}),
        #     'doc_ranking' : forms.TextInput(attrs={'class':'form-control'}),
        #     'doc_room' : forms.NumberInput(attrs={'class':'form-control'}),
        #     'doc_department' : forms.TextInput(attrs={'class':'form-control'}),
        #     'doc_specialization' : forms.TextInput(attrs={'class':'form-control'}),
        #     'phone_number' : forms.NumberInput(attrs={'class':'form-control'}),
        #     'doc_email_address' : forms.EmailInput(attrs={'class':'form-control'}),
        #     'password' : forms.PasswordInput(attrs={'class':'form-control'})
        #     ,
        # }

# class SymptomAddForm(forms.ModelForm):
#     sym1 = forms.CharField(required=True)
#     sym2 = forms.CharField(required=True)
#     sym3 = forms.CharField(required=True)
#     sym4 = forms.CharField(required=True)

#     class Meta:
#         model = SymptomsAdd
#         fields = "__all__"
        
class MakeAppointmentForm(forms.ModelForm):
    Your_Name = forms.CharField(required=True)
    Age = forms.CharField(required=True)
    Disease = forms.CharField(required=True)
    Doctor = models.ForeignKey(AddDoctors , on_delete=models.CASCADE)

    class Meta:
        model = MakeAppointment
        fields = "__all__"
        


class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = Login
        fields = '__all__'


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = Signup
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email_address' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value= True, attrs={'class':'form-control'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control'})
            ,
        }

# class SymptomsAdd(forms.models):
#     symptom1 = models.CharField(max_length=200)
#     symptom2 = models.CharField(max_length=200)
#     symptom3 = models.CharField(max_length=200)
#     symptom4 = models.CharField(max_length=200)

#     class Meta:
#         model = SymptomAdd
#         fields = '__all__'

# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control'}),
#             'email' : forms.EmailInput(attrs={'class':'form-control'}),
#             'password' : forms.PasswordInput(render_value= True, attrs={'class':'form-control'})
#             ,
#         }

class updPassForm(forms.ModelForm):
    password = models.CharField()
    class Meta:
        model = AddDoctors
        fields = {'password'}
        widgets = {
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }

class updAdminForm(forms.ModelForm):
    password = models.CharField()
    class Meta:
        model = AdminLogin
        fields = {'password'}
        widgets = {
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
