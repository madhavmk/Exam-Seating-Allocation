
"""
seat location = floor_no,room_no,row.column

chromosome : list of seat locations
"""

import random
import copy


"""
for each srn:
    {
        srn:(branch,subject)
    }
"""
#list of srn's 
list_of_students = []

student_details = {}
#read in csv and add it to dictonary

def student_fitness(seat_location,srn,chromosome):
    
    

    pass



#to be coded - calculate fitnesss for a single allocation of seats
def get_fintness(chromosome):
    
    """
        get individual student fitness
            similarity
            visibility
            distance
        
        compute overall fitness
    
        return overall fitness of the given chromosome
    """

    indivial_student_fitness = [student_fitness(chromosome[i],list_of_students[i],chromosome) for i in range(len(chromosome))]


    pass

# n chromosomes will give n new chromosomes
def genetic_crossover(current_population,length_of_chromosome):

    size_of_population = len(current_population)

    population = copy.deepcopy(current_population)

    list_of_offsprings = []

    #randomly select two parents and produce an offspring

    while(len(population) != 0):

        a = random.randint(0,len(population)-1)
        parent_1 = population[a]
        population.pop(a)

        b = random.randint(0,len(population)-1)
        parent_2 = population[b]
        population.pop(b)

        offspring_1 = []
        offspring_2 = []

        crossover_point = random.randint(1,length_of_chromosome-2)

        offspring_1 = parent_1[0:crossover_point].exetend(parent_2[crossover_point:length_of_chromosome])
        offspring_2 = parent_2[0:crossover_point].extend(parent_1[crossover_point:length_of_chromosome])

        list_of_offsprings.append(offspring_1)
        list_of_offsprings.append(offspring_2)

    return list_of_offsprings

def genetic_mutation(current_population,length_of_chromosome):

    population = copy.deepcopy(current_population)

    for i in range(len(population)):

        # test and change the number of swaps
        number_of_swaps = random.randint(1,length_of_chromosome//2)

        for j in range(number_of_swaps):

            swap_index_1 = random.randint(0,length_of_chromosome-1)
            swap_index_2 = random.randint(0,length_of_chromosome-1)

            temp = population[i][swap_index_1]

            population[i][swap_index_1] = population[i][swap_index_2]
            population[i][swap_index_2] = temp
    
    return population

def genetic(length_of_chromosome,initial_chromosome,population_size,epochs):

    population=[]
    population.append(initial_chromosome)

    for i in range(population_size):

        chromosome_to_generate_random = random.randint(0,len(population)-1)

        population.append(random.shuffle(population[chromosome_to_generate_random]))

    #now initial population is ready

    current_generation = 1

    while(current_generation<epochs):

        fitness_population = [get_fintness(i) for i in population]

        #get indexes of top fit chromosomes
        top_fitness_indexes = sorted(range(len(fitness_population)), key = lambda sub: fitness_population[sub])[-(population_size//2):] 

        selected_chromosomes = [fitness_population[i] for i in top_fitness_indexes]

        new_chromosomes = genetic_crossover(selected_chromosomes,length_of_chromosome)
        new_chromosomes = genetic_mutation(selected_chromosomes,length_of_chromosome)

        population = selected_chromosomes
        for i in new_chromosomes:
            population.append(i)