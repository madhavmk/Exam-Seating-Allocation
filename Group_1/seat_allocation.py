
"""

updated : student fintness wrapper function is done

"""

"""
seat location = floor_no,room_no:row,column

chromosome : list of seat locations
"""


import input_module
import fitness_calculation
import math
import random
import copy
import pprint
import numpy as np
import helper



st = input_module.read_student_details()

"""
for each srn:
    {
        srn:(subject)
    }
"""


# how many students to consider around a given student to calculate the fitness
student_boundary_range = 2

# list of srn's
list_of_students = [a[0] for a in st]
subject_student = [a[1] for a in st]
student_details = {}
# read in csv and add it to dictonary
# '1,1,:4,1','1,1,:4,2','1,1,:4,3','1,1,:5,1','1,1,:5,2','1,1,:5,3'


room_details = input_module.read_room_details()

allocated_seats = helper.get_allocated_seats(room_details)
#allocated_seats = ['1,1,:1,1','1,1,:1,2','1,1,:1,3','1,1,:2,1','1,1,:2,2','1,1,:2,3','1,1,:3,1','1,1,:3,2','1,1,:3,3','1,1,:4,1','1,1,:4,2','1,1,:4,3','1,1,:5,1','1,1,:5,2','1,1,:5,3']


# seats allocated
# order is same as in list_of_students (corresponding index)



# return student's srn given seat location

def get_student_srn(seat_location, chromosome):

    index = chromosome.index(seat_location)

    return list_of_students[index]

# return student's fitness



def student_fitness(seat_location, srn, chromosome):
    '''
    student_subject = student_details[srn][1]
    student_branch = student_details[srn][0]
    '''
    # fr : floor room no later can also add block
    seat_fr = seat_location.split(sep=":")[0]

    seat_row, seat_col = helper.convert_location_row_col(seat_location)

    # [floor,room:r,c]
    seats_to_compare = []

    for i in range(1, student_boundary_range+1):
        # row- col- rowcol- row+ col+ rowcol+

        # genrate seats to be checked around a particular student
        try:
            s1 = seat_fr + ":" + str(seat_row - i) + "," + str(seat_col)
            a = get_student_srn(s1, chromosome)
            seats_to_compare.append(s1)
        except:
            a = 1

        try:
            s2 = seat_fr + ":" + str(seat_row) + "," + str(seat_col - i)
            a = get_student_srn(s2, chromosome)
            seats_to_compare.append(s2)
        except:
            a = 1

        try:
            s3 = seat_fr + ":" + str(seat_row - i) + "," + str(seat_col - i)
            a = get_student_srn(s3, chromosome)
            seats_to_compare.append(s3)
        except:
            a = 1

        try:
            s4 = seat_fr + ":" + str(seat_row + i) + "," + str(seat_col)
            a = get_student_srn(s4, chromosome)
            seats_to_compare.append(s4)
        except:
            a = 1

        try:
            s5 = seat_fr + ":" + str(seat_row) + "," + str(seat_col + i)
            a = get_student_srn(s5, chromosome)
            seats_to_compare.append(s5)
        except:
            a = 1

        try:
            s6 = seat_fr + ":" + str(seat_row + i) + "," + str(seat_col + i)
            a = get_student_srn(s6, chromosome)
            seats_to_compare.append(s6)
        except:
            a = 1

        try:
            s7 = seat_fr + ":" + str(seat_row + i) + "," + str(seat_col - i)
            a = get_student_srn(s7, chromosome)
            seats_to_compare.append(s7)
        except:
            a = 1
        try:
            s8 = seat_fr + ":" + str(seat_row - i) + "," + str(seat_col + i)
            a = get_student_srn(s8, chromosome)
            seats_to_compare.append(s8)
        except:
            a = 1
        # seats_to_compare.append(s1)
        #print(a)
        # seats_to_compare.append(s4)
        # seats_to_compare.append(s6)

    list_of_fitness_values = []

    #print("SEATS To c \n",seat_location,"\n",seats_to_compare,"\n")

    #print("FOR seat ",seat_location,"\n Comparing > ",seats_to_compare,"\n")
    # print(chromosome)

    if(len(seats_to_compare) == 0):
        print("LOLOLOLOL")
        list_of_fitness_values.append(118000)  # Max possible value of fitness
        #list_of_fitness_values.append(1.944)  # Wemight have to reconsider this value
    else:
        for i in seats_to_compare:

            s_row, s_col = helper.convert_location_row_col(i)

            srns = get_student_srn(i, chromosome)
            #s_branch,s_subject = get_student_details(srn)

            # main student finess function
            # should fill subject similarty

            #student_fitness_value = get_fitness([row,column,subject],[row,column,subject])
            #student_fitness_value = get_distance(seat_row,seat_col,s_row,s_col)

            s1 = [seat_row, seat_col,subject_student[list_of_students.index(srn)]]
            s2 = [s_row, s_col, subject_student[list_of_students.index(srns)]]
            student_fitness_value = fitness_calculation.fitness_value(s1, s2)
            #student_fitness_value = 1 / student_fitness_value
            """
            try:
                student_fitness_value = 1 / student_fitness_value
            except:
                student_fitness_value = 5"""
            # * get_visibility(seat_row,seat_col,s_row,s_col) * get_subject_similarity(student_branch,student_subject,s_branch,s_subject)

            list_of_fitness_values.append(student_fitness_value)

    #print("FITNESS >>>> ",list_of_fitness_values)
    # print(list_of_fitness_values)
    #print(list_of_fitness_values,"\n","Value returned = ",min(list_of_fitness_values))
    return min(list_of_fitness_values)
    # return (sum(list_of_fitness_values)/len(list_of_fitness_values))


# to be coded - calculate fitnesss for a single allocation of seats

def get_fintness(chromosome):
    """
        get individual student fitness
            similarity
            visibility
            distance

        compute overall fitness

        return overall fitness of the given chromosome
    """

    indivial_student_fitness = [student_fitness(
        chromosome[i], list_of_students[i], chromosome) for i in range(len(list_of_students))]

    # print(sum(indivial_student_fitness)/len(list_of_students))
    #print("OVERALL > ",indivial_student_fitness,"\n","returned : ",min(indivial_student_fitness))
    # return min(indivial_student_fitness)
    # return max(indivial_student_fitness)/sum(indivial_student_fitness)
    return sum(indivial_student_fitness)/len(list_of_students)

# n chromosomes will give n new chromosomes


def genetic_crossover(current_population, length_of_chromosome):

    #size_of_population = len(current_population)

    population = copy.deepcopy(current_population)

    list_of_offsprings = []
    #print("len of population ",len(population))
    # input()
    # randomly select two parents and produce an offspring

    # print(population)
    while(len(population) > 1):
        #print(len(population))
        a = random.randint(0, len(population)-1)
        parent_1 = copy.deepcopy(population[a])
        population.pop(a)
        #print("len of population ",len(population))
        # input()
        b = random.randint(0, len(population)-1)
        parent_2 = copy.deepcopy(population[b])
        population.pop(b)

        offspring_1 = []
        offspring_2 = []

        crossover_point = random.randint(1, length_of_chromosome-2)
        offspring_1 = parent_1[0:crossover_point]
        offspring_2 = parent_2[0:crossover_point]

        for seat in parent_2:
            if not(seat in offspring_1):
                offspring_1.append(seat)

        for seat in parent_1:
            if not(seat in offspring_2):
                offspring_2.append(seat)

        list_of_offsprings.append(offspring_1)
        list_of_offsprings.append(offspring_2)

        # """Trying to add the reverse image as well
        offspring_1 = []
        offspring_2 = []

        crossover_point = random.randint(1, length_of_chromosome-2)
        offspring_1 = parent_1[0:crossover_point]
        offspring_2 = parent_2[0:crossover_point]

        for seat in parent_2:
            if not(seat in offspring_1):
                offspring_1.append(seat)

        for seat in parent_1:
            if not(seat in offspring_2):
                offspring_2.append(seat)

        list_of_offsprings.append(offspring_1)
        list_of_offsprings.append(offspring_2)

        offspring_1 = []
        offspring_2 = []

        crossover_point = random.randint(1, length_of_chromosome-2)
        offspring_1 = parent_1[0:crossover_point]
        offspring_2 = parent_2[0:crossover_point]

        for seat in parent_2:
            if not(seat in offspring_1):
                offspring_1.append(seat)

        for seat in parent_1:
            if not(seat in offspring_2):
                offspring_2.append(seat)

        list_of_offsprings.append(offspring_1)
        list_of_offsprings.append(offspring_2)

        offspring_1 = []
        offspring_2 = []

        crossover_point = random.randint(1, length_of_chromosome-2)
        offspring_1 = parent_1[0:crossover_point]
        offspring_2 = parent_2[0:crossover_point]

        for seat in parent_2:
            if not(seat in offspring_1):
                offspring_1.append(seat)

        for seat in parent_1:
            if not(seat in offspring_2):
                offspring_2.append(seat)

        list_of_offsprings.append(offspring_1)
        list_of_offsprings.append(offspring_2)
        # """

    return list_of_offsprings



def genetic_mutation_swap(current_population, length_of_chromosome):
    population = copy.deepcopy(current_population)
    # print(population)

    for i in range(len(population)):

        # test and change the number of swaps
        #number_of_swaps = int(length_of_chromosome//2)
        #number_of_swaps = random.randint(int(length_of_chromosome//10),int(length_of_chromosome//2))
        number_of_swaps = random.randint(int(1), int(length_of_chromosome//2))

        for _ in range(number_of_swaps):

            swap_index_1 = random.randint(0, length_of_chromosome-1)
            swap_index_2 = random.randint(0, length_of_chromosome-1)

            temp = population[i][swap_index_1]

            population[i][swap_index_1] = population[i][swap_index_2]
            population[i][swap_index_2] = temp

    return population



def genetic_mutation_insertion(current_population, length_of_chromosome):
    population = copy.deepcopy(current_population)
    # print(population)

    for i in range(len(population)):

        # test and change the number of swaps
        number_of_insertions = 5

        for _ in range(number_of_insertions):

            index = random.randint(0, length_of_chromosome - 2)
            follow_index = random.randint(0, length_of_chromosome-1)

            print("\n\n POPULATION [i] IS ",
                  population[i], follow_index, sep="//////")

            follow_element = population[i][follow_index]
            # shift other elements
            if(follow_index > index):
                for k in range(follow_index, index, -1):
                    population[i][k] = population[i][k-1]
                population[i][index + 1] = follow_element
            '''
            elif(follow_index<index):
                for k in range(follow_index,index):
                    population[i][k] = population[i][k-1]
                population[i][index + 1 ] = follow_element
            '''

    return population



def genetic_mutation_scramble(current_population, length_of_chromosome):
    population = copy.deepcopy(current_population)
    # print(population)

    for i in range(len(population)):

        # should decide scramble length
        scramble_length = 3
        # max(3,length_of_chromosome//10)
        scramble_index_list = []

        for _ in range(scramble_length):
            scramble_index_list.append(
                random.randint(0, length_of_chromosome-1))

        scramble_index_list = set(scramble_index_list)
        scramble_index_list = list(scramble_index_list)

        scramble_values = [population[i][k] for k in scramble_index_list]

        scramble_length = len(scramble_index_list)

        random.shuffle(scramble_values)

        for a in range(scramble_length):

            change_value_index = scramble_index_list[a]
            population[i][change_value_index] = scramble_values[a]

    return population



def genetic_mutation(current_population, length_of_chromosome):
    a = copy.deepcopy(current_population)

    ret = genetic_mutation_swap(a, length_of_chromosome)

    return ret



def genetic(length_of_chromosome, initial_chromosome, population_size, epochs):

    population = []
    population.append(initial_chromosome)

    for i in range(population_size-1):
        #print("len of population ",len(population)," ")
        #chromosome_to_generate_random = random.randint(0,len(population)-1)
        #print("population of ",i,"      ",population,"\n\n")
        t = copy.deepcopy(population[i])

        random.shuffle(t)
        population.append(t)
        #print("len of population ",len(population),"\n")
        # population.append(initial_chromosome)

    # now initial population is ready

    current_generation = 1

    """ To add exponential decay
    threshold = 0.5
    decay = 0.00005
     """

    while(current_generation < epochs):

        print("\n\n\nGENERATION : ", current_generation)

        """
        for n in range(len(list_of_students)):

            print(list_of_students[n],subject_student[n],">",population[0][n])
        """

        fitness_population = [get_fintness(i) for i in population]
        print('all fitness values >> ', fitness_population)
        print("max fitness >> ", max(fitness_population))
        #print("max fitness >> ",fitness_population[0])
        # a=input()
        # get indexes of top fit chromosomes

        """setting up exponential decay
        threshold = threshold*math.exp(-current_generation*decay)
        threshold = threshold if threshold > 0.05 else 0.05
        point = int(threshold*100)
        print('point: ',point)

        top_fitness_indexes = sorted(range(len(fitness_population)), key = lambda sub: fitness_population[sub])[-point:]
        """

        top_fitness_indexes = sorted(range(len(
            fitness_population)), key=lambda sub: fitness_population[sub])[-(population_size//4):]

        selected_chromosomes = [population[i] for i in top_fitness_indexes]

        new_chromosomes = genetic_crossover(
            selected_chromosomes, length_of_chromosome)
        #print("new ",new_chromosomes)
        #new_chromosomes = genetic_mutation(new_chromosomes,length_of_chromosome)
        new_chromosomes = genetic_mutation(
            new_chromosomes, length_of_chromosome)

        population = selected_chromosomes
        for i in new_chromosomes:
            population.append(i)

        # print(population[top_fitness_indexes[0]],"\n\n>>",population[-1])
        print("\n\n\n")

        current_generation += 1

    top_fitness_indexes = sorted(range(len(fitness_population)), key=lambda sub: fitness_population[sub])[-(population_size//2):]

    #final_allocation = [population[top_fitness_indexes[0]]]
    return population


if __name__ == "__main__":
    
    a = genetic(len(list_of_students), allocated_seats, 300, 6000)

    print(a)

    print("\n\nFINAL ALLOCATION \n\n")

    for i in range(len(a)):

        print("allocation ", i, " : \n")
        for n in range(len(list_of_students)):

            print(list_of_students[n], subject_student[n], ">", a[i][n])
        print("\n\n")

    for i in range(len(a)):

        print("Allocation wrt seats ", i, " fitness ", get_fintness(a[i]))
        array = []
        rooms = []
        start = 0
        
        for r in room_details:
            row,col = int(r[2]),int(r[3])
            total_seats = row*col
            rooms.append(allocated_seats[start:start + total_seats])
            start += total_seats
        print("Rooms: ",rooms)

        for room in rooms:
            sub_array = []

            for s in room:
                try:
                    srn = get_student_srn(s, a[i])
                    sub = subject_student[list_of_students.index(srn)]
                    sub_array.append('{0: <4}'.format(sub))
                except:
                    sub_array.append('{0: <4}'.format("--"))

            print(sub_array)
            sub_array = np.array(sub_array)
            sub_array.resize(int(room_details[0][2]), int(room_details[0][3]))
            array.append(sub_array)
        
        for j in array:
            print(j)
            print("\n")
