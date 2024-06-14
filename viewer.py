import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

#使用 x 和 y 軸繪製正弦曲線
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# 在 x 和 z 軸上繪製散點圖資料 (每種顏色 20 個 2D 點)
colors = ('r', 'g', 'b', 'k')

# 設定隨機狀態以確保可重現性
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# 通過使用 zdir='y'，這些點的 y 值固定為 zs 值 0，
# 而 (x, y) 點被繪製在 x 和 z 軸上。
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')

# M添加圖例,設置坐標軸範圍和標籤
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 自定義視角,使散點更容易看到位於 y=0 平面上
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()