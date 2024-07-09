# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 9:20
# @Author  : Chenyanzhan
# @Function  : 
# @File    : My_train_batch.py.py
# @Software: PyCharm

import os
import subprocess

root_path = './data/'

for town_path in os.listdir(root_path):
    sub_path = os.path.join(root_path, town_path)
    for case_path in os.listdir(sub_path):
        # 如果没有 convert 过，就进行转化
        if 'sparse' in os.listdir(os.path.join(sub_path, case_path)):
            images_path = os.path.join(sub_path, case_path)

            # 脚本运行
            command = f'python train.py -s' + images_path + '/'
            subprocess.run(command, shell=True)