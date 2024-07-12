from rest_framework import serializers

from api.models import Employee,Task

class TaskSerializer(serializers.ModelSerializer):

    employee_obj=serializers.StringRelatedField()

    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=["id","employee_obj"]


class EmployeeSerializer(serializers.ModelSerializer):

    task_count=serializers.CharField(read_only=True)

    tasks=TaskSerializer(read_only=True,many=True)

    class Meta:

        model=Employee

        fields="__all__"
          
        read_only_fields=["id","assigned_date","completed_date","tasks"]

        