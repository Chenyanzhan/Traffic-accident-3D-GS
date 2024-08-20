# -*- coding: utf-8 -*-
# @Time    : 2024/3/12 14:50
# @Author  : Chenyanzhan
# @Function  : 
# @File    : Traffic_accident_image_collect.py
# @Software: PyCharm

from Generate_camera_Pos import get_camera_positions
import sys
import glob
import os
try:
    sys.path.append(
        glob.glob('F://software/CARLA_0.9.13/WindowsNoEditor/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
            sys.version_info.major,
            sys.version_info.minor,
            'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import math
import random
import time
from queue import Queue
import numpy as np
import cv2
import matplotlib.pyplot as plt

class DataCollect():
    def __init__(self,ego_id):
        self.client = carla.Client('localhost', 2000)
        self.world = self.client.get_world()

        # 需要采集图片的自车的ID号
        self.ego_id = ego_id

        # Set up the simulator in synchronous mode
        self.original_settings = self.world.get_settings()

        self.center_x,self.center_y,self.center_z = 0, 0, 5
        self.radius = 5
        self.num_points = 100  # 控制图片的数量

        # 相机参数
        self.width = 1280 #1280
        self.height = 720 #720

        # 刹车时间
        self.brake_iter = 200

    def cam_sensor_callback(self,sensor_data, cam_queue):
        cam_queue.put(sensor_data)


    def process_image(self,image):
        raw_data = np.array(image.raw_data)  # h*w*4,1
        img_data = raw_data.reshape(self.height, self.width, 4)  # 4 = r+g+b+alpha
        img_data = img_data[:, :, :3]
        cv2.imshow('cam', img_data)
        cv2.waitKey(1)

    def reset(self):
        # settings = self.world.get_settings()
        # settings.synchronous_mode = True  # Enables synchronous mode
        # settings.fixed_delta_seconds = 0.05
        # self.world.apply_settings(settings)


        self.sensor_list = []
        self.cam_queue = Queue()

        # 寻找到python manual_control.py中生成的player车辆的ID
        ego_vehicle = self.world.get_actor(self.ego_id)

        # 初始化相机
        cam_bp = self.world.get_blueprint_library().find('sensor.camera.rgb')
        cam_bp.set_attribute("image_size_x", str(self.width))
        cam_bp.set_attribute("image_size_y", str(self.height))
        cam_bp.set_attribute("fov", str(105))


        cam_location = carla.Location(0.5, 0, 1.8)
        cam_rotation = carla.Rotation(0, 0, 0)
        cam_transform = carla.Transform(cam_location, cam_rotation)
        rgb_cam = self.world.spawn_actor(cam_bp, cam_transform, attach_to=ego_vehicle)
        rgb_cam.listen(lambda image: self.cam_sensor_callback(image, self.cam_queue))
        self.sensor_list.append(rgb_cam)


    def get_all_vehs(self):
        while True:
            actor_list = self.world.get_actors()
            if len(actor_list) > 0:
                break
            else:
                time.sleep(1.0)
        vehicle_actors = actor_list.filter("*vehicle*")
        return vehicle_actors

    def brake_all_vehs(self,vehicle_actors):
        for vehicle in vehicle_actors:
            control = vehicle.get_control()
            control.throttle = 0.0
            control.brake = 1.0
            control.hand_brake = True
            vehicle.apply_control(control)


    def save_data(self):
        camera_positions_1 = get_camera_positions(0, 0, 3, 3.5, 50)
        camera_positions_2 = get_camera_positions(0, 0, 4, 4, 50)
        camera_positions_3 = get_camera_positions(0, 0, 4.5, 4.5, 70)
        camera_positions_4 = get_camera_positions(0, 0, 5, 6, 90)
        camera_positions = camera_positions_1 + camera_positions_2 + camera_positions_3 + camera_positions_4

        #camera_positions = get_camera_positions(self.center_x, self.center_y, self.center_z, self.radius, self.num_points)

        for i, pos in enumerate(camera_positions):

            new_camera_transform = carla.Transform(carla.Location(x=pos[0], y=pos[1], z=pos[2]),
                                                   carla.Rotation(yaw=pos[4], pitch=-pos[3]))  # pitch - 10
            self.sensor_list[0].set_transform(new_camera_transform)

            self.world.tick()

            if self.cam_queue.empty():
                continue
            
            while not self.cam_queue.empty():
                cam_data = self.cam_queue.get(True, 1.0)

            print(self.cam_queue.qsize())
            cam_data.save_to_disk('./cam/%.6d.jpg' % i)


    def destroy(self):

        self.world.apply_settings(self.original_settings)
        for sensor in self.sensor_list:
            sensor.destroy()


if __name__ == '__main__':
    ID = 1110
    data_collect = DataCollect(ego_id=ID)

    data_collect.reset()
    data_collect.save_data()
    data_collect.destroy()

