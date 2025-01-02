import os
from itertools import islice
import numpy as np
import seaborn as sns

def line2list(line, field=' ', dtype=float):
    "Convert text data in a line to data object list."
    strlist = line.strip().split(field)
    if type(dtype) != type:
        raise TypeError('Illegal dtype.')
    datalist = [dtype(i) for i in strlist if i != '']

    return datalist

palette = sns.color_palette("Spectral", 10)
alpha = 0.7
#record dft energy and forces train_set
dft_energy_train = []
dft_forces_train = []
Natoms = 128
L_max = 20
with open("train-na-2.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            dft_energy_train.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                dft_forces_train.append(line2list(next(f))[5:8])
                               
dft_energy_train = np.array(dft_energy_train)/Natoms
dft_forces_train = np.array(dft_forces_train)

mtp_energy_train = []
mtp_forces_train = []

with open("train_MTP-2.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            mtp_energy_train.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                mtp_forces_train.append(line2list(next(f))[5:8])
                                
mtp_energy_train = np.array(mtp_energy_train)/Natoms
mtp_forces_train = np.array(mtp_forces_train)

#record dft energy and forces test_set
dft_energy_test = []
dft_forces_test = []

with open("test-na-2.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            dft_energy_test.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                dft_forces_test.append(line2list(next(f))[5:8])
                               
dft_energy_test = np.array(dft_energy_test)/Natoms
dft_forces_test = np.array(dft_forces_test)

#record mtp energy and forces test_set
mtp_energy_test = []
mtp_forces_test = []

with open("test_MTP-2.cfg".format(L_max), 'r') as f:
    for line in f:
        if 'Energy' in line:
            mtp_energy_test.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                mtp_forces_test.append(line2list(next(f))[5:8])
                                
mtp_energy_test = np.array(mtp_energy_test)/Natoms
mtp_forces_test = np.array(mtp_forces_test)

#plot
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.stats import norm
import matplotlib.mlab as mlab

fig = plt.figure(figsize=(10, 4.0))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])
ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[0, 1])
#ax2 = plt.subplot(gs[1, 0])
#ax3 = plt.subplot(gs[1, 1])

ax0.scatter(dft_energy_train, mtp_energy_train, c='r', s=2.5, label='Training', alpha=alpha)
ax0.scatter(dft_energy_test, mtp_energy_test, c='b', s=2.5, label='Testing', alpha=alpha)
ax0.plot([np.amin(dft_energy_train), np.amax(dft_energy_train)],
           [np.amin(dft_energy_train), np.amax(dft_energy_train)],
           'k--',
           lw=1.0,) 

ax1.scatter(dft_forces_train, mtp_forces_train, c='r', s=2.5, label='Training', alpha=alpha)
ax1.scatter(dft_forces_test, mtp_forces_test, c='b', s=2.5, label='Testing', alpha=alpha)
ax1.plot([np.amin(dft_forces_train), np.amax(dft_forces_train)],
           [np.amin(dft_forces_train), np.amax(dft_forces_train)],
           'k--',
           lw=1.0,)


#record dft energy and forces train_set
dft_energy_train = []
dft_forces_train = []
Natoms = 127
L_max = 20
with open("train-na-1.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            dft_energy_train.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                dft_forces_train.append(line2list(next(f))[5:8])
                               
dft_energy_train = np.array(dft_energy_train)/Natoms
dft_forces_train = np.array(dft_forces_train)

mtp_energy_train = []
mtp_forces_train = []

with open("train_MTP-1.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            mtp_energy_train.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                mtp_forces_train.append(line2list(next(f))[5:8])
                                
mtp_energy_train = np.array(mtp_energy_train)/Natoms
mtp_forces_train = np.array(mtp_forces_train)

#record dft energy and forces test_set
dft_energy_test = []
dft_forces_test = []

with open("test-na-1.cfg", 'r') as f:
    for line in f:
        if 'Energy' in line:
            dft_energy_test.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                dft_forces_test.append(line2list(next(f))[5:8])
                               
dft_energy_test = np.array(dft_energy_test)/Natoms
dft_forces_test = np.array(dft_forces_test)

#record mtp energy and forces test_set
mtp_energy_test = []
mtp_forces_test = []

with open("test_MTP-1.cfg".format(L_max), 'r') as f:
    for line in f:
        if 'Energy' in line:
            mtp_energy_test.append(float(next(f)))
        if 'fx' in line:
            for i in range(Natoms):
                mtp_forces_test.append(line2list(next(f))[5:8])
                                
mtp_energy_test = np.array(mtp_energy_test)/Natoms
mtp_forces_test = np.array(mtp_forces_test)


ax0.scatter(dft_energy_train, mtp_energy_train, c='r', s=2.5, alpha=alpha)
ax0.scatter(dft_energy_test, mtp_energy_test, c='b', s=2.5, label='Testing', alpha=alpha)
ax0.plot([np.amin(dft_energy_train), np.amax(dft_energy_train)],
           [np.amin(dft_energy_train), np.amax(dft_energy_train)],
           'k--',
           lw=1.0,) 

ax1.scatter(dft_forces_train, mtp_forces_train, c='r', s=2.5, alpha=alpha)
ax1.scatter(dft_forces_test, mtp_forces_test, c='b', s=2.5, alpha=alpha)
ax1.plot([np.amin(dft_forces_train), np.amax(dft_forces_train)],
           [np.amin(dft_forces_train), np.amax(dft_forces_train)],
           'k--',
           lw=1.0,)


'''
(mu, sigma) = norm.fit(dft_energy_test - mtp_energy_test )
n, bins, patches = ax2.hist(dft_energy_test - mtp_energy_test, 100,
                            range=(-0.010, 0.010),
                            weights=np.ones_like(dft_energy_test - mtp_energy_test)/len(dft_energy_test),
                            facecolor='k',
                            alpha=0.5,
                            orientation='vertical')
y = norm.pdf(bins, mu, sigma)
ax2.plot(bins, y / sum(y), 'k--', lw=1.2)

(mu, sigma) = norm.fit(dft_forces_test[:,1] - mtp_forces_test[:,1])
n, bins, patches = ax3.hist(dft_forces_test[:,1] - mtp_forces_test[:,1], 200,
                            range=(-0.2, 0.2),
                            weights=np.ones_like(dft_forces_test[:,1] - mtp_forces_test[:,1])/len(dft_forces_test[:,1]),
                            facecolor='k',
                            alpha=0.5,
                            orientation='vertical')
y = norm.pdf(bins, mu, sigma)
ax3.plot(bins, y / sum(y), 'k--', lw=1.2)
'''

for axis in ['top','bottom','left','right']:
    ax0.spines[axis].set_linewidth(1.8)
    ax1.spines[axis].set_linewidth(1.8)
    #ax2.spines[axis].set_linewidth(1.8)
    #ax3.spines[axis].set_linewidth(1.8)
ax1.set_xlabel("DFT force (eV/$\mathregular{\AA}$)")
ax1.set_ylabel("Deepmd force (eV/$\mathregular{\AA}$)")
#ax2.set_xlabel("Residual energy error (eV/atom)")
#ax3.set_xlabel("Residual force error  (eV/$\mathregular{\AA}$)")
#ax2.set_ylabel("Probability")
#ax3.set_ylabel("Probability")

ax0.set_xlabel("DFT energy (eV/atom)")
ax0.set_ylabel("Deepmd energy (eV/atom)")
ax0.legend(frameon=False, markerscale=2.)
ax1.legend(frameon=False, markerscale=2.)



ax0.text(-3.65, -3.6745, 'Training RMSE: 1.03 meV/atom', color=palette[9], ha='left')
ax0.text(-3.65, -3.689, 'Testing RMSE: 1.32 meV/atom', color=palette[0], ha='left')
ax1.text(-0.37, -2.96, 'Training RMSE: 0.080 eV/$\mathregular{\AA}$', color=palette[9], ha='left')
ax1.text(-0.37, -3.46, 'Testing RMSE: 0.088 eV/$\mathregular{\AA}$', color=palette[0], ha='left')

plt.tight_layout()

plt.show()
