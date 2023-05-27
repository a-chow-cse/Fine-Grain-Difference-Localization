import os
import torch
import numpy as np
import matplotlib.pyplot as plt



#program to run .match.py with our defined pair files, outputs npz file with visualtion image
def run_match():
    path=os.path.abspath(os.getcwd())+"/Experiment4/Pairs_text/"
    print("pair file path: ",path)
    
    for file in os.scandir(path):
        instruction="./match_pairs.py --resize 1600 --superglue outdoor --max_keypoints 2048 --nms_radius 3  --resize_float \
            --input_dir ./ButterFly --input_pairs Experiment4/Pairs_text/"+file.name+" --output_dir " +"Experiment4/SuperGlue_output_files/"+file.name.removesuffix(".txt")
        #print(instruction)
        os.system(instruction)

if __name__ == "__main__":
    run_match()
    
