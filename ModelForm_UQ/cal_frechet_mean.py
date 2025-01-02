import sys
import os
# sys.path.append(os.path.abspath(os.path.join('..')))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import expm, logm
from utils import Stiefel_Exp_Log as SEL
from utils import stiefel as stf
import time
seed = 41

# PRINT LOGGING DATE AND TIME
print(" ######################################################### ")
print("Script started at: ")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(" ######################################################### ")
start_time = time.time()

print(os.getcwd())

################# Parameters of ROB TO TWEAK #################
Nd = 1016 * 3
numSamples = 1000
trunc_err = '1e-6'

# #### gamma== 0 ####
# gamma = '0'
# Nr = 784
# NrLF_err = '1e-5'
# NrLF = 606
# NrHF = 178
# ######################

#### gamma== 1e-5 ####
gamma = '1e-5'
Nr = 983
NrLF_err = '1e-5'
NrLF = 622
NrHF = 361
######################

# robFile = "robSamples.npy"            # robSamples.npy or stiefel_samples_HF.npy
robFile = "stiefel_samples_HF.npy"
###########################################################

potentialLst = ['NEP', 'MLIP']
datafolderpath = f"{os.getcwd()}/fom_data_15ps/robdata_{trunc_err}"
# load ROB
globalFile = f"{datafolderpath}/Global/rob_trunc_{Nr}_{gamma}.txt"
robGlobal = np.loadtxt(globalFile, delimiter=' ')
print("robGlobal shape: ", robGlobal.shape)
robGlobalLF = robGlobal[:, :NrLF]
print("robGlobalLF shape: ", robGlobalLF.shape)
robGlobalHF = robGlobal[:, NrLF:]
print("robGlobalHF shape: ", robGlobalHF.shape)

# load individual ROBs
robLst = []
robHFLst = []
robLFLst = []

for potential in potentialLst:
    # robFile = "{}/{}/rob.{}_run".format(datafolderpath, potential, potential.lower())
    robFile_path =f"{datafolderpath}/{potential}/rob_trunc_{Nr}_{gamma}.txt"
    # read the file for all rows
    rob = np.loadtxt(robFile_path, delimiter=' ', max_rows=Nd)
    # check the number of columns
    if rob.shape[1] < Nr:
        print(f"Warning: The data has only {rob.shape[1]} columns, but you're trying to load {Nr} columns.")
    robLst.append(rob)
    robLF = rob[:, :NrLF]
    robLFLst.append(robLF)
    robHF = rob[:, NrLF:]
    robHFLst.append(robHF)
    print(f"{potential} Nr, NrLF, NrHF: ", rob.shape[1], robLF.shape[1], robHF.shape[1])

print(" ")
print("Appending robGlobal to the list...")
robLst.append(robGlobal)
robHFLst.append(robGlobalHF)
robLFLst.append(robGlobalLF)
print("Number of potentials: ", len(robLst))
print(" ")

if robFile == "robSamples.npy":
    robAnchor = robLst
    savebackLabel = "robSamples"

elif robFile == "stiefel_samples_HF.npy":
    robAnchor = robHFLst
    savebackLabel = "stiefel_samples_HF"
else:
    raise ValueError("robFile must be either robSamples.npy or stiefel_samples_HF.npy")

# randomizationDir = f"{os.getcwd()}/Randomization_eps{trunc_err}_gam{gamma}"
randomizationDir = f"{os.getcwd()}/Rand15ps_eps{trunc_err}/gamma_{gamma}"
dataDir = f"{randomizationDir}/localization/data_LFeps{NrLF_err}_NrLF{NrLF}_NrHF{NrHF}/multi-potential-{numSamples}"


stiefel_samples = np.load(f'{dataDir}/{robFile}')
print("stiefel_samples shape: ", stiefel_samples.shape)

print("Shape of a robAnchor element: ", robAnchor[0].shape)

frechet_mean, errs = stf.calc_frechet_mean_mat(stiefel_samples, robAnchor[-1], eps=1e-2, tau=1e-3)
print("frechet_mean: \n", frechet_mean)
print("errs: \n", errs)

# save frechet mean
np.save(f"{dataDir}/frechet_mean_{savebackLabel}.npy", frechet_mean)

print('All done!')

end_time = time.time()
time_taken = end_time - start_time

# Print the time taken
print(f"Time taken: {time_taken} seconds")
print("Data saved successfully!")
print(" ")
print("Script ended at: ")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(" ")
