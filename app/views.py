from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_dept(request):
    if request.method=='POST':
        deptno=request.POST['dpo']
        dname=request.POST['dname']
        loc=request.POST['loc']
        DO=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)[0]
        DO.save()
        return HttpResponse('Data is inserted')
    return render(request,'insert_dept.html')


def insert_emp(request):
    DO=Dept.objects.all()
    d={'DO':DO}
    if request.method=='POST':
        empno=request.POST['empno']
        ename=request.POST['ename']
        deptno=request.POST['deptno']
        DO=Dept.objects.get(deptno=deptno)
        EO=Emp.objects.get_or_create(empno=empno,ename=ename,deptno=DO)[0]
        EO.save()
        return render(request,'display_emp.html')
    return render(request,'insert_emp.html',d)

def display_emp(request):
    EO=Emp.objects.all()
    #EO=Emp.objects.get(deptno=20)
    EO=Emp.objects.filter(deptno=20)
    EO=Emp.objects.filter(deptno=10)
    EO=Emp.objects.all()[2:5]
    EO=Emp.objects.filter().order_by('ename')
    EO=Emp.objects.filter().order_by('-ename')
    EO=Emp.objects.filter(ename__startswith='s')
    EO=Emp.objects.filter(ename__endswith='a')
    EO=Emp.objects.filter(ename__contains='t')
    EO=Emp.objects.filter(ename__in=('seshu','siva'))
    EO=Emp.objects.filter(ename__regex='^s\w+')
    
    d={'EO':EO}
    return render(request,'display_emp.html',d)