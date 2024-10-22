import pandas as pd
import numpy as np
import struct
import open3d as o3d
from itertools import zip_longest
import os
from collections import Counter

def write_float_to_binary_file(merged_list, filename):
    merged_list.tofile(filename)

def write_bin_file(coord,intensity,file_name):

    # Define the output bin file path
    #output_bin_file_path = '/content/drive/MyDrive/USC/Lab/3d_semantic/new_data/velodyne/' + str(id) + '.bin'

    # Merging the lists by appending elements of b to the corresponding sublists in a
    merged_array = np.array([np.concatenate((sub_a, sub_b)) for sub_a, sub_b in zip(coord, intensity)])
    #print("length of merged array", merged_array.shape)
    # Write the numpy array to a binary file
    write_float_to_binary_file(merged_array, file_name)

seq_id = 0
folder_name = "2023_07_11"
pcd_path = "/lab/tmpig10c/NIPS_DATA/"+folder_name+"/"
input_pcd_directory = pcd_path + str(seq_id)
output_bin_directory = "./dataset/"+folder_name+"/"+str(seq_id)+"/velodyne"
file_id = 0

# Loop through all directories and subdirectories
for root, _, files in os.walk(input_pcd_directory):
    # Loop through all files in the current directory
    for file in files:
        # Check if the file ends with ".pcd"
        if file.endswith(".pcd"):
            file_path = os.path.join(root, file)
            print("processing file: ", file_path)

            # Add your code to process the .pcd file here
            with open(file_path, 'r') as file:
                pcd = o3d.t.io.read_point_cloud(file_path)
                intensity = pcd.point.intensity.numpy()
                #objs = pcd.point.obj_id.numpy()
                #insta_id = pcd.point.instance_id.numpy()
                pcd = pcd.point.positions.numpy()

                #print("pcd shape: ", pcd.shape)
                # Write the array to a binary file
                binary_file_path = os.path.join(output_bin_directory, str(file_id) + '.bin')
                write_bin_file(pcd, intensity, binary_file_path)
            file_id += 1
