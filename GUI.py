from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Target Market")
theLabel = Label(root, text="Get a target market to advertise your products.", bg="black", fg="white")
theLabel.grid(row=0,columnspan=3)

#------------------------FUNCTIONS-------------------------------------------
def fileOpen():
    imageDest=filedialog.askopenfile()
    message = Label(text=imageDest, fg="grey").grid(row=5, columnspan=4)

#------------------------INPUT-----------------------------------------------
budgetLabel=Label(root, text="Enter your budget in CAD")
budgetLabel.grid(row=3)

budget=Entry(root)
budget.grid(row=3, column=3)
#-----------------------------------
budgetLabel=Label(root, text="Select your product image")
budgetLabel.grid(row=4)

buttonInsert = Button(text="INSERT", command=fileOpen)
buttonInsert.grid(row=4, column=3)
#------------------------------------
buttonSubmit = Button(text="SUBMIT", bg="black", fg="white")
buttonSubmit.grid(row=6, columnspan=4)
#------------------------Buttons----------------------------------------------
# buttonSubmit = Button(middleframe, text="Submit")
# buttonHelp = Button(middleframe, text="Help")
#
# buttonSubmit.pack(side=LEFT)
# buttonHelp.pack(side=LEFT)

root.mainloop()


