#import libraries
import numpy as np
import pandas as pd

#######################
class CasesComp:
    def __init__(self, database_init, database_opt, case):
        self.database_init = database_init
        self.database_opt = database_opt
        self.case = case
        self.df_init = self.case_comp_init()
        self.df_opt = self.case_comp_opt()


    def case_comp_init (self):
        #Extracts the initial condition data corresponding to a given case
        df_init = self.database_init.set_index(['Identifier'])
        return df_init.loc[self.case]


    def case_comp_opt (self):
        # Extracts the optiised condition data corresponding to a given case
        df_opt = self.database_opt.set_index(['Identifier'])
        return df_opt.loc[self.case]


    def comparison (self):
        # Concatenates initial & optimised data
        comparison = [self.df_init, self.df_opt]
        return pd.concat(comparison,axis = 1)
