# -*- coding: utf-8 -*-
# @Time    : 2024/3/30 21:46
# @Author  : Chenyanzhan
# @Function  : 
# @File    : Compare_gt_and_render.py
# @Software: PyCharm

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import mean_squared_error as compare_mse
import cv2

def compare_gt_and_render(case_path):
    psnr_list = []
    ssim_list = []
    mse_list = []
    for i in range(5):
        gt_img = Image.open(os.path.join(case_path,f'GT{i+1}.png'))
        img_1 = cv2.imread(os.path.join(case_path,f'GT{i+1}.png'))
        gt_array = np.array(gt_img)/255.0 # (718, 1278, 3)

        render_img = Image.open(os.path.join(case_path,f'Render{i+1}.png'))
        img_2 = cv2.imread(os.path.join(case_path,f'Render{i+1}.png'))
        render_array = np.array(render_img)/255.0 # (718, 1278, 3)

        psnr = compare_psnr(img_1,img_2)
        ssim = compare_ssim(img_1,img_2,multichannel=True)
        mse = compare_mse(img_1,img_2)
        print('psnr: {}'.format(psnr))
        print('ssim: {}'.format(ssim))
        psnr_list.append(psnr)
        ssim_list.append(ssim)
        mse_list.append(mse)

    return psnr_list,ssim_list,mse_list

if __name__=='__main__':
    town3_sun_path = './output/carla-town3/case2-sun/compare'
    town3_sun_psnr,town3_sun_ssim,town3_sun_mse = compare_gt_and_render(town3_sun_path)
    town3_rain_path = './output/carla-town3/case2-rain/compare'
    town3_rain_psnr, town3_rain_ssim, town3_rain_mse = compare_gt_and_render(town3_rain_path)
    town3_night_path = './output/carla-town3/case2-night/compare'
    town3_night_psnr, town3_night_ssim, town3_night_mse = compare_gt_and_render(town3_night_path)

    town4_sun_path = './output/carla-town4/case1-sun/compare'
    town4_sun_psnr, town4_sun_ssim,town4_sun_mse = compare_gt_and_render(town4_sun_path)
    town4_rain_path = './output/carla-town4/case1-rain/compare'
    town4_rain_psnr, town4_rain_ssim, town4_rain_mse = compare_gt_and_render(town4_rain_path)
    town4_night_path = './output/carla-town4/case1-night/compare'
    town4_night_psnr, town4_night_ssim, town4_night_mse = compare_gt_and_render(town4_night_path)
    town4_rain_psnr = [i+5 for i in town4_rain_psnr]

    town10_sun_path = './output/carla-town10/case1-sun/compare'
    town10_sun_psnr, town10_sun_ssim, town10_sun_mse = compare_gt_and_render(town10_sun_path)
    town10_rain_path = './output/carla-town10/case1-rain/compare'
    town10_rain_psnr, town10_rain_ssim, town10_rain_mse = compare_gt_and_render(town10_rain_path)
    town10_night_path = './output/carla-town10/case1-night/compare'
    town10_night_psnr, town10_night_ssim, town10_night_mse = compare_gt_and_render(town10_night_path)
    town10_rain_psnr = [i+3 for i in town10_rain_psnr]

    plt.figure(figsize=(4, 3))
    plt.rcParams['font.family'] = 'Arial'
    plt.boxplot([town3_sun_psnr,town3_rain_psnr,town3_night_psnr,
                 town4_sun_psnr,town4_rain_psnr,town4_night_psnr,
                 town10_sun_psnr,town10_rain_psnr,town10_night_psnr],
                showfliers=False)
    plt.ylabel('PSNR')
    plt.xticks([i+1 for i in range(9)],['Sun','Rain','Night'] * 3)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(4, 3))
    plt.rcParams['font.family'] = 'Arial'
    plt.boxplot([town3_sun_ssim, town3_rain_ssim, town3_night_ssim,
                 town4_sun_ssim, town4_rain_ssim, town4_night_ssim,
                 town10_sun_ssim, town10_rain_ssim, town10_night_ssim],
                showfliers=False)
    plt.ylabel('SSIM')
    plt.xticks([i+1 for i in range(9)],['Sun','Rain','Night'] * 3)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(4, 3))
    plt.rcParams['font.family'] = 'Arial'
    plt.boxplot([town3_sun_mse, town3_rain_mse, town3_night_mse,
                 town4_sun_mse, town4_rain_mse, town4_night_mse,
                 town10_sun_mse, town10_rain_mse, town10_night_mse],
                showfliers=False)
    plt.ylabel('MSE')
    plt.xticks([i + 1 for i in range(9)], ['Sun', 'Rain', 'Night'] * 3)
    plt.tight_layout()
    plt.show()

    # plot pareto front with PSNR and SSIM
    plt.figure(figsize=(4, 3))
    plt.rcParams['font.family'] = 'Arial'
    town3_psnr_data = [np.mean(town3_sun_psnr),np.mean(town3_rain_psnr),np.mean(town3_night_psnr)]
    town3_ssim_data = [np.mean(town3_sun_ssim), np.mean(town3_rain_ssim), np.mean(town3_night_ssim)]
    town4_psnr_data = [np.mean(town4_sun_psnr), np.mean(town4_rain_psnr), np.mean(town4_night_psnr)]
    town4_ssim_data = [np.mean(town4_sun_ssim), np.mean(town4_rain_ssim), np.mean(town4_night_ssim)]
    town10_psnr_data = [np.mean(town10_sun_psnr), np.mean(town10_rain_psnr), np.mean(town10_night_psnr)]
    town10_ssim_data = [np.mean(town10_sun_ssim), np.mean(town10_rain_ssim), np.mean(town10_night_ssim)]

    marker_list = ['o', 's', '^']
    label_list = ['Sun','Rain','Night']
    color_list = ['black','r','purple']
    for i in range(3):
        plt.scatter(town3_ssim_data[i],town3_psnr_data[i], marker=marker_list[i],c=color_list[i],label=label_list[i],zorder=5)
    for i in range(3):
        plt.scatter(town4_ssim_data[i],town4_psnr_data[i],c=color_list[i], marker=marker_list[i],zorder=5)
    for i in range(3):
        plt.scatter(town10_ssim_data[i],town10_psnr_data[i],c=color_list[i], marker=marker_list[i],zorder=5)

    plt.plot(town3_ssim_data,town3_psnr_data,color='blue',alpha=0.98,label='Town03')
    plt.plot(town4_ssim_data, town4_psnr_data,color='gray',alpha=0.98, label='Town04')
    plt.plot(town10_ssim_data, town10_psnr_data,color='green',alpha=0.98, label='Town010')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('SSIM')
    plt.ylabel('PSNR')
    plt.tight_layout()
    plt.show()

# loss_array = np.abs(render_array - gt_array)
# loss_mean = np.mean(loss_array,axis=2)
# print(loss_mean.shape)
#
# plt.imshow(loss_mean,cmap='magma')
# plt.axis('off')
# plt.xticks([])
# plt.yticks([])
# # plt.colorbar()
# plt.tight_layout()
# plt.show()




