import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  fig,ax = plt.subplots(1,figsize  =(15,8))
  plt.scatter(data = df , x='Year', y='CSIRO Adjusted Sea Level')
    # Create first line of best fit
  
  lineA = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  xA = np.arange(df['Year'].min(),2051,1)
  yA = lineA.intercept + lineA.slope*xA
  plt.plot(xA,yA,color = 'red')

    # Create second line of best fit
  df_since_2000 = df.loc[df.Year >= 2000]
  lineB = stats.linregress(df_since_2000['Year'], df_since_2000['CSIRO Adjusted Sea Level'])
  xB = np.arange(df.loc[df.Year >= 2000,'Year'].min(),2051,1)
  yB = lineB.intercept + lineB.slope * xB
  plt.plot(xB,yB,color = 'green')

    # Add labels and title
  ax = plt.gca()
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
  ax.set_xlim(1850, 2075)
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()