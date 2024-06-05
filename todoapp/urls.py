from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
]
