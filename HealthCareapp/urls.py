from collections import namedtuple
from django.contrib.admin.decorators import register
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('admin/', views.admin_page, name='admin_page'),
    path('patient/', views.patient_page, name='patient_page'),
    path('doctor/', views.doctor_page, name='doctor_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout, name='logged_out'),
    path('signup/', views.signup_page, name='signup_page'),
    path('register_user/', views.register_user, name='register_user'),
    path('doctorRec/', views.doctor_rec, name='doctor_rec'),
    path('viewDoctorProfile/', views.view_doctor_pro, name='view_doctor_pro'),
    path('viewAdminProfile/', views.view_admin_pro, name='view_admin_pro'),
    path('viewPatientProfile/', views.view_patient_pro, name='view_patient_pro'),
    path('editProfile/', views.view_edit_pro, name='view_edit_pro'),
    path('patientRec/', views.patient_rec, name='patient_rec'),
    path('data/<int:id>', views.delete_data, name = "deletedata"),
    path('delete/<int:id>', views.doc_del, name = "docdel"),
    path('depdelete/<int:id>', views.dep_del, name = "depdel"),
    path('updata/<int:id>/', views.update_data, name = "updatedata"),
    path('docupdate/<int:id>/', views.doc_update, name = "docupdate"),
    path('adminupdate/<int:id>/', views.admin_update, name = "adminupdate"),
    path('admin_doc_update/<int:id>/', views.admin_doc_update, name = "admin_doc_up"),
    path('department/', views.department, name = "department_page"),
    path('checked/<int:id>/', views.checked, name = "checkeddata"),
]
