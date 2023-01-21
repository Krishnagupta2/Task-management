from tkinter import*
from PIL import Image,ImageTk

import viewalltask
import viewpendingtask
import viewcompletedtask
import addfeedback
import viewfeedback
import openProjectTask

import Database


class createEmphomemenu:

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

       
    def firstFrame(self, data, status):
        self.data = data
        print(f'frame {self.data[0]}')
        if status == 'login':
            self.empName = Database.getEmpName(self.data[0])
        else:
            self.empName = self.data[0]
        print(self.empName)
        # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

       
        # set background image
        self.image = ImageTk.PhotoImage(Image.open('image/empmenu1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 300 , y = 0,  width="600", height = "500")

        
    
        menubar=Menu(self.mainFrame)



        self.my_label=Label(self.root,text="TASKS",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=25,y=30,width="170")

        self.TaskLabel = Label(self.mainFrame, text="All Tasks",font=("Mongolian Baiti",16))
        self.TaskLabel.place(x = 10, y = 100, width="100")

        self.TasknoLabel = Label(self.mainFrame, text=len(Database.allEmpTask(self.empName)),font=("Mongolian Baiti",16))
        self.TasknoLabel.place(x = 130, y = 100, width="30")

        self.PendingLabel = Label(self.mainFrame, text="Pending",font=("Mongolian Baiti",16))
        self.PendingLabel.place(x = 10, y = 150, width="100")

        self.PendingLabel = Label(self.mainFrame, text=len(Database.allPendingEmpTask(self.empName)),font=("Mongolian Baiti",16))
        self.PendingLabel.place(x = 130, y = 150, width="30")

        self.CompletedLabel = Label(self.mainFrame, text="Completed",font=("Mongolian Baiti",16))
        self.CompletedLabel.place(x = 15, y = 200, width="100")

        self.CompletedLabel = Label(self.mainFrame, text=len(Database.allCompletedEmpTask(self.empName)),font=("Mongolian Baiti",16))
        self.CompletedLabel.place(x = 130, y = 200, width="30")

        #adding self.task menu and commands
        task=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Task",menu=task)
        task.add_command(label="All Tasks",command=self.openViewAllTask)
        # task.add_command(label="Pending Tasks",command=self.openViewPendingTask)
        # task.add_command(label="Completed Tasks",command=self.openViewCompletedTask)


        project=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Project",menu=project)
        dat = Database.allEmpProject(self.empName)
        taskDic = dict()
        for i in dat:
            if i[3] not in taskDic.keys():
                taskDic[i[3]] = []
            if i[3] in taskDic.keys():
                taskDic.get(i[3]).append(i)
        print(taskDic)
        # dat = list(set(dat))
        # print(" value ",dat)
        for i in taskDic.keys():
            print(i)
            project.add_command(label=i, command= lambda x=i: self.openProjectTask(taskDic[x]))

        menubar.add_command(label='logout',command=self.root.quit)
        self.root.config(menu=menubar)
        self.root.mainloop()

    def openProjectTask(self,data):
        # print("hello",data)
        # self.root.destroy()
        obj = openProjectTask.openProjectTask()
        obj.manageProject(self.empName,data)
        

    def openViewAllTask(self):
        self.root.destroy()
        obj = viewalltask.viewAddTask()
        obj.manageTask(self.empName)
        
    # def openViewPendingTask(self):
    #     self.root.destroy()
    #     obj = viewpendingtask.viewAddTask()
    #     obj.manageTask(self.empName)
    
    # def openViewCompletedTask(self):
    #     self.root.destroy()
    #     obj = viewcompletedtask.viewAddTask()
    #     obj.manageTask(self.empName)
        
    # def openViewAddFeedback(self):
    #     self.root.destroy()
    #     obj = addfeedback.createAddFeedback()
    #     obj.firstFrame(self.empName)

    # def openViewFeedback(self):
    #     self.root.destroy()
    #     obj = viewfeedback.viewFeedback()
    #     obj.manageFeedback(self.empName)
        
    
if __name__=="__main__":
     obj=createEmphomemenu()
     obj.firstFrame()
