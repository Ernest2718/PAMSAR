'''
Ernest Lee Mitchell
Wright State University
July 25, 2025
'''

# Import libraries.
import os
import glob
from scipy.io import loadmat
import Data_Load
 
def load_MSTAR_data(base_directory):
    """
    Loads all .mat files found within a base directory and its subdirectories.

    Args:
        base_directory (str): The path to the main directory to start searching from.

    Returns:
        dict: A dictionary where keys are the full paths of the .mat files
              and values are the loaded content of each .mat file.
    """
    mat_data = {}
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.mat'):
                file_path = os.path.join(root, file)
                try:
                    data = loadmat(file_path)
                    mat_data[file_path] = data
                    print(f"Loaded: {file_path}")
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
    return mat_data


# Replace 'path/to/your/base_directory' with the actual path where .mat files are located.
# Locate .mat files with real MSTAR data.
base_dir_real = r'C:/Users/mitch/Documents/SAMPLE_dataset_public-master/SAMPLE_dataset_public-master/mat_files/real'
real_mat = load_MSTAR_data(base_dir_real)
# Locate .mat files with synthetic MSTAR data.
base_dir_synth = r'C:/Users/mitch/Documents/SAMPLE_dataset_public-master/SAMPLE_dataset_public-master/mat_files/synth'
synth_mat = load_MSTAR_data(base_dir_real)