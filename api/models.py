from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    phone=models.CharField(max_length=200)

    email=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()
    
    @property
    def task_count(self):

        return self.task_set.all().count()

    @property 
    def tasks(self):

        return self.task_set.all()

    def __str__(self):
        return self.name
    
class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    options=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=options,default="pending")

    assigned_date=models.DateTimeField(auto_now_add=True)

    completed_date=models.DateField(auto_now=True)

    employee_obj=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
