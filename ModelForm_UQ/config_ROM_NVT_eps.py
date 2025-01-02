import numpy as np
import os
import pandas as pd
from scipy.linalg import svd
import matplotlib.pyplot as plt
import scipy.io as sio
import shutil

trunc_err = '1e-3'
Nr_Lst = [590, 599, 808, 772, 385, 364, 372]
gamma_Lst = ['1e-0', '1e-1', '1e-2', '1e-3', '1e-4', '1e-5', '0']

ROM_NVT_dir = os.getcwd() + f"/rom_data_15ps/ROM_NVT_{trunc_err}/"
# if does not exist, create the directory
if not os.path.exists(ROM_NVT_dir):
    os.makedirs(ROM_NVT_dir)

# create directory for each gamma in gamma_Lst
for gamma, Nr in zip(gamma_Lst, Nr_Lst):
    gamma_dir = ROM_NVT_dir + f"gamma_{gamma}/"

    # data_SPECIFY_ROM
    data_SPECIFY_ROM_dir = os.getcwd() + "/data_SPECIFY_ROM/"

    target_ROB_dir = os.getcwd() + f"/fom_data_15ps/robdata_{trunc_err}/"
    if not os.path.exists(gamma_dir):
        os.makedirs(gamma_dir)
        # Create a Global directory containing the potentials directory
        global_dir = gamma_dir + "Global/"
        if not os.path.exists(global_dir):
            os.makedirs(global_dir)

            target_Global_dir = target_ROB_dir + f"Global/"
            # have a subdirectory for each potential
            for potential in ['NEP', 'MLIP']:
                potential_dir = global_dir + f"{potential}/"
                if not os.path.exists(potential_dir):
                    os.makedirs(potential_dir)

                # copy the rob from the target directory
                rob_target = target_Global_dir + f"rob_trunc_{Nr}_{gamma}.txt"
                os.system(f"cp {rob_target} {potential_dir}")
                # in the same folder copy all the other files from data_SPECIFY_ROM_dir
                for filename in os.listdir(f"{data_SPECIFY_ROM_dir}/Global/{potential}"):
                    shutil.copy(f"{data_SPECIFY_ROM_dir}/Global/{potential}/{filename}", potential_dir)

                # Modify the in.lammps file
                in_lammps_path = os.path.join(potential_dir, 'in.lammps')
                if os.path.exists(in_lammps_path):
                    with open(in_lammps_path, 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        # More robust check for the line to change
                        if "fix" in line and "nvt/rom" in line and "model X rob_trunc_X_X.txt" in line:
                            lines[i] = f"fix             1 all nvt/rom temp $t $t 0.1 model {Nr} rob_trunc_{Nr}_{gamma}.txt\n"

                    with open(in_lammps_path, 'w') as file:
                        file.writelines(lines)

        # create subdirectories for each potential
        for potential in ['NEP', 'MLIP']:
            potential_dir = gamma_dir + f"{potential}/"
            if not os.path.exists(potential_dir):
                os.makedirs(potential_dir)

            # copy the rob from the target directory
            rob_target = target_ROB_dir + f"{potential}/rob_trunc_{Nr}_{gamma}.txt"
            os.system(f"cp {rob_target} {potential_dir}")
            # in the same folder copy all the other files from data_SPECIFY_ROM_dir
            for filename in os.listdir(f"{data_SPECIFY_ROM_dir}/{potential}"):
                shutil.copy(f"{data_SPECIFY_ROM_dir}/{potential}/{filename}", potential_dir)

            # Modify the in.lammps file
            in_lammps_path = os.path.join(potential_dir, 'in.lammps')
            if os.path.exists(in_lammps_path):
                with open(in_lammps_path, 'r') as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    # More robust check for the line to change
                    if "fix" in line and "nvt/rom" in line and "model X rob_trunc_X_X.txt" in line:
                        lines[i] = f"fix             1 all nvt/rom temp $t $t 0.1 model {Nr} rob_trunc_{Nr}_{gamma}.txt\n"

                with open(in_lammps_path, 'w') as file:
                    file.writelines(lines)
print("Done!")
            
