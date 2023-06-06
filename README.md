# Python-DisplayImage
Python显示路径图片的程序
from PIL import Image: 这行代码导入了Pillow库中的Image模块，它提供了处理图像的功能。

image_path = input("请输入图片文件路径："): 这行代码提示用户输入图片文件的路径，并将输入的路径保存到image_path变量中。

image = Image.open(image_path): 这行代码使用Image.open()函数打开指定路径的图片文件，并将返回的图像对象保存到image变量中。

image.show(): 这行代码调用图像对象的show()方法，它将显示该图像。注意，这将会调用系统默认的图像查看器来显示图像。
