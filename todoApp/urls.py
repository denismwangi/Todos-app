from django.urls import path
from . import views

urlpatterns = [
    
    path('list/', views.list_todo_items),
    path('insert_todo/',views.insert_todo_item, name='insert_item'),
    path('delete_item/<int:todo_id>/', views.delete_item, name='delete_item')


]
