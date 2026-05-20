#!/bin/bash
#SBATCH -J ad-em
#SBATCH -N 2
#SBATCH --ntasks-per-node=16
#SBATCH -t 001:00:00
#SBATCH -A xxx

export OMP_NUM_THREADS=2
export OMP_STACKSIZE=512m

module add VASP/6.5.0.16122024-omp-hpc1-intel-2023a-eb
mpprun vasp_std
