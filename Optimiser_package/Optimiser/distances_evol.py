# import libraries
import numpy as np
import matplotlib.pyplot as plt


#########################################
class DistanceEvolution:
    """
    Evolution of distances between arrays as per solver

    Attributes:
        mean_distances (np.array): mean distance between points for each iteration
        total_distances (np.array): total distance between points for each iteration
    """


    def __init__(self, mean_distances, total_distances):
        """
        Initialises the graphical representaiton of distances' evolution

        Args:
            mean_distances (np.array): mean distance between points for each iteration
            total_distances (np.array): total distance between points for each iteration
        """


        self.mean_distances = mean_distances
        self.total_distances = total_distances



    def evol_mean_dist(self):
        """
        Visual representation of evolution of sitances

        Return:
             Plot: distances per iteration
        """


        #Plots the evolution of the minimisation algo (mean dist & tot dist)
        print("The evolution of mean & total distances per iteration is shown in the picture")
        #define x, y1 & y2
        x = range(1, len(self.mean_distances) + 1)
        y1 = self.mean_distances
        y2 = self.total_distances

        #assign vars to plots
        fig, ax = plt.subplots(figsize=(10, 5))
        ax2 = ax.twinx()
        ax.plot(x, y1, 'o:r')
        ax2.plot(x, y2,'x--b')

        # labels for 1st axis
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Mean distances, mm', color='r')
        # label for 2nd axis
        ax2.set_ylabel('Total distances, mm', color='b')

        plt.title('Distance evolution')
        plt.show()

