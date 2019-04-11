import tkinter as tk

class textinputs:

    def __init__ (self):
        window = Tk()
        window.title("Calculation")
        window.geometry("400x200")                          #ractangle size


        frame1 = Frame(window)
        frame1.pack()

        self.name = StringVar(window,value='')
        self.entryName = Entry(frame1, textvariable = self.name, width = 45)
        self.entryName.grid(row = 1, column = 1)




textinputs()

'''
window = tk.Tk()
window.title("Calculation")
window.geometry("400x200")                          #ractangle size


frame1 = tk.Frame(window)
frame1.pack()

name = tk.StringVar(window,value='')
entryName = tk.Entry(frame1, textvariable = name, width = 45)
entryName.grid(row = 1, column = 1)

window.mainloop()
'''