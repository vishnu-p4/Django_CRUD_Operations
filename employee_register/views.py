from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request , "employee_register/employee_list.html" , context)

"""
or 
context = Employee.objects.all()
return render (request ," template" , {'key as employee_list' : context})

"""




def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request , "employee_register/employee_form.html" , {'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee added Successfully ")
        return redirect('list')
    

def update(request,id):
    employee = get_object_or_404(Employee, pk=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        messages.info(request,"Employee updated to the List successfully")
        return redirect('list')
    return render(request, 'employee_register/employee_form.html', {'form': form})
    


def delete(request,id):
    employee  = Employee.objects.get(pk = id)
    employee.delete()
    messages.warning(request ,"Employee removed from the List")
    return redirect('list')




