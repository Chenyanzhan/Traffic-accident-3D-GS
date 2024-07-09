import os
import subprocess

# 图片集所在的绝对路径
images_path = r"F:\Workspace\Project\gaussian-splatting\data\carla-town10\example2\input"

# 上一级文件夹所在路径
folder_path = os.path.dirname(images_path)

# 脚本运行
# COLMAP估算相机位姿
command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)

