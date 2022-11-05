import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax=plt.subplots()
    ax.scatter=plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extend=np.arange(1880, 2051, 1)
    line = [fit.slope*xi + fit.intercept for xi in extend]
    plt.plot(extend, line, color = 'red')
    plt.xticks(range(1850, 2100, 25))

    # Create second line of best fit
    new_df=df.loc[df['Year'] >= 2000]
    new_fit = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])

    new_extend=np.arange(2000, 2051, 1)
    new_line = [new_fit.slope*xi + new_fit.intercept for xi in new_extend]
    plt.plot(new_extend, new_line, color = 'orange')
    plt.xticks(range(1850, 2100, 25))

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()