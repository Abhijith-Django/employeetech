from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

routers=DefaultRouter()

routers.register("employees",views.EmployeeViewSet,basename="employees")

routers.register("tasks",views.TaskViewSet,basename="tasks")


urlpatterns=[
           
]+routers.urls