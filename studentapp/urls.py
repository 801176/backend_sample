from django.urls import path
from .import views
from.views import StudentListCreate,StudentRetrieveUpdateDistroy

urlpatterns=[
    path('students/',StudentListCreate.as_view(),name='student-list-create'),
    path('students/<int:pk>',StudentRetrieveUpdateDistroy.as_view(),name='student-detail')

]
