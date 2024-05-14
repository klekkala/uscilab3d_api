GitHub link:
https://github.com/astra-vision/LMSCNet

config can be changed in:
SSC_configs/config_routine.py

dataset needed to be downloaded
https://www.rocq.inria.fr/rits_files/computer-vision/lmscnet/semanticKITTI_v1.1_dscale.zip

data preprocess
python LMSCNet/data/labels_downscale.py --dset_root /home2/tmp/kiran/2DPASS/

training
python LMSCNet/train.py --cfg SSC_configs/examples/LMSCNet.yaml --dset_root /home2/tmp/kiran/2DPASS/

the model will be saved under /home/student/semantic_scene/SSC_out, the parameter setting is in /home/student/semantic_scene/LMSCNet/SSC_configs

validate
python LMSCNet/validate.py --weights ../LMSCNet.pth --dset_root /home2/tmp/kiran/2DPASS/
