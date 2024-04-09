import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 定义最小外接矩形顶点坐标
x_min, x_max = 425412.86, 428794.46
y_min, y_max = 3265875.98, 3268625.64
z_min, z_max = -18.35, 51.73

# 绘制图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 设置坐标轴等比例缩放
ax.set_box_aspect([np.ptp([x_min, x_max]), np.ptp([y_min, y_max]), np.ptp([z_min, z_max])])

# 绘制最小外接矩形
ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], zs=z_min, color='b')  # 底面
ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], zs=z_max, color='b')  # 顶面
ax.plot([x_min, x_min], [y_min, y_min], [z_min, z_max], color='b')  # 垂直边1
ax.plot([x_max, x_max], [y_min, y_min], [z_min, z_max], color='b')  # 垂直边2
ax.plot([x_max, x_max], [y_max, y_max], [z_min, z_max], color='b')  # 垂直边3
ax.plot([x_min, x_min], [y_max, y_max], [z_min, z_max], color='b')  # 垂直边4

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 定义四个矩形的坐标
#左下角顶点：右下角顶点：右上角顶点：左上角顶点：
rect1 = np.array([[425412.86, 3265875.98, -18.35],
                   [427103.66, 3265875.98, -18.35],
                   [427103.66, 3267250.81, 16.19],
                   [425412.86, 3267250.81, 16.19]])

rect2 = np.array([[427103.66, 3265875.98, -18.35],
                   [428794.46, 3265875.98, -18.35],
                   [428794.46, 3267250.81, 16.19],
                   [427103.66, 3267250.81, 16.19]])

rect3 = np.array([[425412.86, 3267250.81, -18.35],
                   [427103.66, 3267250.81, -18.35],
                   [427103.66, 3268625.64, 51.73],
                   [425412.86, 3268625.64, 51.73]])

rect4 = np.array([[427103.66, 3267250.81, -18.35],
                   [428794.46, 3267250.81, -18.35],
                   [428794.46, 3268625.64, 51.73],
                   [427103.66, 3268625.64, 51.73]])

# 绘制四个矩形外包围框，并使用不同颜色表示
ax.plot(rect1[[0,1,2,3,0],0], rect1[[0,1,2,3,0],1], zs=rect1[0,2], color='r')  # 红色
ax.plot(rect2[[0,1,2,3,0],0], rect2[[0,1,2,3,0],1], zs=rect2[0,2], color='g')  # 绿色
ax.plot(rect3[[0,1,2,3,0],0], rect3[[0,1,2,3,0],1], zs=rect3[0,2], color='b')  # 蓝色
ax.plot(rect4[[0,1,2,3,0],0], rect4[[0,1,2,3,0],1], zs=rect4[0,2], color='y')  # 黄色

# 显示图形
plt.show()

