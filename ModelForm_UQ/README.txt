### bash script command
nohup stdbuf -o0 bash run_get_snapshots.bash 0 999 > logSSbash.txt & echo $(date) $! > ss_bash.pid
nohup stdbuf -o0 bash run_get_computemsd.bash 0 999 > logmsd_bash.txt & echo $(date) $! > msd_bash.pid
kill -9 $(<msd_pids.txt)

### individual
matlab -nodisplay -nosplash -nodesktop -r "get_snapshots('trajectory.lammpstrj', '/data1/yq87/CRISPS/Na3SbSe4-May62024/SIM_15ps_ALLSS/rom_data_15ps/ROM_NVT_1e-6/gamma_0/NEP'); exit"
python -u compute_msd.py "/data1/yq87/CRISPS/Na3SbSe4-May62024/SIM_15ps_ALLSS/rom_data_15ps/ROM_NVT_1e-6/gamma_0/MLIP"
python -u compute_msd.py "/data1/yq87/CRISPS/Na3SbSe4-May62024/SIM_15ps_ALLSS/rom_data_15ps/ROM_NVT_1e-6/gamma_0/NEP"


# FOM OF 80 ps
## MLIP
nohup stdbuf -o0 taskset -c 1 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logMLIP.txt & echo $(date) $! > run.pid
## NEP
nohup stdbuf -o0 taskset -c 143 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logNEP.txt & echo $(date) $! > run.pid


nohup stdbuf -o0 bash run_get_snapshots.bash 2 999 > logbash.txt & echo $(date) $! > bash.pid

# Rand15ps_eps1e-6/gamma0, (/==JOB DONE ; O==RUNNING)
## LFeps = 1e-4 # (coreId_start, coreId_end, sampleId_start, sampleId_end, LFeps, NrLF, NrHF, numSamples) 
nohup stdbuf -o0 bash taskset_run.bash 0 24 0 249 1e-4 469 315 1000 > logROMNr315.txt & echo "part1 " $(date) $! >> run.pid  /
nohup stdbuf -o0 bash taskset_run.bash 25 49 250 499 1e-4 469 315 1000 > logROMNr315.txt & echo "part2 " $(date) $! >> run.pid  /
nohup stdbuf -o0 bash taskset_run.bash 50 74 500 749 1e-4 469 315 1000 > logROMNr315.txt & echo "part3 " $(date) $! >> run.pid  /
nohup stdbuf -o0 bash taskset_run.bash 75 99 750 999 1e-4 469 315 1000 > logROMNr315.txt & echo "part4 " $(date) $! >> run.pid  /
## LFeps = 1e-5 # (coreId_start, coreId_end, sampleId_start, sampleId_end, LFeps, NrLF, NrHF, numSamples) 
nohup stdbuf -o0 bash taskset_run.bash 0 24 0 249 1e-5 606 178 1000 > logROMNr178.txt & echo "part1 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 25 49 250 499 1e-5 606 178 1000 > logROMNr178.txt & echo "part2 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 50 74 500 749 1e-5 606 178 1000 > logROMNr178.txt & echo "part3 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 100 124 750 999 1e-5 606 178 1000 > logROMNr178.txt & echo "part4 " $(date) $! >> run.pid /


# Rand15ps_eps1e-6/gamma1e-5, 
## LFeps = 1e-4 # (coreId_start, coreId_end, sampleId_start, sampleId_end, LFeps, NrLF, NrHF, numSamples)
nohup stdbuf -o0 bash taskset_run.bash 0 24 0 249 1e-4 463 520 1000 > logROMNr520.txt & echo "part1 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 25 49 250 499 1e-4 463 520 1000 > logROMNr520.txt & echo "part2 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 50 74 500 749 1e-4 463 520 1000 > logROMNr520.txt & echo "part3 " $(date) $! >> run.pid /
nohup stdbuf -o0 bash taskset_run.bash 75 99 750 999 1e-4 463 520 1000 > logROMNr520.txt & echo "part4 " $(date) $! >> run.pid /
## LFeps = 1e-5 # (coreId_start, coreId_end, sampleId_start, sampleId_end, LFeps, NrLF, NrHF, numSamples) /JOB RUNNING
<!-- nohup stdbuf -o0 bash taskset_run.bash 0 24 0 249 1e-5 622 361 1000 > logROMNr361.txt & echo "part1 " $(date) $! >> run.pid  
nohup stdbuf -o0 bash taskset_run.bash 25 49 250 499 1e-5 622 361 1000 > logROMNr361.txt & echo "part2 " $(date) $! >> run.pid   -->
### new arrangements for when batch cores are available; SAMPLES ID:0 -499 ###
nohup stdbuf -o0 bash taskset_run.bash 0 24 0 124 1e-5 622 361 1000 > logROMNr361.txt & echo "part1 " $(date) $! >> run.pid O
nohup stdbuf -o0 bash taskset_run.bash 25 49 125 249 1e-5 622 361 1000 > logROMNr361.txt & echo "part2 " $(date) $! >> run.pid O
nohup stdbuf -o0 bash taskset_run.bash 50 74 250 374 1e-5 622 361 1000 > logROMNr361.txt & echo "part2 " $(date) $! >> run.pid O
nohup stdbuf -o0 bash taskset_run.bash 100 124 375 500 1e-5 622 361 1000 > logROMNr361.txt & echo "part4 " $(date) $! >> run.pid O
##############################################################################
nohup stdbuf -o0 bash taskset_run.bash 75 99 500 749 1e-5 622 361 1000 > logROMNr361.txt & echo "part3 " $(date) $! >> run.pid O
nohup stdbuf -o0 bash taskset_run.bash 100 124 750 999 1e-5 622 361 1000 > logROMNr361.txt & echo "part4 " $(date) $! >> run.pid  /







#################################################################################
###### MODE 400 ######
# gamma = 1e-5 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 140 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 141 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 142 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 143 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 1e-4 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 139 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 138 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 137 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 136 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 1e-3 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 135 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 134 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 133 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 132 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 1e-2 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 131 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 130 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 129 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 128 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 1e-1 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 127 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 126 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 125 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 124 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 1e-0 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 123 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 122 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 121 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 120 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid

# gamma = 0
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 119 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 118 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 117 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 116 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo $(date) $! > run.pid


####################################################################################################################################################################################################
# EXAMPLE
###### EPS = 1e-6 ######
# eps= 1e-6, gamma = 1e-0 ///
## Global Simulation Centered
nohup stdbuf -o0 taskset -c 140 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCMLIP.txt & echo "taskset Global Centered MLIP -c 140: " $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 141 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logGlobalCNEP.txt & echo "taskset Global Centered NEP -c 141: " $(date) $! > run.pid
# Individual Simulations Centered
nohup stdbuf -o0 taskset -c 142 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCMLIP.txt & echo "taskset Centered MLIP -c 142: " $(date) $! > run.pid
nohup stdbuf -o0 taskset -c 143 /data1/yq87/software/interface-lammps-mlip-2/mylammps/src/lmp_serial -in in.lammps > logCNEP.txt & echo "taskset Centered NEP -c 143: " $(date) $! > run.pid

####################################################################################################################################################################################################

### MODES 400 AND 600
nohup python -u get_eigval_spectrum_mom_Gamma_modes.py > mode400_gamma_log.txt 2>&1 & echo $! >> run_mode_spectrum_.pid

matlab -r "get_snapshots('trajectory.lammpstrj', '/data1/yq87/CRISPS/Na3SbSe4-May62024/SIM_30ps_ALLSS/Symplectic_Test_15ps/data/NEP/')"