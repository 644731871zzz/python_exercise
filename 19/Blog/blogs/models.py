from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """blog的主题"""
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """blog的具体内容"""
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        """定义如果模型为复数名称,正确显示复数名称"""
        verbose_name_plural='entries'

    def __str__(self):
        """返回一个表示条目的简单字符串"""
        if len(self.text) >50 :
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"