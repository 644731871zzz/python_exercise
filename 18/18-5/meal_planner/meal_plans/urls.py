from . import views
from django.urls import path

app_name='meal_plans'
urlpatterns=[
    path('',views.index,name='index')
]