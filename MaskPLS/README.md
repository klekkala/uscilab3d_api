# Mask-Based Panoptic LiDAR Segmentation for Autonomous Driving

This repository contains the implementation of our [paper](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/marcuzzi2023ral.pdf).

## Installation

* Install this package by running in the root directory of this repo:

```
pip3 install -U -e .
```

* Install the packages in [requirements.txt](requirements.txt).


## Data preparation

### SemanticKITTI
Download the [SemanticKITTI](http://www.semantic-kitti.org/dataset.html#overview) dataset inside the directory `data/kitti/`. The directory structure should look like this:
```
./
└── data/
    └── kitti
        └── sequences
            ├── 00/           
            │   ├── velodyne/	
            |   |	├── 000000.bin
            |   |	├── 000001.bin
            |   |	└── ...
            │   └── labels/ 
            |       ├── 000000.label
            |       ├── 000001.label
            |       └── ...
            ├── 08/ # for validation
            ├── 11/ # 11-21 for testing
            └── 21/
                └── ...
```

### NuScenes
We use [nuscenes2kitti](https://github.com/PRBonn/nuscenes2kitti) to convert the nuScenes format into the SemanticKITTI format and store it in `data/nuscenes/`.

In the scripts, use the `--nuscenes` flag to train or evaluate using this dataset.

## Pretrained models

* [SemanticKITTI](https://www.ipb.uni-bonn.de/html/projects/mask_based_panoptic_segmentation/mask_pls_kitti.ckpt)

* [NuScenes](https://www.ipb.uni-bonn.de/html/projects/mask_based_panoptic_segmentation/mask_pls_nuscenes.ckpt)

## Reproducing results
```
python3 scripts/evaluate_model.py --w [path_to_model]
```

## Training

```
python3 scripts/train_model.py

```
## Tutorial and Error Explaination
link:
1-	https://nvidia.github.io/MinkowskiEngine/quick_start.html
2-	https://github.com/BVLC/caffe/issues/3599
3-	https://github.com/microsoft/DeepSpeed/issues/2684
4-	https://github.com/PRBonn/MaskPLS



1.	git clone the repository link4
2.	go to mask_pls/config/model.yaml, change line 32(path to kitti dataset), also change the “config” that is right under it, change config path to the total path to the configuration file for mask_pls to avoid directory problem(!not the configuration file for Cylinder3D, they are different)
3.	conda create --name MaskPLS python=3.9, activate it
4.	pip3 install torch, and remove torch inside requirements.txt(reason: putting torch inside requirements.txt don’t run well when pip3 install -r requirements.txt), change requirements.txt, move numpy before MinkowskiEngine, because numpy is prerequisites for MinkowskiEngine.
a.	error: No module named 'setuptools.extern.six'
reason: numpy version too old
solution: install newest numpy in console, and delete the one in requirements.txt
b.	error: Could not find a version that satisfies the requirement BLAS (from versions: none)
solution: follow link 1 to install BLAS, conda install -c intel mkl mkl-include
c.	action: install MinkowskiEngine
error: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions.
solution: pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
reason: install wrong version of torch for cuda
d.	action: install MinkowskiEngine
error: look at the middle of the output message, if it says it cannot find ninja, then pip install, the output message looks like this
/home/student/anaconda3/envs/MaskPLS/lib/python3.9/site-packages/torch/utils/cpp_extension.py:476: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.. Falling back to using the slow distutils backend.
warnings.warn(msg.format('we could not find ninja.'))
e.	action: 
error: cblas.h: No such file or directory
solution: sudo apt-get install libopenblas-dev, see link 2

conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
# CUDA 11.7


error: fatal error: cusolverDn.h: No such file or directory
         10 | #include <cusolverDn.h>
reason:
solution: export PATH=/usr/local/cuda/bin:$PATH, check link 3


then install MinkowskiEngine using command pip3 install -U git+https://github.com/NVIDIA/MinkowskiEngine, don’t use other command

problem: when try to run python3 “scripts/train_model.py”
error: ModuleNotFoundError: No module named 'mask_pls'
reason: working directory is different
solution: import sys package, and append directory to a variable.

run “python3 scripts/train_model.py” to avoid directory error, note that we need to go to directory “scripts” and run this command.

problem: No such file or directory: '/home2/student/2DPASS/dataset/sequences/00/calib.txt'
reason: we also need to go to website link4 and download ‘KITTI Odometry Benchmark calibration data’
solution: download the file and put zip file in the same directory as “dataset” (not inside), and unzip it.

change N_GPUS from -1 to 1 in config/model.yaml



## Citation
```bibtex
@article{marcuzzi2023ral,
  author = {R. Marcuzzi and L. Nunes and L. Wiesmann and J. Behley and C. Stachniss},
  title = {{Mask-Based Panoptic LiDAR Segmentation for Autonomous Driving}},
  journal = ral,
  volume = {8},
  number = {2},
  pages = {1141--1148},
  year = 2023,
  doi = {10.1109/LRA.2023.3236568},
  url = {https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/marcuzzi2023ral.pdf},
}
```
## Licence
Copyright 2023, Rodrigo Marcuzzi, Cyrill Stachniss, Photogrammetry and Robotics Lab, University of Bonn.

This project is free software made available under the MIT License. For details see the LICENSE file
