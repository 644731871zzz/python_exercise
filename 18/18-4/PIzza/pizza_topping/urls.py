from . import views
from django.urls import path


app_name='pizza_topping'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
]