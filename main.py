import Optimiser

#Get Data, user should write Filename i.e. 'Part_02.csv'
ref_coords, init_coords = Optimiser.get_data('Part_79.csv')

#Starting Condition, will compute distances & direction of the offset
starting_condition = Optimiser.InitialCondition(ref_coords,init_coords)
initial_distances = starting_condition.initial_distances()
starting_direction = starting_condition.points_direction()

#Process File using Gradient Descend
solver_results = Optimiser.gradient_descent(ref_coords,init_coords,max_iterations=5000,learning_rate=0.1, shift_limit=0.5,stop_criteria=1e-6)
#Plot the evolution of the solver
Optimiser.DistanceEvolution(solver_results[1],solver_results[2]).evol_mean_dist()#Plot

#Optimised Condition - Shift. Computing optimised distance & direction of the offset
optimised_condition = Optimiser.OptimisedCondition(ref_coords,init_coords,solver_results[0])
optimised_distance = optimised_condition.optimised_distances()
optimised_direction = optimised_condition.points_direction()

#Offset Direction Comparison Bef VS Aft with regards to 0 - Plot
Optimiser.OffsetDirection(starting_direction,optimised_direction).offset_direction()#Plot

# V&V using Scipy CG
vv_results_CG = Optimiser.minimize_dist_CG(ref_coords,init_coords,max_iterations=5000,stop_criteria=1e-6)
print(f"Shift differences between coded solver & scipyCG is :{(solver_results[0] - vv_results_CG)} mm")
# V&V using Scipy BFGS
vv_results_BFGS = Optimiser.minimize_dist_BFGS(ref_coords,init_coords,max_iterations=5000,stop_criteria=1e-6, stop_tolerance=1e-6)
print(f"Shift differences between coded solver & scipyBFGS is :{(solver_results[0] - vv_results_BFGS)} mm")

#Minimising using Scipy BFGS (with Rotation)
min_shift_rot_BFGS = Optimiser.minimize_dist_rot_BFGS(ref_coords,init_coords,max_iterations=5000,stop_criteria=1e-6, stop_tolerance=1e-3)

#Updating Database with initial & optimised values
#User should write case i.e. 'Part_02'
database = Optimiser.DataUpdate(starting_direction,optimised_direction,case='Part_79', material='Material1', side='R')
data_initial = database.initial_data()
data_optimised = database.optimised_data()

#Checking metrics for multiple points in the global database for initial & optimised
#User should write a list of points to check (i.e. ["Point_1", "Point_15"])
point_stats_init = Optimiser.PointStats(data_initial,points_list=["Point_1", "Point_2", "Point_20"])
point_stats_opt = Optimiser.PointStats(data_optimised,points_list=["Point_1", "Point_2", "Point_20"])

print("Points metrics in their initial condition are as follow")
print(point_stats_init.point_stats())
print("Points metrics once optimised are as follow")
print(point_stats_opt.point_stats())

# Checking offset for a given case
#User should write a case to check (i.e. 'Part_55'])
case = Optimiser.CasesComp(data_initial, data_optimised, case='Part_50')
print("Offset distances before & after are as follow")
print(case.comparison())