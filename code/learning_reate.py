


learning_rate = 5e-5 
min_learning_rate = 1e-5 


passed = 0 
steps = 100
def on_batch_begin(batch, logs=None):
    """
        第一个epoch用来warmup，第二个epoch把学习率降到最低
    """
    global passed, steps 
    if passed < steps:
        lr = (passed + 1.) / steps * learning_rate
        passed += 1
    elif steps <=  passed < steps * 2:
        lr = 2 - (passed + 1.) / steps * (learning_rate - min_learning_rate)
        lr += min_learning_rate
        passed += 1
    else: 
        lr = None 
    return lr 



x = [] 
y = [] 
for i in range(100): 
    rate = on_batch_begin(i)
    if rate: 
        x.append(i)
        y.append(rate)


    
import matplotlib.pyplot as plt
import numpy as np

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)


# 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
plt.plot(x, y, color="blue", linewidth=1.0, linestyle="-")

# # 设置横轴的上下限
# plt.xlim(-1, 6)
# # 设置纵轴的上下限
# plt.ylim(-2, 10)

plt.show()







