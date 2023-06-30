#import libraries
import numpy as np
from scipy.spatial.transform import Rotation as R
import time

#########################################

def compute_distances(array_A, array_B):
    # Computes dist per point along two arrays
    return np.linalg.norm(array_A - array_B, axis=1)

def gradient_descent (array_A, array_B,max_iterations,learning_rate, shift_limit, stop_criteria):
    #Coded algorithm to minimise distance between two arrays.
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



#gradient descent for rotation is not activated in the case herein
#Scipy is included though
def gradient_descent_rot(self):# array_A, array_B, max_iterations, learning_rate_rot, shift, stop_criteria):
    start_time = time.perf_counter()  # for the time measurement

    angles = np.zeros(3)  # Initial Euler angles in rad
    distances_rot_mean = []  # List to store distances per iteration
    distances_rot_sum = []  # List to store distances_sum per iteration
    ref_distance = float('inf')  # large number

    array_Bshifted = array_B + shift #apply shift before loop rot

    for iteration in range(max_iterations):
        r = R.from_euler('xyz', angles)
        array_Brotated = r.apply(array_Bshifted)

        distances = compute_distances(array_A, array_Brotated)
        gradient = -1 * np.mean((arr1 - arr2_transformed) / distances[:, np.newaxis], axis=0)

        angles -= learning_rate_rot * gradient  # Update Euler angles, must be updatedseparately

        distances_rot_mean.append(np.mean(distances))
        distances_rot_sum.append(distances.sum())

        if abs(distances.sum()-ref_distance) <= stop_criteria:
            break

        ref_distance = distances.sum()  # update variable for next iteration

    if distances_rot_mean[0] <= distances_rot_mean[-1]:
        angles = np.zeros(3)

    end_time = time.perf_counter()  # for the time measurement
    solver_time = end_time - start_time
    print(f"The shift solver did {iteration} iterations")
    print(f"The solver took {solver_time:.3f} seconds")
    print(f"The solver found the following optimised combination of angles {angles} in rad")
    print(f"The minimum mean distance at opt shift is {distances_rot_mean[-1]} mm")
    print(f"The minimum total distance at opt shift is {distances_rot_sum[-1]} mm")

    return angles, distances_rot_mean, distances_rot_sum



