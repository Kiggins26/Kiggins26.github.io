from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Target Market")
theLabel = Label(root, text="Target Market", bg="black", fg="white", font=("Arial Black", 20))
theLabel.grid(row=0,columnspan=5)
theLabel = Label(root, text="Get a target market for optimum advertising", bg="grey", fg="black", font=("Arial Black", 13))
theLabel.grid(row=1,columnspan=5)

#------------------------FUNCTIONS-------------------------------------------
def fileOpen():
    imageDest=filedialog.askopenfile(title="Select an image")
    message = Label(text=imageDest, fg="grey").grid(row=5, columnspan=4)

def getBudget():
    budget=budgetentry.get()
    message1="The program is running for the budget "+budget+"."
    message = Label(text=message1).grid(row=7, columnspan=4)

#------------------------INPUT-----------------------------------------------
budgetLabel=Label(root, text="Enter your budget in CAD")
budgetLabel.grid(row=3)

budgetentry=Entry(root)
budgetentry.grid(row=3, column=3)
#-----------------------------------
budgetLabel=Label(root, text="Select your product image")
budgetLabel.grid(row=4)

buttonInsert = Button(text="INSERT", command=fileOpen)
buttonInsert.grid(row=4, column=3)
#------------------------------------
buttonSubmit = Button(text="SUBMIT", bg="black", fg="white", command=getBudget)
buttonSubmit.grid(row=6, columnspan=4)
#------------------------Buttons----------------------------------------------
# buttonSubmit = Button(middleframe, text="Submit")
# buttonHelp = Button(middleframe, text="Help")
#
# buttonSubmit.pack(side=LEFT)
# buttonHelp.pack(side=LEFT)

root.mainloop()


