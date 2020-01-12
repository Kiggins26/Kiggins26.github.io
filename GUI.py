from tkinter import *

root = Tk()
theLabel = Label(root, text="Get a target market to advertise your products.", bg="black", fg="white")
theLabel.pack(fill=X)

#-----------------------FRAMES-----------------------------------------------
topframe = Frame(root)
topframe.pack()
middleframe = Frame(root)
middleframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#------------------------Buttons----------------------------------------------
buttonSubmit = Button(middleframe, text="Submit")
buttonHelp = Button(middleframe, text="Help")

buttonSubmit.pack(side=LEFT)
buttonHelp.pack(side=LEFT)

root.mainloop()


