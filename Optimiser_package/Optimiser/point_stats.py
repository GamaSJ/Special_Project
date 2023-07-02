#import libraries
import numpy as np
import pandas as pd

#######################
class PointStats:
    """
    Computes metrics for a givenset of points of interest

    Attributes:
        database (Dataframe): global data
        points_list (list): points of interest
    """
    def __init__(self, database, points_list):
        """
        Initialise the computation of metrics for points of interest

        Args:
            database (Dataframe): global data
            points_list (list): points of interest

        """

        self.database = database
        self.points_list = points_list


    def point_stats (self):
        """
        Identifies points of interest and computes its metrics

        Return:
             DataFrame: metrics of points of interest
        """
        df = self.database

        df3 = df[self.points_list].describe(percentiles=[])
        return df3
