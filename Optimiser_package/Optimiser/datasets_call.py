#import libraries
import pandas as pd
import numpy as np

################################

def get_data (filename):
    """
    Gets data from a given file.
    User should know filename

    Args:
        filename (str) : given by user, include extension

    Returns:
        np.arrays: two np.array with sets of coordinates (reference & initial)
    """
    df = pd.read_csv(filename, header=None)
    df.columns = ["Label", "Coord_X", "Coord_Y", "Coord_Z", "Measured_X", "Measured_Y", "Measured_Z"]
    original_coords = ["Coord_X", "Coord_Y", "Coord_Z"] # Ref coords
    reference_coordinates = df[original_coords].to_numpy()#convert to np
    measured_coords = ["Measured_X", "Measured_Y", "Measured_Z"] # Measured coords
    initial_coordinates = df[measured_coords].to_numpy()#convert to np

    return reference_coordinates, initial_coordinates