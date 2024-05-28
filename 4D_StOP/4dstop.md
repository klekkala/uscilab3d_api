# 4D-StOP

Read the reference repository [here][repo].

### Repository

Download the above [repository][repo]. You can clone it or download a ZIP file.

### Environment

The repository has a ```requirements.txt``` file. You can create a conda environment by using ```conda create --name <env> --file requirements.txt```. If this doesn't work you can still download packages from pip and conda manually.

Make sure the ```protobuf``` package is at version 3.20.X or lower, otherwise the training program will not work. If downloading ```protobuf``` with the command ```pip install protobuf``` doesn't work, you can download the package using conda by running the command ```conda install anaconda::protobuf```.

Install sympy using ```pip install sympy```. This is not listed in ```requirements.txt``` but is required for training.

There is also a ```pointnet2=0.0.0``` requirement. We will install this later.

### Dataset

Dowload the SemanticKITTI dataset [here][kitti].
There are three zip files to download: [Velodyne point clouds][velodyne] (80 GB, requires email), [Calibration data][calib] (1 MB, requires email), and label data (179 MB).

After downloading the velodyne dataset and extracting from the zip file, you should see a folder named ```dataset```. Put this folder in the repository you just downloaded.

After downloading the calibration and label data and extracting from the zip file, you should see a folder named ```dataset```. Go to this folder, then the ```sequences``` folder, and there are 22 folders named ``00`` to ``21``. ```dataset``` also has these folders. Inside these folders are the files ```calib.txt``` and ```times.txt``` (for the calibration data) and ```poses.txt``` and ```labels``` folder (for the labels data). Note that only folders from ```00``` to ```10``` have the ```labels``` folder. Move all of these files to the corresponding folders in ```dataset```.

In the end your ```dataset``` folders from ``00`` to ``10`` should look like this (copied from the original repo):
```sh
dataset
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

Now, you need to get the ```semantic-kitti.yaml``` file. I uploaded this file in the same folder that this markdown file is located in. Put this file inside the ```dataset``` folder.

After this, go to ```utils/create_center_label.py``` and edit line 10. The path should be to your ```dataset``` folder. Include the ```dataset``` folder in the path. For example: ```home/4dstop/dataset```.
Next, run ```python utils/create_center_label.py``` to generate additional labels.

Final dataset folder structure:
```sh
dataset
├── semantic-kitti.yaml
└── sequences
    └── 00
        ├── poses.txt
        ├── calib.txt
        ├── times.txt
        └── labels
            ├── 000000.label
            ├── 000000.center.npy
            ...
        └── velodyne
            ├── 000000.bin
            ...
   ...
  ```
  
### Installations

Run the following commands:
```sh
cd cpp_wrappers
sh compile_wrappers.sh
```

Before installing pointnet2, we need to make sure it can read all the header files. Sometimes it is unable to read the header files in the ```pointnet2/_ext_src/include``` folder. To solve this, move all the files in the ```pointnet2/_ext_src/include``` folder to the ```pointnet2/_ext_src/src``` folder.

Then you can run the following commands to install pointnet2:
```sh
cd pointnet2
python setup.py install
```

### Training

Before running the training script, open the file ```train_SemanticKitti.py```. On lines 308-310, change the paths to the path of your dataset folder.
There are other paths throughout the file ```train_SemanticKitti.py``` as well. For example: ```/globalwork/kreuzberg/4D-PLS/results``` and ```/globalwork/kreuzberg/4D-PLS/test```. You can change them to the paths of the folders where you want to store the results.

To run the training script, run
```sh
python train_SemanticKitti.py
```
Edit configurations at the file ```train_SemanticKitti.py```, starting at line 279. Read the [repository][repo] for more details on training and testing.

[repo]: <https://github.com/LarsKreuzberg/4D-StOP>
[kitti]: <www.semantic-kitti.org/dataset.html#download>
[velodyne]: <https://www.cvlibs.net/download.php?file=data_odometry_velodyne.zip>
[calib]: <https://www.cvlibs.net/download.php?file=data_odometry_calib.zip>
