from PIL import Image

# 获取图片文件路径
image_path = input("请输入图片文件路径：")

# 打开图片文件
image = Image.open(image_path)

# 显示图片
image.show()
