#!/bin/bash
#!SBATCH -J AutoC
#!SBATCH -A cs475-575
#!SBATCH -p class
#!SBATCH -N 8   # number of nodes
#!SBATCH -n 8   # number of tasks
#!SBATCH -o autoc.out
#!SBATCH -e autoc.err
mpic++ autoc.cpp -o autoc -lm
mpiexec -mca btl self,tcp -np 4 autoc    # 4 processors