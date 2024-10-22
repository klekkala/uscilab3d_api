import numpy as np
import struct
import open3d as o3d
from itertools import zip_longest
import os
from collections import Counter

def take_value(x, y):
    # get 32 bits
    label_id = int(x[0])
    instance_id = int(y[0])

    # handle for case where instance id == -1
    if instance_id == -1 or instance_id > 50000:
        instance_id = 0

    # Convert decimal to binary (32 bits)
    binary_label_id = bin(label_id)[2:].zfill(16)
    binary_instance_id = bin(instance_id)[2:].zfill(16)

    binary_comb = binary_instance_id + binary_label_id

    #print("32-bit binary representation:", binary_comb)
    if len(binary_comb) != 32:
        print("comb: ", binary_comb)
        print("x: ", x)
        print("y: ", y)
        raise ValueError("The binary string must be exactly 32 bits long")

    # Convert the binary string to an integer
    integer_value = int(binary_comb, 2)
    return integer_value

# Specify the file path
def write_labels(comb, output_file_path):
    with open(output_file_path, 'wb') as file:
        # Apply the function to each element using list comprehension
        #obj_value_array = np.array([take_value(x) for x in comb[0]])
        obj_value_array = np.array([take_value(x,y) for x, y in zip(comb[0], comb[1])])

        # Iterate over each unsigned integer in the array
        for uint32_value in obj_value_array:
            # Pack the integer into 4 bytes (32 bits) in big-endian order
            packed_bytes = struct.pack('I', uint32_value)
            # Write the packed bytes to the file
            file.write(packed_bytes)

seq_id = 0
folder_name = "2023_07_11"
pcd_path = "/lab/tmpig10c/NIPS_DATA/"+folder_name+"/"
input_pcd_directory = pcd_path + str(seq_id)
output_bin_directory = "./dataset/"+folder_name+"/"+str(seq_id)+"/labels"
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
                objs = pcd.point.obj_id.numpy()
                insta_id = pcd.point.instance_id.numpy()

                # Write the array to a binary file
                binary_file_path = os.path.join(output_bin_directory, str(file_id) + '.label')
                comb = [objs, insta_id]
                write_labels(comb, binary_file_path)
            file_id += 1

