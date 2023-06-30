#import libraries
import numpy as np

####################################################

class OptimisedCondition:
    def __init__(self, array_A, array_B, shift):
        self.array_A = np.array(array_A)
        self.array_B = np.array(array_B)
        self.shift = shift
        self.opt_array_B = self.optimised_B()

############
    def optimised_B(self):
        # Computes optimised array
        return self.array_B + self.shift



    def compute_distances(self):
        # Computes dist per point along two arrays
        return np.linalg.norm(self.array_A - self.opt_array_B, axis=1)



    def optimised_distances(self):
        #Computes optimised condition in terms of mean dist & tot dist
        distances = self.compute_distances()
        print(f"The optimised mean distance is {np.mean(distances):.3f} mm")
        print(f"The optimised total distance is {distances.sum():.3f} mm")
        return np.mean(distances),distances.sum()



    def points_direction (self):
        #identifies if a new optimised coords are closest or furthest than reference
        distances = self.compute_distances()
        for i in range(len(distances)):
            # determines if shifted point is closess to origin
            k = np.linalg.norm(self.array_A[i]) - np.linalg.norm(self.array_B[i])
            if k < 0:
                # neg = -1; for corresponding distances of shifted points
                distances[i] = distances[i] * (-1)
        return distances

