# import libraries
import numpy as np
import matplotlib.pyplot as plt

#########################################
class OffsetDirection:
    def __init__(self, initial_direction, optimised_direction):
        self.initial_direction = initial_direction
        self.optimised_direction = optimised_direction


    def offset_direction(self):
        #Plots the offset direction (where 0 represents ideal geom)
        print("The offset before and after adjustment is shown in the picture")
        plt.figure(figsize=(10, 5))
        plt.axhline(y=0.0, color='r', linestyle='--')
        plt.scatter(range(1, len(self.initial_direction) + 1), self.initial_direction)
        plt.scatter(range(1, len(self.optimised_direction) + 1), self.optimised_direction)

        #labels & Title
        plt.xlabel('Point')
        plt.ylabel('Offset, mm')
        plt.legend(["Ref","Original Offset", "New Offset"])
        plt.title('Offset per point')

        #Grid
        plt.grid(axis='x')

        plt.show()
