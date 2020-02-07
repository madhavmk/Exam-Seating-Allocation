import input_module
import fitness_calculation

if __name__=='__main__':

    configuration_data = input_module.read_configuration_file()
    student_details = input_module.read_student_details()
    subject_details = input_module.read_subject_details()
    print("configuration_data ",configuration_data)
    print("student_details ",student_details)
    print("subject_details ",subject_details)
    
    """
    #For example 2 students of s1->[row,column,subject]  s2->[row,column,subject]
    s1=[1,1,'A']
    s2=[4,4,'B']
    fitness = fitness_calculation.fitness_value(s1,s2)
    print("fitness ",fitness)
    """


