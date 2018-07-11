from population import population
from read_csv import csv
from tkinter import *

window = Tk()
window.title("testing")

theLabel = Label(window, text="This is a label")
theLabel.pack()

"""Dyanmic Button Creation Loop"""
def printName(i):
    print ("Printing because u clicked on me. Button no: %s" %i)

buttons = [i for i in range(10)]
list = []

for i in range(len(buttons)):
    btn = Button(window, text=buttons[i], command=lambda i=i: printName(i))
    btn.pack()


window.mainloop()
