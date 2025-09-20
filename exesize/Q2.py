#Q2
import math
import matplotlib.pyplot as plt

num=100
#创建了函数的起始值和最终值,并求出了公差
x_start=-3
x_end=3
x_step=(x_end-x_start)/(num-1)

#这里将所有函数中的x进行配置 并且创建了需要后续用的y的数列集合
x_array=[x_start+i*x_step for i in range(num)]
y_array=[]

#计算y的值并使用for配置到y_array
for x in x_array:
    y=math.exp(x)
    y_array.append(y)

#绘制图像
plt.plot(x_array,y_array)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()