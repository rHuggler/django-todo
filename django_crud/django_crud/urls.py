from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('admin/', admin.site.urls),
]
