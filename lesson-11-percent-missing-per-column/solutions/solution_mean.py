import numpy as np
import pandas as pd

def percent_missing_per_column(dframe):
    return dframe.isna().mean() * 100 
