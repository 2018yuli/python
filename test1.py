import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('./assets/1.jpg')  # 替换为你图像的路径

# 检查图像是否加载成功
if image is None:
    print("Error: Unable to load image.")
else:
    # 转换 BGR 到 RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 使用 matplotlib 显示图像
    plt.imshow(image_rgb)
    plt.axis('off')  # 关闭坐标轴
    plt.show()
