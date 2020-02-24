import numpy as np
from numpy import arange
import math

from matplotlib import pyplot as mp
import numpy as np
from scipy.spatial import distance

import input_module

from input_module import subject_subject_dictionary_constant


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def unit_vector(vector):
    # Returns the unit vector of the vector. 
    return vector / np.linalg.norm(vector)

def angle_between_vectors(v1, v2):

    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def angle_between_students(s1,s2):
    vertical_vector=[0,1]
    difference_vector=[s1[0]-s2[0],s1[1]-s2[1]]

    return angle_between_vectors(vertical_vector,difference_vector) 

def visibility_factor(s1,s2):
    angle= angle_between_students(s1,s2)
    vis_fact=gaussian(angle,0,1)
    return float(vis_fact)

def euclidean_distance(s1,s2):
    dst = distance.euclidean(s1, s2)
    return float(dst)


def subject_similarity(s1,s2):
    subj_sim=subject_subject_dictionary_constant[s1][s2]
    return float(subj_sim)


def fitness_value(s1,s2):   ### THIS IS THE FUNCTION TO CALL  s1->[row,column,subject]  s2->[row,column,subject]

    visibility_coefficient=visibility_factor([s1[0],s1[1]],[s2[0],s2[1]])
    #print("visibility_coefficient ",visibility_coefficient)
    distance_coefficient=euclidean_distance([s1[0],s1[1]],[s2[0],s2[1]])
    #print("distance_coefficient ",distance_coefficient)
    subject_similarity_coefficient=subject_similarity(s1[2],s2[2])
    #print("subject_similarity_coefficient ",subject_similarity_coefficient)

    subject_dissimilarity_coefficient = (1 - subject_similarity_coefficient) 
    #/ 0.9 * 70
    non_visibility_coefficient = (1 - visibility_coefficient)
    #/1 * 15
    distance_coefficient = math.pow(distance_coefficient,3)
    #/2.4) * 15
    #fitness_s1_s2 = visibility_coefficient * (1/distance_coefficient) * subject_similarity_coefficient
    fitness_s1_s2 = ( non_visibility_coefficient + distance_coefficient ) * math.pow(subject_dissimilarity_coefficient*10,2)
    #15+15*70
    #print('fitness s1 s2 ',fitness_s1_s2)
    #print("SEAT : ",s1,s2,fitness_s1_s2,"\n\n")
    return fitness_s1_s2
"""
if __name__=="__main__":

    v1=[1,1,'A']
    v2=[4,4,'B']
    print('subject dict ',subject_subject_dictionary_constant)
    fitness = fitness_value(v1,v2)
    print('fitness ',fitness)   ##   MAIN FUNCTION IS WORKING

    '''
    for i in arange(-2,2,0.1):
        print(i,' ',gaussian(i,0,1))
    '''
"""