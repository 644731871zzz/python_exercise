"""定义blog的urls"""
from django.urls import path
from . import views

#定义名称,方便html中的代码查询到此app
app_name='blogs'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    path('topics',views.topics,name='topics'),
    path('topic/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]