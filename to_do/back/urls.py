from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.start),
    path("gentodo", views.new_to_do),
    path('new-task', views.new_task, name=""),
    path('make_done', views.make_done, name=""),
    path("delete_task", views.delete_task, name="")
]