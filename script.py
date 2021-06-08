import os

num_cpus = [1, 2, 4, 8, 16, 32]

if __name__ == '__main__':
    cmd = "mpic++ -o autoc autoc.cpp -lm"
    os.system(cmd)

    for c in num_cpus:
        if c == 64:
            flag = '--use-hwthread-cpus'
        else:
            flag = ''
        cmd = f"mpiexec -mca btl self,tcp -np {c} autoc {flag}"
        os.system(cmd)
