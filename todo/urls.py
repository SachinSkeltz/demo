from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_home,name='home'),
    # path('delete/<int:task_id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete')

    ]