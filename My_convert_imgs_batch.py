import os
import subprocess

root_path = './data/'

for town_path in os.listdir(root_path):
    sub_path = os.path.join(root_path,town_path)
    for case_path in os.listdir(sub_path):
        # 如果没有 convert 过，就进行转化
        if 'sparse' not in os.listdir(os.path.join(sub_path,case_path)): 
            images_path = os.path.join(sub_path,case_path) + '/input'
            
            # 上一级文件夹所在路径
            folder_path = os.path.dirname(images_path)

            # 脚本运行
            # COLMAP估算相机位姿
            command = f'python convert.py -s {folder_path}'
            subprocess.run(command, shell=True)
