import os

num_cpus = [1, 2, 4, 8, 16, 32]

if __name__ == '__main__':
    cmd = "mpic++ -o autoc auto.cpp -lm"
    os.system(cmd)

    for c in num_cpus:
        cmd = f"mpiexec -mca btl self,tcp -np {c} autoc"
        os.system(cmd)
