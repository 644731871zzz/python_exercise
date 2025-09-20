from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request,'pizza_topping/index.html')

def pizzas(request):
    """显示所有的pizza"""
    #根据data_added进行排序
    pizzas=Pizza.objects.order_by('data_added')
    #定义发送给模板的数据这里是字典中键值对,值为类似列表的一个可迭代对象(django专用)
    context={'pizzas':pizzas}
    return render(request,'pizza_topping/pizzas.html',context)

def pizza(request,pizza_id):
    """显示单个pizza主题极其所有条目的界面"""
    pizza=Pizza.objects.get(id=pizza_id)
    entries=pizza.topping_set.order_by('-data_apped')
    context={'pizza':pizza,'entries':entries}
    return render(request,'pizza_topping/pizza.html',context)