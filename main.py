import input_module

if __name__=='__main__':

    configuration_data = input_module.read_configuration_file()
    student_details = input_module.read_student_details()
    subject_details = input_module.read_subject_details()
    print(configuration_data)
    print(student_details)
    print(subject_details)

