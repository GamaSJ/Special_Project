##import libraries
import numpy as np
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation as R
import time

#########################

def distance(array_A, array_B):
    #Compute distances between two arrays
    return np.mean(np.linalg.norm(array_A - array_B, axis=1))


def objective(shift, array_A, array_B):
    #Both shift & rotation are applied before computing distances
    shifted_B = array_B + shift[:3]
    r = R.from_euler('xyz', shift[3:])
    transf_B = r.apply(shifted_B)
    return distance(array_A, transf_B)


def minimize_dist_rot_BFGS(array_A, array_B, max_iterations, stop_criteria, stop_tolerance):
    #minize distances between two arrays while considering both shift and rot
    #uses Scipy - BFGS method
    start_time = time.perf_counter()  # for the time measurement
    # Initial guess for the shift
    initial_guess = np.zeros(6)

    # stop_criteria - terminate if gradient norm is less than
    # stop_tolerance - terminate if step size is less than
    # max_iterations - max number of iterations

    # Define the objective function
    obj_func = lambda shift: objective(shift, array_A, array_B)

    # Call scipy.optimize.minimize
    result = minimize(obj_func, initial_guess, method='BFGS', options={'maxiter':max_iterations,'gtol':stop_criteria, 'xrtol':stop_tolerance})

    iteration = result.nit # Retrieve number of iterations
    optimized_adjustment = result.x # Retrieve the optimized adjustment (shift & rot)
    final_distance = result.fun  # Retrieve the final mean distance

    # Apply the shift to array B (first shift, then rotations
    shifted_B = array_B + optimized_adjustment[:3]
    r = R.from_euler('xyz', optimized_adjustment[3:])
    optimized_B = r.apply(shifted_B)

    end_time = time.perf_counter()#for the time measurement
    solver_time = end_time - start_time

    print(f"For comparison, minimisation with scipy BFGS while considering shift & rot requires {iteration} iterations")
    print(f"Optimised shift would be :{np.around(optimized_adjustment[:3], decimals=3)} mm for x, y & z coordinates")
    print(f"Optimised rotation would be :{np.around(optimized_adjustment[3:], decimals=6)} rad")
    print("Note that angular values might be closer to 0, thus difficult to adjust the positioning")
    print(f"The minimum mean distance with this solver is :{final_distance:.3f} mm")
    print(f"The solver took {solver_time:.3f} seconds")

    return optimized_adjustment
