from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic,Entry

from .forms import TopicForm,EntryForm

def index(request):
    return render(request,'blogs/index.html')


def topics(request):
    #按照时间顺序排序
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'blogs/topics.html',context)


def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    #使用了自动生成的set函数获取所有内容
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'blogs/topic.html',context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            #添加新主题时候保寸用户id到数据库
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            return redirect('blogs:topics')
        
    context={'form':form}
    return render(request,'blogs/new_topic.html',context)

@login_required        
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)

    check_top_owner(request,topic)

    if request.method != 'POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('blogs:topic',topic_id=topic_id)
        
    context={'topic':topic,'form':form}
    return render(request,'blogs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    check_top_owner(request,topic)

    if request.method !='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:topic',topic_id=topic.id)
        
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'blogs/edit_entry.html',context)


def check_top_owner(request,topic):
    if topic.owner != request.user:
        raise Http404