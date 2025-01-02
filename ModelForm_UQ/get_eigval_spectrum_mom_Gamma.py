import numpy as np
import os
import pandas as pd
from scipy.linalg import svd
import matplotlib.pyplot as plt
import scipy.io as sio

# Simulation parameters
dt_sim = 0.002
ss_per_ts = 1
dt_ss = dt_sim * ss_per_ts
total_ts = 7500
num_ss = total_ts // ss_per_ts + 1
print(f'dt_ss = {dt_ss}')
print(f'num_ss = {num_ss}')

# Tolerance for SVD
tol = 1e-3
label_tol = '1e-3'
# weightCoeffSym = 1e-5
# label_weightCoeffSym = '1e-5'

weightCoeffSym_lst = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 0]
label_weightCoeffSym_lst = ['1e-0', '1e-1', '1e-2', '1e-3', '1e-4', '1e-5', '0']

data_folder = f"/fom_data_15ps/robdata_{label_tol}/"

# Change your root here:
root = os.getcwd() + data_folder

logFilename = os.path.join(root, 'logidx_gamma.txt')

# Load the log file
if os.path.exists(logFilename):
    logFile = pd.read_csv(logFilename, delim_whitespace=True, header=None, names=['Var1', 'Var2', 'Var3'])
    tolLog = logFile['Var1'].values
    weightCoeffSymLog = logFile['Var2'].values
    idxLog = logFile['Var3'].values

else:
    tolLog = []
    idxLog = []


# Iterate over each weight coefficient
for weightCoeffSym, label_weightCoeffSym in zip(weightCoeffSym_lst, label_weightCoeffSym_lst):
    print(f'Running simulation with weightCoeffSym = {weightCoeffSym}')

    mass_lst = [22.9897692800, 121.7600000000, 78.9600000000]
    numAtoms = 1016

    # Initialization
    rel_err_SVD_lst = []
    rob_lst = []
    qp_lst = []

    # Potential labels
    pot_label_lst = ['NEP', 'MLIP']

    # Process each potential
    for pot in pot_label_lst:
        print(f'Curr pot: {pot}')
        filepath_FOM = os.path.join(os.getcwd(), 'fom_data_15ps', pot)
        mat_q = sio.loadmat(os.path.join(filepath_FOM, 'ss_q.mat'))
        ss_q_dis = mat_q['ss_q_dis']
        print("Shape of ss_q_dis: ", ss_q_dis.shape)

        mat_v = sio.loadmat(os.path.join(filepath_FOM, 'ss_v.mat'))
        ss_v = mat_v['ss_v']
        print("Shape of ss_v: ", ss_v.shape)

        ss_p = ss_v.copy()

        # x-mom
        ss_p[0:376, :] = ss_p[0:376, :] * mass_lst[0]
        ss_p[376:504, :] = ss_p[376:504, :] * mass_lst[1]
        ss_p[504:numAtoms, :] = ss_p[504:numAtoms, :] * mass_lst[2]
        # y-mom
        ss_p[0+numAtoms:376+numAtoms, :] = ss_p[0+numAtoms:376+numAtoms, :] * mass_lst[0]
        ss_p[376+numAtoms:504+numAtoms, :] = ss_p[376+numAtoms:504+numAtoms, :] * mass_lst[1]
        ss_p[504+numAtoms:numAtoms*2, :] = ss_p[504+numAtoms:numAtoms*2, :] * mass_lst[2]
        # z-mom
        ss_p[0+numAtoms*2:376+numAtoms*2, :] = ss_p[0+numAtoms*2:376+numAtoms*2, :] * mass_lst[0]
        ss_p[376+numAtoms*2:504+numAtoms*2, :] = ss_p[376+numAtoms*2:504+numAtoms*2, :] * mass_lst[1]
        ss_p[504+numAtoms*2:numAtoms*3, :] = ss_p[504+numAtoms*2:numAtoms*3, :] * mass_lst[2]


        if weightCoeffSym != 0:
            ss_p *= weightCoeffSym
            qp_arr = np.hstack((ss_q_dis, ss_p))  # Concatenate only if weightCoeffSym is not 0
            num_ss_scale = 2
        else:
            qp_arr = ss_q_dis.copy()  # Use only displacement data if weightCoeffSym is 0
            num_ss_scale = 1

        # append to qp_lst
        qp_lst.append(qp_arr)
        print("Shape of qp_arr: ", qp_arr.shape)

        # Centering ss_q_dis, minus mean
        qp_c = qp_arr - np.mean(qp_arr, axis=1, keepdims=True)

        # Singular Value Decomposition
        U, S, V = svd(qp_c, full_matrices=False)
        S = (S**2) * (1 / (num_ss*num_ss_scale - 1))

        rob_lst.append(U)
        rel_err_SVD = 1 - (np.cumsum(S) / np.sum(S))
        rel_err_SVD_lst.append(rel_err_SVD)

        idx = np.where(rel_err_SVD < tol)[0][0]
        print(f'idx = {idx}')
        print(f'rel_err_SVD[idx] = {rel_err_SVD[idx]}')
        print(' ')

    # Global singular value decomposition
    qp_global = np.hstack(qp_lst)
    print("Shape of qp_global: ", qp_global.shape)
    qp_global_c = qp_global - np.mean(qp_global, axis=1, keepdims=True)
    robGlobal, S, V = svd(qp_global_c, full_matrices=False)
    rob_lst.append(robGlobal)
    S = (S**2) * (1 / (num_ss*num_ss_scale - 1))
    rel_err_SVD_global = 1 - (np.cumsum(S) / np.sum(S))
    rel_err_SVD_lst.append(rel_err_SVD_global)
    idx = np.where(rel_err_SVD_global < tol)[0][0]
    print('Global')
    print(f'idx = {idx}')
    print(f'rel_err_SVD[idx] = {rel_err_SVD_global[idx]}')
    print(' ')

    # # Plotting
    # colors = ['b', 'g', 'r']
    # plt.figure()
    # for i, rel_err_SVD in enumerate(rel_err_SVD_lst):
    #     linestyle = '-' if i < len(pot_label_lst) else '--'
    #     plt.plot(rel_err_SVD, linestyle=linestyle, linewidth=1.5, color=colors[i])
    # plt.gca().set_yscale('log')
    # plt.xlabel('Rank r')

    # plt.ylabel('epsilon (log scale)')
    # plt.grid(True)
    # plt.legend(pot_label_lst + ['Global'], loc='best')
    # plt.savefig(f'data_{label_tol}/figs/rel_err_SVD_{weightCoeffSym}.png')
    # # plt.show()

    # Add Global to the list
    pot_label_lst.append('Global')

    # now align the signs of Vr_lst_sel with Vr_lst_sel[-1]
    U_g = rob_lst[-1]

    for idx_rob in range(len(rob_lst) - 1):
        Ur_idx = rob_lst[idx_rob]
        for j in range(Ur_idx.shape[1]):
            dist1 = np.linalg.norm(U_g[:, j] - Ur_idx[:, j])
            dist2 = np.linalg.norm(U_g[:, j] + Ur_idx[:, j])
            if dist2 < dist1:
                rob_lst[idx_rob][:, j] = -rob_lst[idx_rob][:, j]

            
    # Truncation and saving the Global idx
    # print(f"Truncating to idx = {idx}")
    n = idx + 1         # number of basis to keep
    print(f'Number of basis retained: {n}')

    for i, pot in enumerate(pot_label_lst):
        rob_trunc = rob_lst[i][:, :n]
        filepath = os.path.join(root, pot)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        # print("filepath_FOM: ", filepath_FOM)
        filename = os.path.join(filepath, f'rob_trunc_{n}_{label_weightCoeffSym}.txt')
        np.savetxt(filename, rob_trunc, fmt='%.16f', delimiter=' ')
        print(f'rob_trunc_centered {n} saved for {pot}')

    with open(logFilename, 'a') as fid:
        fid.write(f'{tol:.16f} {weightCoeffSym} {n}\n')

    print('Done with weightCoeffSym = ', weightCoeffSym)
    print(' ')

print('All done!')