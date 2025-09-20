from django.shortcuts import render

def index(request):
    """饮食计划主页"""
    return render(request,'meal_plans/index.html')
