#Budget stored in "budget"
#Image source stored in "imageDest"
#import Starter.py
from tkinter import *
from tkinter import filedialog

import user_scraper
from Starter import infoGen, starter_images

root = Tk()
root.title("Target Market")
root.geometry('720x500')
theLabel = Label(root, text="Target Market", bg="black", fg="white", font=("Arial Black", 20))
theLabel.grid(row=0,column=0,columnspan=5)
theLabel = Label(root, text="Get a target market for optimum advertising", bg="grey", fg="white", font=("Arial Black", 13))
theLabel.grid(row=1,columnspan=5)

budget=1
imageDest="address"
#------------------------FUNCTIONS-------------------------------------------
listLabels=[]
def fileOpen():
    global imageDest
    global listLabels
    imageDest=filedialog.askopenfilename(title="Select an image")
    message = Label(text=imageDest, fg="grey").grid(row=5, columnspan=4)
    listLabels = starter_images(imageDest)

def getBudget():
    global budget
    budget=budgetentry.get()
    message1="The program is running for the budget "+budget+"."
    message = Label(text=message1).grid(row=7, columnspan=4)
    displayLabels()
    #starter_image(imgDest)

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


#-------------------------------------------------------------------------------------------------GUI ENDS-----------------------------------------


labelsString=""
labelentry = Entry(root)
def displayLabels():
    messageLabels = Label(root, text="The following are the labels your product is associated with:",font=("Arial", 11))
    messageLabels.grid(row=8, columnspan=5, pady=30)
    for i in range(listLabels.__len__()):
        global labelsString
        labelsString+=listLabels[i]+" ,"
    messageLabels = Label(root, text=labelsString,font=("Arial", 11), bg="grey", fg="white")
    messageLabels.grid(row=9, columnspan=5, pady=15)

    messageLabels = Label(root, text="Enter the labels you wish to use separated by spaces", font=("Arial", 11))
    messageLabels.grid(row=10, columnspan=5, pady=15)

    labelentry.grid(row=11, column=0, columnspan=9)

    SubmitLabel = Button(text="SUBMIT", bg="black", fg="white",  command=labelEdit)
    SubmitLabel.grid(row=12, columnspan=4, pady=5)

labelsStringUpdated=""
listLabels1=[]

def labelEdit():
    global labelsStringUpdated
    labelsStringUpdated=labelentry.get()
    listLabels1=labelsStringUpdated.split(" ")
    userlist = [] # accounts
    for i in listLabels1:
        userlist.append(infoGen(listLabels1))
    print("Userlist:")
    print(userlist)
    print("Program Finished")


# listLabelsUpdated=labelsStringUpdated.split()
# print(listLabelsUpdated)
# print(labelsStringUpdated)

root.mainloop()
