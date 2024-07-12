from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from api.models import Employee,Task

from api.serializers import EmployeeSerializer,TaskSerializer

from rest_framework import viewsets 

from rest_framework.decorators import action

class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class=EmployeeSerializer

    queryset=Employee.objects.all()
    
    @action(methods=["POST"],detail=True)
    def add_task(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=Employee.objects.get(id=id)

        serializer_instance=TaskSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(employee_obj=employee_object)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
class TaskViewSet(viewsets.ModelViewSet):

    serializer_class=TaskSerializer

    queryset=Task.objects.all()

    
        

