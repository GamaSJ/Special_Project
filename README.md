# Special_Project

This depository contains a Py code that aims to minimise the distance between two sets of 3D coordinates.
In principle, the code should find the idealised adjustments for a given set of 3D coordinates with regards to an idealised envelope
Overal description of the files as follow, for moore details see comments along the code lines:


  A) main
  
  	Calls up the different modules
   	A working example is included in the file

B)Minimisation

  
	  datasets_call - gets data from file
	  gradient_descent - coded algo
	  initial_condition - reference initial values
	  distances_evol - evolution of distances (plot)
	  offset_direction - offset of given points with regards to ideal (plot)
	  optimised_condition - computes solution found
	  minimise_BFGS- scipy - robust comparison


 C)VV - verification & validation using scipy

  
	  vv_shift_BFGS - shift verification with BFGS
	  vv_shift_CF - shift verification with BFGS

D) Data comparison & manipulation


	   cases_comparison - compares cases
	   data_update - feeds databas   
	   points_stats


Test_dummy files with data for working test samples are included in this depositoty


GS









