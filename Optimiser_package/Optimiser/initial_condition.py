#import libraries
import numpy as np

#########################################
class InitialCondition:
    """
    Evaluation of initial condition of arrays

    Attributes:
        array_A (np.array): reference array
        array_B (np.array): array under study
    """
    def __init__(self, array_A, array_B):
        """
        Initialises the evaluation of the initial condition as-is between two arrays

        Args:
            array_A (np.array): considered as the reference
            array_B (np.array): array under stuay

        """
        self.array_A = np.array(array_A)
        self.array_B = np.array(array_B)


############
    def compute_distances(self):
        """
        Computes distance between arrays

        Return:
             np.array: distances between points along array
        """

        return np.linalg.norm(self.array_A - self.array_B, axis=1)



    def initial_distances(self):
        """
        Computes initial condition between arrays: mean dist & tot dist

        Return:
             mean distance & total distances
        """

        distances = self.compute_distances()
        print(f"The initial mean distance is {np.mean(distances):.3f} mm")
        print(f"The initial total distance is {distances.sum():.3f} mm")
        return np.mean(distances),distances.sum()



    def points_direction (self):
        """
        Identifies if coords are closest or furthest than reference

        Return:
             np.array: offset per point
        """

        distances = self.compute_distances()
        for i in range(len(distances)):
            # determines if shifted point is closess to origin
            k = np.linalg.norm(self.array_A[i]) - np.linalg.norm(self.array_B[i])
            if k < 0:
                # neg = -1; for corresponding distances of shifted points
                distances[i] = distances[i] * (-1)
        return distances

