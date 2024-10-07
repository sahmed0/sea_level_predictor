import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')
    
    # First line of best fit (1880 to 2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    years_extended = np.arange(1880, 2051)
    sea_levels_extended = slope * years_extended + intercept
    
    # Second line of best fit (2000 onwards)
    df_recent = df[df['Year'] >= 2000]  # Filter data for years from 2000 onwards
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = np.arange(2000, 2051)
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')
    plt.plot(years_extended, sea_levels_extended, label='Best Fit Line (1880-2050)', color='green')
    plt.plot(years_recent, sea_levels_recent, label='Best Fit Line (2000-2050)', color='orange')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()