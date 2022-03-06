import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

csv = 'https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/cases.csv'
df = pd.read_csv(csv)
# Πρώτος πίνακας
plt.plot(df.loc[: , "date"] ,df.loc[:,"new_deaths"],color = "green", linewidth = 2)
plt.title("Εξέλιξη Ανθρώπινων Απωλειών")
plt.xlabel("Ημερομηνία")
plt.ylabel("Πλήθος απωλειών")
plt.show()

#Δεύτερος πίνακας
df = df.loc[::-1].reset_index(drop=True).head()
plt.bar(df.loc[:1,"date"],df.loc[:1,'new_cases'],color = "green")
plt.title("Νέα Περιστατικά")
plt.xlabel("Ημερομηνία")
plt.ylabel("Πλήθος νέων περιστατικών")
plt.show()



#change

# class Root(Tk):
#     def __init__(self):
#         super(Root, self).__init__()
#         self.title("Tkinter Matplotlib Embeding")
#         self.minsize(640,400)
#         self.wm_iconbitmap('plt.plot')
#
#
#     def matplotCanvas(self):
#         f = Figure(size=(5,5), dpi = 100)
#         a = f.add_subplot(111)
#         a.plot([df.loc[:,"date"],df.loc[:,"new_deaths"]])
#
#         canvas = FigureCanvasTkAgg(f,self)
#         canvas.show()
#         canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
#
# if __name__=='__main__':
#     root = Root()
#     root.mainloop()
