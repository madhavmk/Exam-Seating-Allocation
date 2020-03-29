import os
import copy
import subprocess

subfolders_list = [ f.path for f in os.scandir("./") if f.is_dir() ]

group_list = copy.deepcopy(subfolders_list)

try:
    group_list.remove('./__pycache__')
except:
    pass
try:
    group_list.remove('./.git')
except:
    pass

print('Groups are : ',group_list)

processes=[]

for group in group_list:
    command = "cd " + group + " && " + "python3 seat_allocation.py > out.txt"
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

output = [p.wait() for p in processes]

"""
print('Started group 1')
#os.system('cmd /c "cd Group_1  && python seat_allocation.py > out.txt"')
p1 = subprocess.Popen( "cd Group_1  && python seat_allocation.py > out.txt")
print('Started group 2')
#os.system('cmd /c "cd Group_2  && python seat_allocation.py > out.txt"')
p2 = subprocess.Popen( "cd Group_2  && python seat_allocation.py > out.txt")
print('Started group 3')
#os.system('cmd /c "cd Group_3  && python seat_allocation.py > out.txt"')
p3 = subprocess.Popen( "cd Group_3  && python seat_allocation.py > out.txt")
"""
