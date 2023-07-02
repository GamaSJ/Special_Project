#import libraries
import numpy as np
from scipy.spatial.transform import Rotation as R
import time

#########################################

def compute_distances(array_A, array_B):
    """
    Computes distance between arrays for each point.

    Args:
        array_A (np.array): Reference Array
        array_B (np.array): Array to modify

    Returns:
        np.array: distance norm
    """


    # Computes dist per point along two arrays
    return np.linalg.norm(array_A - array_B, axis=1)

def gradient_descent (array_A, array_B,max_iterations,learning_rate, shift_limit, stop_criteria):
    """
    Coded algorithm to minimise distance between two arrays.
    Algo uses gradient decent

    Args:
        array_A (np.array): Reference Array
        array_B (np.array): Array to modify
        max_iterations (int): max number of iterations
        learning_rate (float): learning rate for algo
        shift_limit (float): limits of adjustment
        stop_criteria (float): criteria to stop algo

    Returns:
        shigt (np.array): shift in x,y,z for array B
        distances_mean (np.array): evolution of mean distances as per algo
        distances_sum (np.array): evolution of total distances as per algo
        iteration (int): number of iterations done by algo


    """





    start_time = time.perf_counter()#for the time measurement
    #Defined arguments for solver
    shift = np.zeros(3)  # Initial shift values
    distances_mean = []  # List to store distances_mean per iteration
    distances_sum = [] # List to store distances_sum per iteration
    ref_distance = float ('inf')#large number

    #Actual solver starts iterating from this point onwards
    for iteration in range(max_iterations):
        distances = compute_distances(array_A, (array_B + shift))# Apply shift to array B
        gradient = -1 * np.mean((array_A - (array_B + shift)) / distances[:, np.newaxis], axis=0)#computes gradient
        shift -= learning_rate * gradient  # Update shift x,y,z
        shift = np.clip (shift,-shift_limit,shift_limit)#snips if necessary
        distances_mean.append(np.mean(distances))#appends mean distances
        distances_sum.append(distances.sum())#appends total distances

        if abs(distances.sum()-ref_distance) <= stop_criteria:#conditional to check stop criteria
            break
        ref_distance = distances.sum()#update variable for next iteration

    end_time = time.perf_counter()#for the time measurement
    solver_time = end_time - start_time
    print(f"The solver did {iteration} iterations")
    print(f"It took {solver_time:.3f} seconds")
    print(f"The solver found the following optimised shift {np.around(shift, decimals=3)} in the x, y & z coordinates")

    return shift, distances_mean, distances_sum, iteration


