from tkinter import*
from MySQLdb import DatabaseError
from PIL import Image,ImageTk

import addemployee
import viewaddemployee
import addtask
import viewaddtask
import viewassigntask
import reports
import assigntasks
import addproject
import viewaddproject
import database

class createhome_menu:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Home Menu')

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

        self.my_label=Label(self.root,text="WELCOME!",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=25,y=30,width="170")

        self.EmpLabel = Label(self.mainFrame, text="Employees",font=("Mongolian Baiti",16))
        self.EmpLabel.place(x = 10, y = 100, width="100")

        self.EmpnoLabel = Label(self.mainFrame, text=len(database.nameEmp()),font=("Mongolian Baiti",16))
        self.EmpnoLabel.place(x = 130, y = 100, width="30")

        self.ProjectLabel = Label(self.mainFrame, text="Projects",font=("Mongolian Baiti",16))
        self.ProjectLabel.place(x = 0, y = 150, width="100")

        self.ProjectnoLabel = Label(self.mainFrame, text=len(database.allProjects()),font=("Mongolian Baiti",16))
        self.ProjectnoLabel.place(x = 130, y = 150, width="30")

        self.TaskLabel = Label(self.mainFrame, text="All Tasks",font=("Mongolian Baiti",16))
        self.TaskLabel.place(x = 0, y = 200, width="100")

        self.TasknoLabel = Label(self.mainFrame, text=len(database.allTask()),font=("Mongolian Baiti",16))
        self.TasknoLabel.place(x = 130, y = 200, width="30")

        # self.CompletedLabel = Label(self.mainFrame, text="Completed",font=("Mongolian Baiti",16))
        # self.CompletedLabel.place(x = 5, y = 300, width="100")

        # self.CompletedLabel = Label(self.mainFrame, text=len(database.completedTask()),font=("Mongolian Baiti",16))
        # self.CompletedLabel.place(x = 130, y = 300, width="30")


        
        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/menuimg.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 250 , y = 0,  width="600", height = "500")

        
    
        menubar=Menu(self.mainFrame)
        
        #adding self.employee menu and commands
        employee=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Employee",menu=employee)
        employee.add_command(label="Add",command=self.openAddEmp)
        employee.add_command(label="Manage",command=self.openViewAddEmp)

        project=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Project",menu=project)
        project.add_command(label="Add",command=self.openAddpro)
        project.add_command(label="Manage",command=self.openViewAddpro)

        #adding self.task menu and commands
        task=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Task",menu=task)
        task.add_command(label="Add",command=self.openAddTask)
        task.add_command(label="Manage",command=self.openViewAddTask)


        assignTask=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Assign Task",menu=assignTask)
        assignTask.add_command(label="Add",command=self.openAddassignTask)
        assignTask.add_command(label="Manage",command=self.openViewAddassignTask)

        #adding feedback menu and commands
        feedback=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Reports",menu=feedback)
        feedback.add_command(label="View",command=self.openViewReports)

        menubar.add_command(label='logout',command=self.root.quit)
        self.root.config(menu=menubar)
        self.root.mainloop()

    def openAddEmp(self):
        self.root.destroy()
        obj = addemployee.createAddEmployee()
        obj.firstFrame()

    def openViewAddEmp(self):
        self.root.destroy()
        obj = viewaddemployee.viewAddEmployee()
        obj.manageEmployee()

    def openAddTask(self):
        self.root.destroy()
        obj = addtask.createAddTask()
        obj.firstFrame()
        

    def openViewAddTask(self):
        self.root.destroy()
        obj = viewaddtask.viewAddTask()
        obj.manageTask()
    
    def openAddpro(self):
        self.root.destroy()
        obj = addproject.createAddProject()
        obj.firstFrame()
    
    def openViewAddpro(self):
        self.root.destroy()
        obj = viewaddproject.viewAddProject()
        obj.manageTask()
        
    def openAddassignTask(self):
        self.root.destroy()
        obj = assigntasks.createAddTask()
        obj.firstFrame()

    def openViewAddassignTask(self):
        self.root.destroy()
        obj = viewassigntask.viewAssignTask()
        obj.manageTask()
        
    # def openViewFeedback(self):
    #     self.root.destroy()
    #     obj = viewfeedback.viewFeedback()
    #     obj.manageFeedback()

    def openViewReports(self):
        self.root.destroy()
        obj = reports.reportMenu()
        obj.firstFrame()
        
    
if __name__=="__main__":
     obj=createhome_menu()
     obj.firstFrame()
