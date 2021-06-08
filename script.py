import os

num_cpus = [1, 2, 4, 8, 16, 32, 64]

if __name__ == '__main__':
    cmd = "mpic++ -o autoc autoc.cpp -lm"
    os.system(cmd)

    for c in num_cpus:
        if c == 64:
            thread_flag = '--use-hwthread-cpus'
            write_flag = True
        else:
            thread_flag = ''
            write_flag = False
        cmd = f"mpiexec -mca btl self,tcp -np {c} {thread_flag} autoc -DWRITEFILE={write_flag}"
        os.system(cmd)
