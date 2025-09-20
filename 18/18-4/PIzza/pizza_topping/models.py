from django.db import models

class Pizza(models.Model):
    """继承了Model模型"""
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Topping(models.Model):
    """继承Model模型并且关联Pizza"""
    topic=models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text=models.TextField()
    data_apped=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='toppings'

    def __str__(self):
        if len(self.text)<=50:
            return f'{self.text}'
        else:
            return f'{self.text[:50]}...'
