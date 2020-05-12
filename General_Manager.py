from tkinter import *

# Application Window

Application = Tk()
Application.title("3's General Manager 2020")
Application.resizable(0,0)
Application.geometry('800x800')


# Main Frame (Background)
Main = Frame(master=Main, width=800, height=800, background='#ADD8E6')
Main.grid(row=0,column=0)

# First Save Slot Button (max three games)
Save_1 = Button(master=Main, text='Save 1', height=10, width=50, background='#808080')
Save_1.grid(row=1,sticky='N')

# Second Save Slot Button Button
Save_2 = Button(master=Application, text='Save 2', height=10, width=50, background='#808080')
Save_2.grid(row=2,sticky='N')

# Third Save Slot Button
Save_3 = Button(master=Main, text='Save 3', height=10, width=50, background='#808080')
Save_3.grid(row=3,sticky='N')


# Start program
Application.mainloop()






