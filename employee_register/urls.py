from django.urls import path , include
from .import views

urlpatterns = [
    path('',views.employee_form , name = 'form'),
    path('update/<int:id>/',views.update , name = 'update'),
    path('list/',views.employee_list , name = 'list'),
    path('delete/<int:id>/' ,views.delete , name = 'delete'),
]