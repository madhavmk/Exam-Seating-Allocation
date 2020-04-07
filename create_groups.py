import os
import subprocess
import pandas as pd
import numpy as np
import shutil
import errno
from numpy.random import choice

MAX_STUDENTS_GROUP = 80
MAX_SUBJECTS_ROOM = 4

"""
Returns dictionary containing array of students for each subject
"""
def get_student_dict(stdf, sdf):
    sdict = dict()
    sub_arr = []
    for i in sdf.columns[1:]:
        temp = stdf.loc[stdf['subject'] == i]
        sdict[i] = np.array(temp['student'])
        sub_arr.append(i)
    return sdict,sub_arr

"""
Returns array containg total no of seats of each room
"""
def get_room_seats(rdf):
    seats = []
    for _, row in rdf.iterrows():
        seats.append(row[2]*row[3])
    return seats

"""
Returns array of tuples containing seats,rooms of each group
"""
def get_all_groups(room_seats):
    groups = []
    seats = 0
    rooms = 0
    for i in room_seats:
        seats += i
        if seats < MAX_STUDENTS_GROUP: rooms += 1
        else:
            groups.append((seats-i,rooms))
            seats = i
            rooms = 1
    groups.append((seats,rooms))
    return groups

"""
Creates folders based on the number of groups and splits the room-details and subject-details onto those files
"""
def create_groups(groups,rdf,sdf):
    rind = 0
    src = './ex_group'
    for i,rooms in enumerate(groups,1):
        temp_rdf = rdf.iloc[rind:rind+rooms[1]]
        dest = './Group_' + str(i)
        shutil.copytree(src, dest)
        pd.DataFrame(temp_rdf).to_csv(dest + "/room-details.csv",header=None, index=None) 
        pd.DataFrame(sdf).to_csv(dest + "/subject-details.csv",header=None, index=None)
        rind += rooms[1]

"""
Returns an array with probablities of being selected w.r.t a specified subject
"""
def get_sub_prob(exc_subs,subject,sdf,sub_arr,pre_arr):
    simis = np.array(sdf[subject])
    sub_prob = list(map(lambda x: 1/x,simis))
    for i in exc_subs:
        ind = sub_arr.index(i)
        sub_prob[ind] = 0
    if(len(exc_subs) < len(pre_arr)):
        for i,sub in enumerate(sub_arr):
            if sub not in pre_arr:
                sub_prob[i] = 0

    s = sum(sub_prob)
    sub_prob = list(map(lambda x: x/s,sub_prob))    
    return list(sub_prob)

"""
Splits the students into multiple groups based on the subjects and group size
"""
def create_student_groups(sub_arr,sdf,st_dict,groups):
    dest = './Group_'
    #dest = './tempp'
    exc_subs = []
    prev_subs = []
    total_students = 0
    for i,group in enumerate(groups,1):
        print("Group No ",i,"--"*50)
        exc_len = len(exc_subs)
        slen = len(sub_arr)
        if(exc_len == slen):
            break
        elif (slen - exc_len) <= MAX_SUBJECTS_ROOM:
            total_students = group[0]//(slen - exc_len)
        else:
            total_students = group[0]//MAX_SUBJECTS_ROOM
        start_sub = ""
        print("Total count: ",total_students)
        st_count = 0
        prev_subs = [ele for ele in prev_subs if ele not in exc_subs]
        if(len(prev_subs) == 0):        
            start_sub = max(st_dict.keys(),key = lambda x: len(st_dict[x]))
        else:
            start_sub = prev_subs[0]
        print("Start sub: ",start_sub)
        st_arr = []
        local_exc_subs = list.copy(exc_subs)
        print("Excluded subs: ",local_exc_subs)
        exit = 0
        print("Entering group allocation")
        while True:
            sub_len = st_dict[start_sub].size 
            print("Subject len: ",sub_len)
            added_len = 0           
            if(sub_len > total_students):
                added_len = total_students
                print("1")
            elif sub_len <= total_students:
                added_len = sub_len
                print("2")
                exc_subs.append(start_sub)
            if(st_count + added_len > group[0]):
                added_len = group[0] - st_count
                exit = 1
            elif st_count + added_len == group[0]:
                exit = 1
            
            st_arr.extend([[x,start_sub] for x in st_dict[start_sub][:added_len]])
            st_dict[start_sub] = st_dict[start_sub][added_len:]
            st_count += added_len  

            if start_sub not in prev_subs:
                prev_subs.append(start_sub)          
            if exit:
                exit = 0
                break
            """
            """
            local_exc_subs.append(start_sub)
            if slen == len(local_exc_subs):
                local_exc_subs = list.copy(exc_subs)          
            arr = []
            if(len(prev_subs) > 1):
                arr = prev_subs
            else:
                arr = sub_arr
            print("Subjects Array: ",sub_arr)
            print("Preferred subjects: ",arr)
            sub_prob = get_sub_prob(local_exc_subs,start_sub,sdf,sub_arr,arr)
            print("Subject probablities: ",sub_prob)
            start_sub = choice(sub_arr,1,p=sub_prob)[0]
            print("Next subject: ",start_sub)
            print("Local excluded and global excluded: ",local_exc_subs,exc_subs)
        
        pd.DataFrame(st_arr).to_csv(dest +str(i) + "/student-details.csv",header=None, index=None)
        #pd.DataFrame(st_arr).to_csv(dest + "/student" + str(i) + ".csv",header=None, index=None)


if __name__ == "__main__":
    # get all csv files
    student_df = pd.read_csv('student-details.csv')
    room_df = pd.read_csv('room-details.csv',header=None)
    subject_df = pd.read_csv('subject-details.csv')

    # Get corresponding dependencies
    student_dict,subject_arr = get_student_dict(student_df,subject_df)
    room_seats = get_room_seats(room_df)    
    groups = get_all_groups(room_seats)

    # create folders
    create_groups(groups,room_df,subject_df)
    
    # create the student csv files
    create_student_groups(subject_arr,subject_df,student_dict,groups)

    # call all_group_call.py
    command = "python3 all_group_call.py"
    process = subprocess.Popen(command, shell=True)
    process.wait()

