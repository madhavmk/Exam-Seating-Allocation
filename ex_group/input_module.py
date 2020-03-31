import json
import csv




def read_configuration_file():
    
    with open('configuration.json') as open_json_file:
        json_conf_data=json.load(open_json_file)
    
    #print('\nData type ',type(json_conf_data),'\nData\n',json_conf_data)
    
    return json_conf_data


def read_student_details():
    configuration_data=read_configuration_file()
    array=[]
    #print(configuration_data)
    #print(configuration_data["file_location"]["student-details"])
    with open(configuration_data["file_location"]["student-details"]) as student_details_file:
        student_details_file = csv.reader(student_details_file)
        for row in student_details_file:
            #print(row)
            array.append(list([str(row[0]),str(row[1])]))
    #print(array)
    return array


def read_subject_details():
    configuration_data=read_configuration_file()
    subject_subject_dictionary=dict()
    #temp_dictionary=dict()
    subject_column=[]
    subject_row=[]
    csv_array=[]
    with open(configuration_data["file_location"]["subject-details"]) as subject_details_file:
        subject_details_file = csv.reader(subject_details_file)
        #print(subject_details_file)
        for row in subject_details_file:
            csv_array.append(list(row))
    #print(csv_array)

    for i in range(len(csv_array)):
        subject_column.append(str(csv_array[i][0]))
        #print(csv_array[i][0])
    for i in range(len(csv_array[0])):
        subject_row.append(str(csv_array[0][i]))

    subject_row.pop(0)
    subject_column.pop(0)

    #print(subject_column)
    #print(subject_row)

    for i in range(len(subject_column)):
        subject_dictionary=dict()
        for j in range(len(subject_row)):
            subject_dictionary[subject_row[j]]=csv_array[i+1][j+1]
        subject_subject_dictionary[subject_column[i]]=subject_dictionary

    '''
    print('SUBJECT SUBJECT DICTIONARY')

    for key in subject_subject_dictionary:
        print('key : ',key,'\n',subject_subject_dictionary[key],'\n\n')
    '''

    return subject_subject_dictionary



def read_room_details():
    configuration_data=read_configuration_file()
    array=[]
    #print(configuration_data)
    #print(configuration_data["file_location"]["student-details"])
    with open(configuration_data["file_location"]["room-details"]) as room_details_file:
        room_details_file = csv.reader(room_details_file)
        for row in room_details_file:
            #print(row)
            array.append(list([str(row[0]),str(row[1]),str(row[2]),str(row[3])]))
    #print(array)
    return array


subject_subject_dictionary_constant=read_subject_details()



