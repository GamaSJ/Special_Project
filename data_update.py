#import libraries
import numpy as np
import pandas as pd

#######################
class DataUpdate:
    """
    Database updates for init and opt

    Attributes:
        init_condition (np.array): results from starting condition
        opt_condition (np.array): results from minimisation
        case (str): case under study
        material (str): material
        side (str): characteristic
    """
    def __init__(self, init_condition,opt_condition, case, material, side):
        """
        Initialise the update of databases based on results

        Args:
            init_condition (np.array): results from starting condition
            opt_condition (np.array): results from minimisation
            case (str): case under study
            material (str): material
            side (str): characteristic


        """


        self.case = case
        self.material = material
        self.side = side
        self.init_condition = init_condition
        self.opt_condition = opt_condition



    def initial_data (self):
        """
        Updates database of initial condition
        #Assumes the existence of a "database" under the name "Bef_dummy.csv"

        Return:
             DataFrame: initial results
        """

        file_name = "Bef_dummy.csv"
        df = pd.read_csv(file_name)

        #Creates new row with data from new case
        row_to_add = pd.DataFrame ({'Identifier':[self.case],'Material':[self.material],'Side':[self.side]})
        #numerical values are added using a loop
        for i in range (len(self.init_condition)):
            point_name = f'Point_{i+1}'
            row_to_add[point_name] = self.init_condition[i]

        #updated dataframe
        df = df._append(row_to_add,ignore_index=True)
        #print(df.iloc[-1]) # print last row
        df.to_csv('Bef_dummy_update.csv',index=False)
        return df




    def optimised_data (self):
        """
        Updates database of opt condition
        Assumes the existence of a "database" under the name "Aft_dummy.csv"

        Return:
             DataFrame: opt results
        """
        file_name = "Aft_dummy.csv"
        df = pd.read_csv(file_name)

        # Creates new row with data from new case
        row_to_add = pd.DataFrame({'Identifier': [self.case], 'Material': [self.material], 'Side': [self.side]})
        # numerical values are added using a loop
        for i in range(len(self.opt_condition)):
            point_name = f'Point_{i + 1}'
            row_to_add[point_name] = self.opt_condition[i]

        # updated dataframe
        df = df._append(row_to_add, ignore_index=True)
        #print(df.iloc[-1]) # print last row
        df.to_csv('Aft_dummy_update.csv', index=False)#save updated databse
        return df
