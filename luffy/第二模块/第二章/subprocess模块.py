
import subprocess
# print(subprocess.call(['ifconfig','eth0']))
import os
# os.system('dir')
# subprocess.run(["dir"])
# subprocess.call(['dir'])
# print(subprocess.run())
# print(subprocess.run([],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True,shell=True))
import subprocess,sys



print(subprocess.run(['dir'], shell = True, stdout = subprocess.PIPE))
# print(subprocess.call(["ls", "-l"]))
# subprocess.run('sleep 10',shell=True,stdout=subprocess.PIPE)

print(subprocess.Popen("dir", shell=True))
import os
print(os.popen('dir').read())