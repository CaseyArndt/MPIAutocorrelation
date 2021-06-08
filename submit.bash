#!/bin/bash
#!SBATCH -J Heat
#!SBATCH -A cs475-575
#!SBATCH -p class
#!SBATCH -N 8   # number of nodes
#!SBATCH -n 8   # number of tasks
#!SBATCH -o heat.out
#!SBATCH -e heat.err
mpic++ heat.cpp -o heat -lm
mpiexec -mca btl self,tcp -np 4 heat    # 4 processors