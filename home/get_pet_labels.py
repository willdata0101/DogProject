#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Will
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    path = image_dir
    in_files = path.splitext(path)
    results_dic = dict()
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_label = ""
            low_in_files = in_files[idx].lower()
            word_list_in_files = low_in_files.split("_")
            for word in word_list_in_files:
                if word.isalpha():
                    pet_label += word + " "
            pet_label = pet_label.strip()
            
            if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
            
        else:
            print("** Warning: Key=", filenames[idx], "already exists in results_dic with value =", results_dic[filenames[idx]])
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, " Pet Label=", results_dic[key][0])
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
