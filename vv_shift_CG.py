#import libraries
import numpy as np
from scipy.optimize import minimize
import time

#######################

def distance(array_A, array_B):
    # Mean distance along array of points
    return np.mean(np.linalg.norm(array_A - array_B, axis=1))#mean distance along array of points


def objective(shift, array_A, array_B):
    # Computes a shifted geometry, then calls the distance func
    shifted_B = array_B + shift
    return distance(array_A, shifted_B)


def minimize_dist_CG(array_A, array_B, max_iterations, stop_criteria):
    # Minimisation of distance between two array while considering shift
    # Uses Scipy BFGS
    start_time = time.perf_counter()  # for the time measurement

    initial_guess = np.zeros(3) # Initial guess for the shift

    # Define the objective function
    obj_func = lambda shift: objective(shift, array_A, array_B)

    # Call scipy.optimize.minimize
    result = minimize(obj_func, initial_guess, method='CG', options={'maxiter':max_iterations, 'gtol':stop_criteria})

    iteration = result.nit # Retrieve number of iterations
    optimized_shift = result.x # Retrieve the optimized shift
    final_distance = result.fun  # Retrieve the final mean distance

    end_time = time.perf_counter()#for the time measurement
    solver_time = end_time - start_time

    print(f"Using scipy CG, minimisation requires {iteration} iterations")
    print(f"Optimised shift is then :{np.around(optimized_shift, decimals=3)} for x, y & z coordinates")
    print(f"The minimum mean distance with this solver is :{final_distance:.3f} mm")
    print(f"The solver took {solver_time:.3f} seconds")

    return optimized_shift


