import numpy as np
import sys
import os
import argparse
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy
import scipy.stats
import seaborn as sns


def msd_singAtom(x_i, y_i, z_i):
    msd = np.zeros((len(x_i), 2))
    for i in range(len(x_i)):
        for j in range(i + 1, len(x_i)):
            msd[j - i, 0] += (x_i[i] - x_i[j]) ** 2 + (y_i[i] - y_i[j]) ** 2 + (z_i[i] - z_i[j]) ** 2
            msd[j - i, 1] += 1
    return np.divide(
        msd[:, 0], 
        msd[:, 1], 
        out=np.zeros_like(msd[:, 0]), 
        where=msd[:, 1] != 0,
    )


def vec_msd_singAtom(x_i, y_i, z_i):
    n = len(x_i)
    # Create an array to hold the MSD values
    msd = np.zeros(n)
    count = np.zeros(n)
    
    # Calculate the MSD using vectorized operations
    for t in range(1, n):
        x_disp = x_i[:-t] - x_i[t:]
        y_disp = y_i[:-t] - y_i[t:]
        z_disp = z_i[:-t] - z_i[t:]
        squared_displacements = x_disp ** 2 + y_disp ** 2 + z_disp ** 2
        msd[t] = np.sum(squared_displacements)
        count[t] = len(squared_displacements)
    
    # Compute the average MSD
    result = np.divide(msd, count, out=np.zeros_like(msd), where=count != 0)
    
    return result


def compute_msd(x, y, z):
    numAtoms, numTS = x.shape
    msdRunTot = np.zeros(numTS)

    for i in range(numAtoms):
        msdRunTot += vec_msd_singAtom(x[i, :], y[i, :], z[i, :])
    msdAvg = msdRunTot / numAtoms

    return msdAvg