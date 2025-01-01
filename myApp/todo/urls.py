from django.urls import path


from .views import index,updateTask,deleteTask

urlpatterns =[
    path('', index, name=""),

    path('update-task/<str:pk>/',updateTask,name="update-task"),

    path('delete-task/<str:pk>/',deleteTask,name="delete-task"),

]