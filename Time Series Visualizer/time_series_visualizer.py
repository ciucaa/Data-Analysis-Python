import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df=df.set_index('date')
# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,4))
    ax = sns.lineplot(data = df)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month
    df_bar = df.groupby(['month','year']).value.mean()

    # Draw bar plot
    fig = df_bar.unstack(0).plot.bar(xlabel='Years', ylabel='Average Page Views', figsize=(14, 7), fontsize=10).figure
    plt.legend(fontsize=10, labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    #df_box = df.copy()
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    ax0 = sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    ax1 = sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    ax0.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    ax1.set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")
    ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
