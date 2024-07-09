import os
from PIL import Image
from tqdm import tqdm

# 指定输入文件夹和输出文件夹
input_folder = r'D:\gitlab2024\gaussian-splatting\data\1\input'
output_folder = r'D:\gitlab2024\gaussian-splatting\data\1_resize1500\input'

# 创建保存路径文件夹
os.makedirs(output_folder, exist_ok=True)

# 指定目标高宽
target_width = 1500
target_height = 1000
skip = 1
# 获取图片名字
image_list = os.listdir(input_folder)
image_list.sort()

# 遍历输入文件夹底下的所有图片
for i, filename in enumerate(tqdm(image_list)):
    # 每隔n张获取一张图
    if i % skip == 0:
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG"):
            # 打开图片
            img = Image.open(os.path.join(input_folder, filename))
            # 调整大小
            resized_img = img.resize((target_width, target_height))
            # 保存到输出文件夹
            resized_img.save(os.path.join(output_folder, filename))
