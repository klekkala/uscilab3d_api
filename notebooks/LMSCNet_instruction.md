# LMSCNet_instruction

This is an simple instructional guide for using [LMSCNet](https://github.com/astra-vision/LMSCNet) code.

## Preparation

### Prerequisites and Setup
Firstly, gitclone the code. Then, you can refer to the Prerequirements and Setup section displayed in the original github repository address to create the environment. Please refer to the original repository for this section.

### Dataset

According to the guidelines of the original code repository, preprocess your dataset to generate lower scale labels for LMSCNet code. You can get some ```file.label_1_X``` and ```file.invalid_1_X``` file.

```bash
$ cd <root dir of this repo>
$ python LMSCNet/data/labels_downscale.py --dset_root <path/dataset/root>
```

Add the original dataset to form the following directory structure. In the training and validation sets, the program will read ```3D-LABEL ('*.label', '*.invalid', '*.label_1_2', '*.invalid_1_2', '*.label_1_4', '*.invalid_1_4', '*.label_1_8', '*.invalid_1_8')``` and ```3D-OCCLUDED ('*.included')```, while the test set will read ```3D-OCCUPANCY ('*.bin')```

```
dataset/
└── sequences/
    ├── 00/
    │ └── voxels/
    │   └── 000000.bin
    │   └── 000000.invalid
    │   └── 000000.invalid_1_2
    │   └── 000000.invalid_1_4
    │   └── 000000.invalid_1_8
    │   └── 000000.label
    │   └── 000000.label_1_2
    │   └── 000000.label_1_4
    │   └── 000000.label_1_8
    │   └── 000000.occluded
    ...
    ├── 07/
    │ └── voxels/
    ├── 08/
    │ └── voxels/
    ├── 09/
    │ └── voxels/
    ├── 10/
    │ └── voxels/
    ├── 11/
    │ └── voxels/
    │   └── 000000.bin
    ...
    ├── 20/
    │ └── voxels/
    └── 21/
    └── voxels/
```

Please note the distribution of training, validation, and testing sets in the above directory.

```python
split = {'train': [0, 1, 2, 3, 4, 5, 6, 7, 9, 10], 'val': [8],
'test': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]}
```

### Conifg

Find ```SSC_configs/config_routine.py``` to modify your config. For example, change your dataset and output path by change ```config_dict['DATASET']['ROOT_DIR']``` and ```config_dict['OUTPUT']['OUT_ROOT']``` to fit your running script.

## Running

Please refer to the original code repository [LMSCNet](https://github.com/astra-vision/LMSCNet) for details. 

### Train

LMSCNet
```bash
$ cd <root dir of this repo>
$ python LMSCNet/train.py --cfg SSC_configs/examples/LMSCNet.yaml --dset_root <path/dataset/root>
```

LMSCNet-SS
```bash
$ cd <root dir of this repo>
$ python LMSCNet/train.py --cfg SSC_configs/examples/LMSCNet_SS.yaml --dset_root <path/dataset/root>
```

### Baseline
```bash
$ python LMSCNet/train.py --cfg SSC_configs/examples/SSCNet.yaml --dset_root <path/dataset/root>
$ python LMSCNet/train.py --cfg SSC_configs/examples/SSCNet_full.yaml --dset_root <path/dataset/root>
```

### Validating 
```bash
$ cd <root dir of this repo>
$ python LMSCNet/validate.py --weights </path/to/model.pth> --dset_root <path/dataset/root>
```

### Testing
```bash
$ cd <root dir of this repo>
$ python LMSCNet/test.py --weights </path/to/model.pth> --dset_root <path/dataset/root> --out_path <predictions/output/path>
```