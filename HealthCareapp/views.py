
from itertools import count
from re import T, search
from typing import ContextManager
from django import http
from django.forms.forms import Form
from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime
import random
from django.utils import tree
from .forms import *
from .models import *
from django.contrib import messages
import numpy as np
import pandas as pd
from django.template import RequestContext, context
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from django.contrib import messages


Disease_symptoms = pd.read_excel('D:\HealthCare\HealthCare/newDataset.xlsx')

Disease_symptoms['Symptom_1'] = Disease_symptoms['Symptom_1'].str.replace(" ","")
Disease_symptoms['Symptom_1'] = Disease_symptoms['Symptom_1'].str.replace("_","")
Disease_symptoms['Symptom_2'] = Disease_symptoms['Symptom_2'].str.replace(" ","")
Disease_symptoms['Symptom_2'] = Disease_symptoms['Symptom_2'].str.replace("_","")
Disease_symptoms['Symptom_3'] = Disease_symptoms['Symptom_3'].str.replace(" ","")
Disease_symptoms['Symptom_3'] = Disease_symptoms['Symptom_3'].str.replace("_","")
Disease_symptoms['Symptom_4'] = Disease_symptoms['Symptom_4'].str.replace(" ","")
Disease_symptoms['Symptom_4'] = Disease_symptoms['Symptom_4'].str.replace("_","")
Disease_symptoms['Symptoms'] = Disease_symptoms['Symptom_1'] + "," + Disease_symptoms['Symptom_2'] + "," + Disease_symptoms['Symptom_3'] + "," + Disease_symptoms['Symptom_4']
Disease_symptoms = Disease_symptoms.drop(columns="Symptom_1")
Disease_symptoms = Disease_symptoms.drop(columns="Symptom_2")
Disease_symptoms = Disease_symptoms.drop(columns="Symptom_3")
Disease_symptoms = Disease_symptoms.drop(columns="Symptom_4")
Disease_symptoms['Precautions'] = "You have suffering from " + Disease_symptoms['Disease'] + " and " + Disease_symptoms['Description'] + " So Don't Worry Just Follow These medicines " + Disease_symptoms['Medicine_1'] + " and avoid every things which is not good for health " + Disease_symptoms['Precaution_1'] + " " + Disease_symptoms['Precaution_2'] + " " + Disease_symptoms['Precaution_3'] + " " + Disease_symptoms['Precaution_4']
Disease_symptoms = Disease_symptoms.drop(columns="Precaution_1")
Disease_symptoms = Disease_symptoms.drop(columns="Precaution_2")
Disease_symptoms = Disease_symptoms.drop(columns="Precaution_3")
Disease_symptoms = Disease_symptoms.drop(columns="Precaution_4")
Disease_symptoms = Disease_symptoms.drop(columns="Medicine_1")
Disease_symptoms = Disease_symptoms.drop(columns="Description")
Disease_symptoms.dropna(inplace=True)
x = np.array(Disease_symptoms['Symptoms'])
y = Disease_symptoms['Precautions']
  
cv = CountVectorizer(
    stop_words='english',
)
X = cv.fit_transform(x)
svc_s = SVC()

X_train , X_test , Y_train , Y_test = train_test_split(X , y , test_size=0.2 )
svc_s.fit(X_train , Y_train)



def home_page(request):
    return render(request, 'home.html')


def signup_page(request):
    return render(request, 'signup.html')


def register_user(request):
    if request.POST:
        request.session['fname'] = request.POST['fname']
        request.session['lname'] = request.POST['lname']
        request.session['pnumber'] = request.POST['pnumber']
        request.session['email'] = request.POST['eml']
        request.session['Password'] = request.POST['Password']
        obj = Signup(first_name=request.session['fname'], last_name=request.session['lname'],
                     phone_number=request.session['pnumber'],  email_address=request.session['email'], password=request.session['Password'] )
        count = Signup.objects.filter(
            email_address=request.session['email']).count()
        if count > 0:
            return render(request, 'signup.html', {"username_error": "Username Already Exist"})
        else:
            obj.save()
        return redirect('/home/login')


def login_page(request):
    if request.POST:
        request.session['email'] = request.POST['email']
        request.session['Password'] = request.POST['password']
        count_patient = Signup.objects.filter(
            email_address=request.session['email'], password=request.session['Password']).count()
        count_doctor = AddDoctors.objects.filter(
            doc_email_address=request.session['email'], password=request.session['Password']).count()
        count_admin = AdminLogin.objects.filter(
            AdminEmail = request.session['email'], password=request.session['Password']).count()
    
        if count_patient > 0:
            return redirect("/home/patient/")
        elif count_doctor > 0 :
            return redirect("/home/doctor/")
        elif count_admin > 0 :
            return redirect("/home/admin/")
        else:
            inval = "Please Enter right credentials"
            return render(request, 'login.html', {"Details_Error": inval})

    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return render(request,"home.html")

def admin_page(request):
    if not request.session.get('email'):
        return redirect('/home/')
    else:
        if request.method == 'GET':
            formdata = AddDoctorsForm()
            formdata2 = AddDepartmentForm()
        else:
            formdata = AddDoctorsForm(data=request.POST)
            formdata2 = AddDepartmentForm(data=request.POST)
            if formdata.is_valid():
                formdata.save()
            elif formdata2.is_valid():
                formdata2.save()
            else:
                messages.error(request, 'The form is invalid.')
            return redirect('/home/admin/')
    admin_verified = AdminLogin.objects.filter(AdminEmail = request.session.get('email'))
    return render(request, 'admin.html', {'printdata': AddDoctorsForm, 'doc_data': AddDoctors.objects.all(), 'doc_department': AddDepartmentForm, 'docterdata': AddDepartment.objects.all(),"Your_Email":request.session.get('email')})


def AI_Chatbot_App(request, Dept):
    patient_Info = Signup.objects.get(email_address = request.session.get('email'))
    
    print("Patient email  = ", patient_Info)
    Depart_name = AddDepartment.objects.get(Department=Dept)

    print("Department Name", Depart_name)
    print("Department id = ",Depart_name.id)

    Doc_Info = AddDoctors.objects.get(doc_department_id =Depart_name)
    Doc_Name = Doc_Info.doc_name

    print("Doctor Info  = ", Doc_Info)
    print("Doctor Name  = ", Doc_Name)

    patient_name = patient_Info.first_name
    print("Patient Name = ",patient_name)

    patient_email_address = request.session.get("email")
    print("Email = ",patient_email_address)
    do_appoint = MakeAppointment(
        Your_Name=patient_name ,
    
        email_address=patient_email_address,
        Doctor=Doc_Info
        )
    if do_appoint :
        do_appoint.save()
        msg = "Appointment Booked"
        print(msg)
    else:
        pass
    context = {"Appoint_msg": msg}
    print(context)
  



def patient_page(request):
    if request.POST:
        if 'symptomsbtn' in request.POST:
            sy1 = request.POST['s1']
            sy2 = request.POST['s2']
            sy3 = request.POST['s3']
            sy4 = request.POST['s4']
            sym = SymptoInsert(s1 = sy1, s2 = sy2, s3 = sy3, s4 = sy4)
            sym.save()

            fatch = SymptoInsert.objects.all()
            for item in fatch:
                item.s1
                item.s2
                item.s3
                item.s4

            problem = item.s1 + "," + item.s2 + "," + item.s3 + "," + item.s4
            vectors = cv.transform([problem]).toarray()
            prediction = svc_s.predict(vectors)
            
            d = dict(enumerate(prediction.flatten(), 1))
            print("printing the prediction type")
            print(type(d))
            fatch.delete()
            print(problem)
            print(d)
            a_dict = d
            search_1 = "medical"
            search_2 = "dermatology"
            search_3 = "gastroenterology"
            search_4 = "Endocrinology"
            search_5 = "hepatitis"
            search_6 = "orthopedic"
            search_7 = "ENT"
            search_8 = "Nephrology"
            search_9 = "surgical"
            search_10 = "Neurology"
            search_11 = "urology"
            search_12 = "Pulmonologist"
            search_13 = "cardiology"
            search_14 = "covid"

            for value in a_dict.values():
                if search_1 in value:
                    print(search_1)
                    AI_Chatbot_App(request, search_1)
                elif search_2 in value:
                    print(search_2)
                    AI_Chatbot_App(request, search_2)
                elif search_3 in value:
                    print(search_3)
                    AI_Chatbot_App(request, search_3)
                elif search_4 in value:
                    print(search_4)
                    AI_Chatbot_App(request, search_4)
                elif search_5 in value:
                    print(search_5)
                    AI_Chatbot_App(request, search_5)
                elif search_6 in value:
                    print(search_6)
                    AI_Chatbot_App(request, search_6)
                elif search_7 in value:
                    print(search_7)
                    AI_Chatbot_App(request, search_7)
                elif search_8 in value:
                    print(search_8)
                    AI_Chatbot_App(request, search_8)
                elif search_9 in value:
                    print(search_9)
                    AI_Chatbot_App(request, search_9)
                elif search_10 in value:
                    print(search_10)
                    AI_Chatbot_App(request, search_10)
                elif search_11 in value:
                    print(search_11)
                    AI_Chatbot_App(request, search_11)
                elif search_12 in value:
                    print(search_12)
                    AI_Chatbot_App(request, search_12)
                elif search_13 in value:
                    print(search_13)
                    AI_Chatbot_App(request, search_13)
                elif search_14 in value:
                    print(search_14)
                    AI_Chatbot_App(request, search_14)
                
            patient_verified = Signup.objects.filter(email_address = request.session.get('email'))
            print(patient_verified)
            formdata = MakeAppointmentForm()
            get_doc_details = MakeAppointment.objects.filter(email_address = request.session.get("email"))

            context = {"form":formdata,"appointinfo":reversed(get_doc_details.all()) , "Your_Email":request.session.get('email'), "doc_data":AddDoctors.objects.all(),"apnt_dtl": MakeAppointment.objects.all(), 'pres': d, 'prob': problem} 
        
            return render(request, 'patient.html', context)
            
        elif 'appointmentbtn' in request.POST:
            patient_verified = Signup.objects.filter(email_address = request.session.get('email'))
            print(patient_verified)
            if not request.session.get('email'):
                return redirect('/home/')
            elif patient_verified:
                if request.method == 'GET':
                    formdata = MakeAppointmentForm()
                else:
                    formdata = MakeAppointmentForm(data=request.POST)
                    if formdata.is_valid():
                        formdata.save()
                    else:
                        messages.error(request, 'The form is invalid.')

            get_doc_details = MakeAppointment.objects.filter(email_address = request.session.get("email"))
   
            context = {"form":formdata,"appointinfo":reversed(get_doc_details.all()) , "Your_Email":request.session.get('email'), "doc_data":AddDoctors.objects.all(), "apnt_dtl": MakeAppointment.objects.all()} 
            return render(request, 'patient.html', context)
            
            
    else:
        patient_verified = Signup.objects.filter(email_address = request.session.get('email'))
        print(patient_verified)
        if not request.session.get('email'):
            return redirect('/home/')
        formdata = MakeAppointmentForm()
       
        get_doc_details = MakeAppointment.objects.filter(email_address = request.session.get("email"))
     
        context = {"form":formdata,"appointinfo":reversed(get_doc_details.all()) , "Your_Email":request.session.get('email'), "doc_data":AddDoctors.objects.all(), "apnt_dtl": MakeAppointment.objects.all()} 
        return render(request, 'patient.html', context)

def doctor_page(request):
    if not request.session.get('email'):
        return redirect('/home/')
    else:
        get_doc_details = AddDoctors.objects.filter(doc_email_address = request.session.get("email"))
        for i in get_doc_details.all():
            print(i.id)
            treatments = MakeAppointment.objects.filter(Doctor = i.id)
            
        total_no_of_treatments = treatments.count()
        date = datetime.date.today()
        context = {"Your_Email": request.session.get('email'),"treatments":reversed(treatments) , 'date': date, 'total_no_of_treatments': total_no_of_treatments}
        return render(request, 'doctor.html', context)

def doctor_rec(request):
    CONTEXT = {'department_details': AddDepartment.objects.all(
    ), 'docter_rec': AddDoctors.objects.all()}
    return render(request, 'doctorRec.html', CONTEXT)

def patient_rec(request):
    CONTEXT = {'patientrec_details': MakeAppointment.objects.all(), 'docterdata': AddDepartment.objects.all(), 'regstr_pt': Signup.objects.all()}
    return render(request, 'patientsRec.html', CONTEXT)


def view_doctor_pro(request):
    get_doc_details = AddDoctors.objects.get(doc_email_address = request.session.get("email"))
    return render(request, 'viewDoctorProfile.html' , {"doc_details":get_doc_details})


def view_patient_pro(request):
    get_patient_details = Signup.objects.filter(email_address = request.session.get("email"))
    return render(request, 'viewPatientProfile.html' , {"patient_details":get_patient_details.all()})


def view_admin_pro(request):
    get_admin_details = AdminLogin.objects.all()
    return render(request, 'viewAdminProfile.html' , {"admin_details": get_admin_details})
    


def view_edit_pro(request):
    return render(request, 'editpro.html')

def department(request):
    CONTEXT = {'department_details': AddDepartment.objects.all()}
    return render(request, 'departments.html', CONTEXT)
    
  

def contact(request):
    return render(request, 'patient.html')

def delete_data(request, id):
    if request.method == 'POST':
        pi = MakeAppointment.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/home/patient')

def doc_del(request, id):
    if request.method == 'POST':
        pi = AddDoctors.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/home/admin')

def dep_del(request, id):
    if request.method == 'POST':
        pi = AddDepartment.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/home/department')

def checked(request, id):
    if request.method == 'POST':
        pi = MakeAppointment.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/home/doctor')

def doc_update(request, id):
    if request.POST:
        p = AddDoctors.objects.get(pk = id)
        f = updPassForm(request.POST, instance = p)
        if f.is_valid():
            f.save()
    else:
        p = AddDoctors.objects.get(pk = id)
        f = updPassForm(instance = p)
    return render(request, 'editdoc.html', {'edpr': f})

def admin_update(request, id):
    if request.POST:
        p = AdminLogin.objects.get(pk = id)
        f = updAdminForm(request.POST, instance = p)
        if f.is_valid():
            f.save()
    else:
        p = AdminLogin.objects.get(pk = id)
        f = updAdminForm(instance = p)
    return render(request, 'editadmin.html', {'edpr': f})


def update_data(request, id):
    if request.POST:
        pi = Signup.objects.get(pk = id)
        fm = SignupForm(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Signup.objects.get(pk = id)
        fm = SignupForm(instance = pi)
    return render(request, 'editpro.html', {'edtpro': fm})


def admin_doc_update(request, id):
    if request.POST:
        pi = AddDoctors.objects.get(pk = id)
        fm = AddDoctorsForm(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = AddDoctors.objects.get(pk = id)
        fm = AddDoctorsForm(instance = pi)
    return render(request, 'ad_doc_edit.html', {'edtpro': fm})


