import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    df.rename(columns={"paYear": "Year"}, inplace=True)
    # Create scatter plot
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]
    plt.figure(figsize=(10, 6))
    plt.scatter(x,y,color="blue", alpha=0.6, label="Data")
    # Create first line of best fit
    #Perform linear regression
    slope_all, intercept_all = linregress(x, y)

    years_extended = pd.Series(range(int(x.min()), 2051))
    #predicted sea levels
    sea_levels_pred = intercept_all + slope_all * years_extended
    plt.plot(years_extended, sea_levels_pred, color="red", label="Line of Best Fit")

    # Create second line of best fit
    df_recent = df[x >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = intercept_recent + slope_recent * years_recent
    plt.plot(years_recent, sea_level_recent, color="green", label="Fit: 2000+ Data")


    # Add labels and title
    
    plt.xlabel("Year")  
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()