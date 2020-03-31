import os
import subprocess
import pandas as pd
import numpy as np
import shutil
import errno

MAX_STUDENTS_GROUP = 80

"""
Returns dictionary containing array of students for each subject
"""
def get_student_dict(stdf, sdf):
    sdict = dict()
    for i in sdf.columns[1:]:
        temp = stdf.loc[stdf['subject'] == i]
        sdict[i] = np.array(temp['student'])
    return sdict

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



if __name__ == "__main__":
    # get all csv files
    student_df = pd.read_csv('student-details.csv')
    room_df = pd.read_csv('room-details.csv',header=None)
    subject_df = pd.read_csv('subject-details.csv')

    # Get corresponding dependencies
    student_dict = get_student_dict(student_df,subject_df)
    room_seats = get_room_seats(room_df)    
    groups = get_all_groups(room_seats)
    
    # create folders
    create_groups(groups,room_df,subject_df)