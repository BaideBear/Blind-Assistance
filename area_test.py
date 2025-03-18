from PIL import Image, ImageDraw

# 假设图像的宽度W和高度H
W, H = 700, 900  # 示例图像尺寸

# 划分比例
left_width = int(0.10 * W)
left_center_width = int(0.15 * W)
center_width = int(0.40 * W)
right_center_width = int(0.15 * W)
right_width = int(0.10 * W)

# 图像创建
image = Image.new('RGB', (W, H), color='white')
draw = ImageDraw.Draw(image)

# 计算每个区域的边界
bottom_left1_X = W * 0.1 #最左侧和偏左侧分界
bottom_left2_X = W * 0.4 #偏左侧和中间分界
bottom_right1_X = W * 0.6 #中间和偏右侧分界
bottom_right2_X = W * 0.9 #偏右侧和最右侧分界
top_left1_X = W * 0.15
top_left2_X = W * 0.45
top_right1_X = W * 0.55
top_right2_X = W * 0.85

# 画出区域划分的斜线
draw.line((top_left1_X, H/2, bottom_left1_X, H), fill='black', width=2)  # 左侧与偏左侧分割线
draw.line((top_left2_X, H/2, bottom_left2_X, H), fill='black', width=2)  # 偏左侧与正前方分割线
draw.line((top_right1_X, H/2, bottom_right1_X, H), fill='black', width=2)  # 正前方与偏右侧分割线
draw.line((top_right2_X, H/2, bottom_right2_X, H), fill='black', width=2)  # 偏右侧与右侧分割线


# 显示图像
image.show()

# 可选：保存图片
image.save("divided_image.png")
