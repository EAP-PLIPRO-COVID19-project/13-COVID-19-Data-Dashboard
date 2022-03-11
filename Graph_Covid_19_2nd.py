import tkinter as tk
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.

csv = 'https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/cases.csv'
data1 = pd.read_csv(csv)
df1 = DataFrame(data1, columns=['date', 'new_deaths'])

data2= data1.loc[::-1].reset_index(drop=True).head()
data3 = {'date': data2.loc[:1,"date"], 'new_cases': data2.loc[:1,'new_cases']}
df2 = DataFrame(data3, columns=["date", 'new_cases'])

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
line1 = FigureCanvasTkAgg(figure1, root)
line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['date', 'new_deaths']].groupby('new_deaths').sum()
df1.plot(kind='line', legend=True, ax=ax1)
ax1.set_title('date vs new_deaths')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, root)
bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['date', 'new_cases']].groupby('date').sum()
df2.plot(kind='bar', legend=True, ax=ax2)
ax2.set_title('date vs new_cases')
add_value_labels(ax2)


root.mainloop()





















