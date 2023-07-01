#import libraries
import numpy as np
import pandas as pd

#######################
class CasesComp:
    """
    Compares offset data (init vs opt).

    Attributes:
        databaset_init (dataframe): Databese with initial condition
        database_opt (dataframe): Database with opt condition
        case (str): case under study
    """
    def __init__(self, database_init, database_opt, case):
        """
        Initialises the comparison for given case

        Args:
            databaset_init (DataFrame): Databese with initial condition
            database_opt (DataFrame): Database with opt condition.
            case (str): case under study
            df_init (DataFrame): Data of points of interest for given case -init
            df_opt (DataFrame): Data of points of interest for given case - opt

        """
        self.database_init = database_init
        self.database_opt = database_opt
        self.case = case
        self.df_init = self.case_comp_init()
        self.df_opt = self.case_comp_opt()


    def case_comp_init (self):
        """
        Refines the database from initial data
        Extracts the initial condition data corresponding to a given case

        Return:
             DataFrame: points of interest - init
        """

        df_init = self.database_init.set_index(['Identifier'])
        return df_init.loc[self.case]


    def case_comp_opt (self):
        """
        Refines the database from optimise data
        Extracts the optimised condition data corresponding to a given case

        Return:
             DataFrame: points of interest opt
        """
        df_opt = self.database_opt.set_index(['Identifier'])
        return df_opt.loc[self.case]


    def comparison (self):
        """
        Compares both before & after data

        Return:
             Dataframe: points of interest for given case
        """
        comparison = [self.df_init, self.df_opt]
        return pd.concat(comparison,axis = 1)
