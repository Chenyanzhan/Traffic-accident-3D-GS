

# A Virtual-Real-Fusion Framework for Intelligent 3D Traffic Accident Reconstruction

This study proposes a novel virtual-real-fusion simulation framework that integrates traffic accident generation, unmanned aerial vehicle (UAV)-based image collection and a 3D traffic accident reconstruction pipeline with advanced computer vision techniques and unsupervised 3D point clouds clustering algorithms.

## 目录


- [开发前的配置要求](#开发前的配置要求)
- [Running](#Running)
- [RenderingForTown03](#RenderingForTown03)
- [RenderingForTown04](#RenderingForTown04)
- [RenderingForTown10](#RenderingForTown10)
- [作者](#作者)


### 开发前的配置要求

###### Hardware Requirements

- CUDA-ready GPU with Compute Capability 7.0+
- 24 GB VRAM (to train to paper evaluation quality)
- Please see FAQ for smaller VRAM configurations

###### Software Requirements

- Conda (recommended for easy setup)
- C++ Compiler for PyTorch extensions (we used Visual Studio 2019 for Windows)
- CUDA SDK 11 for PyTorch extensions, install *after* Visual Studio (we used 11.8, **known issues with 11.6**)
- C++ Compiler and CUDA SDK must be compatible

### Running
To run the optimizer, simply use

```shell
python train.py -s /content/gaussian-splatting/carla/
```

### Renderings for Town03


### Renderings for Town04


### Renderings for Town10

![2024 07 09-16 06 40-ezgif com-optimize](https://github.com/Chenyanzhan/Traffic-accident-3D-GS/assets/59226366/1c223e25-344d-4ba9-a3a2-6f478431b669)


### 作者
Yanzhan Chen


### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt)

