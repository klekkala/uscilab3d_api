import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import imageio
from PIL import Image


# A path to a T1-weighted brain .nii image:
#t1_fn = '/content/drive/MyDrive/3d_semantic_segmentation/raw_dataset/test/ct/volume-0.nii'
#t1_fn = '/home/student/3duNet/raw_dataset/test/label/segmentation-99.nii'
t1_fn = '/home/student/3duNet/3duNet_main/output_graph/result-99.nii'

# Read the .nii image containing the volume with SimpleITK:
sitk_t1 = sitk.ReadImage(t1_fn)

# and access the numpy array:
t1 = sitk.GetArrayFromImage(sitk_t1)

print("shape of the segmentation data: ", t1.shape)

frame_list = []
for frame_id in range(t1.shape[0]):
    frame = Image.fromarray(np.uint8(t1[frame_id] * 255) , 'L')
    frame_list.append(frame)

frame_list[0].save('origin.gif', save_all=True, append_images=frame_list[1:-1])
