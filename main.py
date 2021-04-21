import subprocess
import io

sp = subprocess.Popen(['ls -l'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout)
s = ''
while s:
    s = out.readline()
    print(s)
