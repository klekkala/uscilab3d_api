# MF-MOS data preprocessing

Read the reference repository [here][repo].

## Specs

My environment is Ubuntu 20.04 and CUDA 11.8. The repository says Ubuntu 18.04 and CUDA 11.2 works.

## Repository

Download the above [repository][repo]. You can clone it or download a ZIP file. 

## Dataset

Dowload the SemanticKITTI dataset [here][kitti].
There are three zip files to download: [Velodyne point clouds][velodyne] (80 GB, requires email), [Calibration data][calib] (1 MB, requires email), and label data (179 MB).

After downloading the velodyne dataset and extracting from the zip file, you should see a folder named ```dataset```. Rename this folder to ```DATAROOT``` and put this folder in the repository you just downloaded.

After downloading the calibration and label data and extracting from the zip file, you should see a folder named ```dataset```. Go to this folder, then the ```sequences``` folder, and there are 22 folders named ``00`` to ``21``. ```DATAROOT``` also has these folders. Inside these folders are the files ```calib.txt``` and ```times.txt``` (for the calibration data) and ```poses.txt``` and ```labels``` folder (for the labels data). Note that only folders from ```00``` to ```10``` have the ```labels``` folder. Move all of these files to the corresponding folders in ```DATAROOT```.

In the end your ```DATAROOT``` folders from ``00`` to ``10`` should look like this (copied from the original repo):
```sh
DATAROOT
└── sequences
    ├── 00
    │   ├── poses.txt
    │   ├── calib.txt
    │   ├── times.txt
    │   ├── labels
    │   └── velodyne
   ...
   ```
   
Folders from ``11`` to ``21`` should look the same except without the ```labels``` folder.

### Preprocessing

You can create the conda environment:
```sh
conda env create -f environment.yml
conda activate mfmos
```
This will install packages and their versions needed for preprocessing and training.

Before preprocessing, in the ```utils``` folder, open the file ```auto_gen_residual_images.py```. On line 156, add the code
```sh
residual_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 19, 22]
```
We need to do this because the original ```residual_list``` does not match the residuals used in the training script.

After doing so, run
```sh
python utils/auto_gen_residual_images.py
```

After this script is finished, the DATAROOT folder should look like this (copied from the original repo):
```sh
DATAROOT
└── sequences
    ├── 00
    │   ├── poses.txt
    │   ├── calib.txt
    │   ├── times.txt
    │   ├── labels
    │   ├── residual_images_1
    │   ├── residual_images_10
    │   ├── residual_images_11
    │   ├── residual_images_13
    │   ├── residual_images_15
    │   ├── residual_images_16
    │   ├── residual_images_19
    │   ├── residual_images_2
    │   ├── residual_images_22
    │   ├── residual_images_3
    │   ├── residual_images_4
    │   ├── residual_images_5
    │   ├── residual_images_6
    │   ├── residual_images_7
    │   ├── residual_images_8
    │   ├── residual_images_9
    │   └── velodyne
   ...
  ```

### Training

Before running the training script, in the folder ```script```, open the file ```dist_train.sh```. On line 8 there is the code
```sh
export CUDA_VISIBLE_DEVICES=0,1
```
If you only have 1 GPU in your device, change it to
```sh
export CUDA_VISIBLE_DEVICES=0
```
If you have multiple GPUs in your device, change it so that the GPUs you want to use are listed.

To run the training script, run
```sh
bash script/dist_train.sh
```

[repo]: <https://github.com/SCNU-RISLAB/MF-MOS>
[kitti]: <www.semantic-kitti.org/dataset.html#download>
[velodyne]: <https://www.cvlibs.net/download.php?file=data_odometry_velodyne.zip>
[calib]: <https://www.cvlibs.net/download.php?file=data_odometry_calib.zip>
