from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('additem', views.addItem),
    path('dummy', views.getDataDummy),
    path('todo', views.getTodo),
    path('addtodo', views.addTodo),
]
