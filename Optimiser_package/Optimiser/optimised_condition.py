#import libraries
import numpy as np

####################################################

class OptimisedCondition:
    """
    Evaluation of optimised condition of arrays

    Attributes:
        array_A (np.array): reference array
        array_B (np.array): array under study
        shift (np.array): optimised shift
    """
    def __init__(self, array_A, array_B, shift):
        """
        Initialises the evaluation of the optimised condition

        Args:
            array_A (np.array): considered as the reference
            array_B (np.array): array under stuay
            shift (np.array): optimised shift

        """
        self.array_A = np.array(array_A)
        self.array_B = np.array(array_B)
        self.shift = shift
        self.opt_array_B = self.optimised_B()

############
    def optimised_B(self):
        """
        Computes optimised arrays by applying shift to array B

        Return:
             np.array: distances between points along array
        """
        return self.array_B + self.shift



    def compute_distances(self):
        """
        Computes distance between arrays

        Return:
             np.array: distances between points along array
        """
        return np.linalg.norm(self.array_A - self.opt_array_B, axis=1)



    def optimised_distances(self):
        """
        Computes optimised condition between arrays: mean dist & tot dist

        Return:
             mean distance & total distances
        """
        distances = self.compute_distances()
        print(f"The optimised mean distance is {np.mean(distances):.3f} mm")
        print(f"The optimised total distance is {distances.sum():.3f} mm")
        return np.mean(distances),distances.sum()



    def points_direction (self):
        """
        Identifies if optimised coords are closest or furthest than reference

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

