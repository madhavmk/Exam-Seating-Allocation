import os
import copy
import subprocess
import pandas as pd
import shutil
import sys

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

try:
    group_list.remove('./ex_group')
except:
    pass

try:
    group_list.remove('./Rooms')
except:
    pass


print('Groups are : ',group_list)

processes=[]

for group in group_list:
    command = "cd " + group + " && " + "python3 seat_allocation.py > out.txt"
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

output = [p.wait() for p in processes]

try:
    os.mkdir('Rooms')
except FileExistsError:
    print("File exists")
except:
    print('Error occurred')
    exit()

#room_df = pd.read_csv('room-details.csv',header=None)
room_df = pd.read_csv(sys.argv[1])
ind = 0 
for group in group_list:
    rooms = [name for name in os.listdir(group) if name.startswith('Room')]
    src = group + '/'
    dest = './Rooms' 
    for i in rooms:
        row = list(room_df.iloc[ind])
        room_no = str(row[0]) + str(row[1])
        shutil.copyfile(src + i,dest + '/Room_' + room_no)
        ind += 1



