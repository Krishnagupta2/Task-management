from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import homemenu
import viewaddtask
import viewassigntask
import database


class createAddTask:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Assign Task')

        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        

    def firstFrame(self):

        # create a frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.root,text="Assign Tasks",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=30,width="200")


        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/taskimg.webp'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "500")

        self.EmpIdLabel = Label(self.mainFrame, text="Emp Id",font=("Mongolian Baiti",16))
        self.EmpIdLabel.place(x = 15, y = 100, width="120")

        self.emp = database.nameEmp()
        self.empName = StringVar()
        self.EmpIdEntry = ttk.Combobox(self.mainFrame,value=self.emp, textvariable=self.empName)
        self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)        
        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)
        self.Taskname = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.Taskname.place(x = 30, y = 150, width="120")

        self.Task = database.nameTask()
        self.TaskName = StringVar()
        self.TasknameEntry = ttk.Combobox(self.mainFrame,value=self.Task, textvariable=self.TaskName)
        self.TasknameEntry.place(x = 150, y = 150, width="150",height=30)

        self.StartdateLabel = Label(self.mainFrame, text="Start Date",font=("Mongolian Baiti",16))
        self.StartdateLabel.place(x = 25, y = 200, width="120")

        self.startData = StringVar()
        self.StartdateEntry = DateEntry(self.mainFrame, textVariable = self.startData,date_pattern='yyyy-MM-dd')
        self.StartdateEntry.place(x = 150, y = 200, width="150",height=30)

        self.EnddateLabel = Label(self.mainFrame, text="End Date",font=("Mongolian Baiti",16))
        self.EnddateLabel.place(x = 25, y = 250, width="120")

        self.endData = StringVar()
        self.EnddateEntry = DateEntry(self.mainFrame, textVariable = self.endData,date_pattern='yyyy-MM-dd')
        self.EnddateEntry.place(x = 150, y = 250, width="150",height=30)
       

        self.submit = Button(self.mainFrame, text = "Submit", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.submit.place(x = 50, y = 320, width="70")
        
        self.backBtn=Button(self.mainFrame,text="Back",font=("Mo-ngolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=320,width="70",height=40)
        
        self.root.mainloop()

    def create(self):
        self.data = [
            self.empName.get(), 
            self.TasknameEntry.get(),  
            self.StartdateEntry.get(),
            self.EnddateEntry.get(),
            'pending'
        ]
        print(self.data)
        if (self.empName.get() == ''):
            messagebox.showinfo('Alert', 'Enter your EmpId.')
        elif self.TasknameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Task Name.')
        elif self.StartdateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Start Date.')
        elif self.EnddateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your End Date.')
        else:
            res = database.assigntask(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.root.destroy()
                obj = viewassigntask.viewAssignTask()
                obj.manageTask()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')



    def back(self):
        self.root.destroy()
        obj = homemenu.createhome_menu()
        obj.firstFrame()




if __name__ == '__main__':
    obj = createAddTask()
    obj.firstFrame()