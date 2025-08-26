

import numpy as np
from scipy.stats import t

# Define a function to apply the t-test to each pixel
def ttest_ind_from_stats_pixel(mean1, std1, nobs1, mean2, std2, nobs2):
    t_stat, p_value = stats.ttest_ind_from_stats(mean1, std1, nobs1, 
                                                 mean2, std2, nobs2, 
                                                 equal_var=False, alternative='two-sided')
    return t_stat, p_value

 
def ttest_xr(mean1, std1, nobs1, mean2, std2, nobs2):
    # Use xr.apply_ufunc to apply this function element-wise across the arrays
    t_stat, p_value = xr.apply_ufunc(
        ttest_ind_from_stats_pixel, 
        mean1, std1, nobs1, 
        mean2, std2, nobs2,
        input_core_dims=[[], [], [], [], [], []],  # No core dimensions; apply to each element
        output_core_dims=[[], []],                 # Output is a scalar for each pixel
        vectorize=True                             # Apply element-wise
    )
    return t_stat, p_value

def welchs_ttest_array(mean1, std1, n1, mean2, std2, n2):

    mean1, std1, n1 = np.array(mean1), np.array(std1), np.array(n1)
    mean2, std2, n2 = np.array(mean2), np.array(std2), np.array(n2)
    
    numerator = mean1 - mean2
    denominator = np.sqrt((std1**2 / n1) + (std2**2 / n2))
    t_stat = numerator / denominator

    v1 = (std1**2 / n1)
    v2 = (std2**2 / n2)
    df = ((v1 + v2)**2) / ((v1**2 / (n1 - 1)) + (v2**2 / (n2 - 1)))

    return t_stat, df

def calculate_pvalue_array(t_stat, df):
    # Calculate two-sided p-values
    p_values = 2 * t.sf(np.abs(t_stat), df)
    return p_values

def fdr_threshold(pvalues, alpha=0.05):
    """Calculate the FDR threshold following Wilks (2016)"""
    pvals_sorted = np.sort(np.asarray(pvalues).flatten())
    N = len(pvals_sorted)
    return np.max(np.where(pvals_sorted <= (np.arange(1, N+1) / N * alpha), pvals_sorted, 0))