# Imports
import numpy as np
from scipy.stats import pearsonr

# Defining a function which converts the column names to snake_case
def to_snake_case(name):
    ''' Transforms sequence of strings separated by single space to snake_case. 
        If single string is provided, transforms it to lower case. '''
    
    if ' ' in name:
        name = name.replace(' ', '_').lower()
        return name.replace('-', '_')
    return name.lower()

# Defining a function which replaces certain values in a colum
def rplace_col_values(dict, df, col):
    ''' Replaces the values of col in df with dict_values 
        where dict_keys are equal to the current col values. '''
    
    for key, value in dict.items():
        if key in df[col].values:
            df[col].replace(df[df[col] == key][col].values[0], value, inplace = True)

# Defining a function to extract certain column/s from one df in a resulted df
def extract_cols(df, col_names):
    ''' A function which extracts certain column/s from one df in a resulted df.
        Column names are provided as list/array of strings. '''
    return df[col_names]

# Defining a function which returns a dictionary with descriptive results of statistical test of Pearson\'s correlation
def return_significance_test_results_on_corr_coeff(data):
    ''' A function which test Pearson\'s correlation for statistical significance
        and returns string with summary of the result.
        The function takes 2D array as argument.
        Each nested array contains in this order:
        dataframe, independent and dependent variables,
        descriptive name of the correlation and significance level '''
    
    significance_testing_results = {}
    for val in data:
        r, p_value = pearsonr(val[0][val[1]], val[0][val[2]])
        significance_testing_results['{0}: {1} to {2}'.format(val[3], val[1], val[2])] = ('correlation coefficient= ' + str(np.round(r, 2)) + ', p_value= ' + str(np.round(p_value, 7)) +  ', statistically significant: ' + str(p_value < val[4]))
    return significance_testing_results