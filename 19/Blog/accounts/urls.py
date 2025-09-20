"""为应用程序accounts配置url模式"""

from django.urls import path,include
from . import views

app_name='accounts'
urlpatterns=[
    path('',include('django.contrib.auth.urls')), #自动包含指定的django的urls,如果关键在在其中,将会导入django的页面
    path('register/',views.register,name='register')
]