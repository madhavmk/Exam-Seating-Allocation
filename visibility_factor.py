import numpy as np
from numpy import arange

from matplotlib import pyplot as mp
import numpy as np

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
    return gaussian(angle,0,1)

if __name__=="__main__":

    v1=[0,0]
    v2=[4,4]
    print(angle_between_students(v1,v2))
    print(visibility_factor(v1,v2))   ##   MAIN FUNCTION IS WORKING

    '''
    for i in arange(-2,2,0.1):
        print(i,' ',gaussian(i,0,1))
    '''
