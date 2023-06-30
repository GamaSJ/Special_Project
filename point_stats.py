#import libraries
import numpy as np
import pandas as pd

#######################
class PointStats:
    def __init__(self, database, points_list):
        self.database = database
        self.points_list = points_list


    def point_stats (self):
        #Computes the metrics for a given list of points of interest
        df = self.database

        df3 = df[self.points_list].describe(percentiles=[])
        return df3
