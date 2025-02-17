# Based on Code written by JHL and KN

import os
import tkinter as tk
from tkinter import filedialog
import glob
from natsort import natsorted, ns


## Returns single file

def select_single_file(runme_Path_TWO):
    """
    :return: path for a SINGLE file
    """
    root = tk.Tk()
    root.withdraw()

    home = os.path.expanduser('~')
    #file_path = filedialog.askopenfilename(initialdir=home)
    file_path = runme_Path_TWO

    # multi_df = pd.read_csv(file_path, header=[0, 1], index_col=[0], low_memory=False)

    return file_path   # multi_df

## Returns single directory path

def select_single_dir():
    root = tk.Tk()
    root.withdraw()

    home = os.path.expanduser('~')
    dir_path = filedialog.askdirectory(initialdir=home)  ## ask_directory
    
    return dir_path


## Returns EVERY single file in the directory

def select_all_files_in_directory():
    """
    :USER INPUT: extension type --> wrong extension type will result in EMPTY list
    :return: (files_list, dir_title) --> list of all the flies within selected directory
    """

    files_list = []
    root = tk.Tk();   root.withdraw()

    #extension_type = str(input("What is the extension type in this directory? "))
    extension_type = 'txt'
    home = os.path.expanduser('~')  # returns the home directory on any OS --> ex) /Users/jhl
    selected_dir_path = filedialog.askdirectory(initialdir = home)

    file_pattern = os.path.join(selected_dir_path, "*." + extension_type)

    for file in natsorted(glob.glob(file_pattern), alg=ns.IGNORECASE):
        files_list.append(file)

    selected_dir_title = os.path.basename(selected_dir_path)

    return files_list, selected_dir_title

## Returns EVERY single file in the directory

def select_and_sort_directory_contents(runme_Path):
    """
    :USER INPUT: extension type --> wrong extension type will result in EMPTY list
    :return: (files_list, dir_title) --> list of all the flies within selected directory
    """

    files_list = []
    root = tk.Tk();   root.withdraw()

    #extension_type = str(input("What is the extension type in this directory? "))
    extension_type = 'txt'
    home = os.path.expanduser('~')  # returns the home directory on any OS --> ex) /Users/jhl
    #selected_dir_path = filedialog.askdirectory(initialdir = home)
    selected_dir_path = runme_Path  ######  Ka added this part, so path imported from RunMe
    file_pattern = os.path.join(selected_dir_path, "*." + extension_type)

    for file in natsorted(glob.glob(file_pattern), alg=ns.IGNORECASE):
        files_list.append(file)

    selected_dir_title = os.path.basename(selected_dir_path)

    return files_list, selected_dir_title

## Returns EVERY single file in the directory

def select_all_files_in_directory_works_with_RunMe(runme_Path):
    """
    :USER INPUT: extension type --> wrong extension type will result in EMPTY list
    :return: (files_list, dir_title) --> list of all the flies within selected directory
    """

    files_list = []
    root = tk.Tk();   root.withdraw()

    #extension_type = str(input("What is the extension type in this directory? "))
    extension_type = 'txt'
    home = os.path.expanduser('~')  # returns the home directory on any OS --> ex) /Users/jhl
    #selected_dir_path = filedialog.askdirectory(initialdir = home)
    selected_dir_path = runme_Path  ######  Ka added this part, so path imported from RunMe
    file_pattern = os.path.join(selected_dir_path, "*." + extension_type)

    for file in natsorted(glob.glob(file_pattern), alg=ns.IGNORECASE):
        files_list.append(file)

    selected_dir_title = os.path.basename(selected_dir_path)

    return files_list, selected_dir_title