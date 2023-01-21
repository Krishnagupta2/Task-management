from tkinter import*
from tkinter.ttk import Treeview
from MySQLdb import DatabaseError
from PIL import Image,ImageTk

import homemenu
import viewaddemployee
import addtask
import viewaddtask
import viewassigntask
import viewfeedback
import assigntasks
import addproject
import viewaddproject
import database

class reportMenu:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Report')

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

        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/menuimg.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 250 , y = 0,  width="600", height = "500")   #x=250

        self.reportFrame = Canvas(self.root)
        self.reportFrame.place(x = 0, y = 0, width="250", height="500")

        sb = Scrollbar(
            self.reportFrame,
            orient=VERTICAL
        )
        sb.pack(fill=Y,side='right')

        # Make the buttons 
        self.home_b = Button(self.reportFrame,text="Projects",font=("Mongolian Baiti",24),relief='flat')
        self.home_b.place(x=50,y=10)

        data = database.allProjects()
        print(data)
        self.cordinateY=80
        for i in data:
            # print(i)
            self.set_b = Button(self.reportFrame,text=i[1],font=("Mongolian Baiti",16),relief='flat', command= lambda x = i: self.taskFrame(x))
            self.set_b.place(x=10,y=self.cordinateY)
            self.cordinateY+=50

        self.reportFrame.config(yscrollcommand=sb.set)
        sb.config(command=self.reportFrame.yview)

        self.backBtn=Button(self.reportFrame,text="Back",font=("Mongolian Baiti",20),bg="white", command= self.back)
        self.backBtn.place(x=150,y=450,width="70",height=40)

        self.root.mainloop()

    def taskFrame(self,tdata):

        self.AssignTaskFrame = Frame(self.root)
        self.AssignTaskFrame.place(x = 250, y = 300, width="650", height="200")

        self.TaskFrame = Frame(self.root)
        self.TaskFrame.place(x = 250, y = 0, width="650", height="300")


        for widget in self.AssignTaskFrame.winfo_children():
            widget.destroy()

        taskData = database.ReportTask(tdata[0])      

        
        self.ProjectName = Label(self.TaskFrame,text=f'Project - {tdata[1].title()}',font=("Mongolian Baiti",22))
        self.ProjectName.pack()

        self.tr = Treeview(self.TaskFrame, columns=('A', 'B', 'C'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#1', text="Task Name")
        self.tr.column('#1', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#2', text="Details")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)

        # print(tdata)
        for i in taskData:
            self.tr.insert('', 0, text = i[0], values=(i[2], 'View'))
        
        self.tr.pack() 

        self.tr.bind('<Double-Button-1>', self.actions)
 

    def assigntaskFrame(self,tdata):
        data = database.reportassignTask(tdata)
        print(data)

        self.frame2 = Frame(self.AssignTaskFrame, bg = "black")
        self.frame2.place(x = 0, y = 0, width="650", height="200")

        self.TaskName = Label(self.frame2,text=f'Task - {data[0][2].title()}',font=("Mongolian Baiti",22))
        self.TaskName.pack()

        self.tr1 = Treeview(self.frame2, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr1.heading('#0', text="Id")
        self.tr1.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr1.heading('#1', text="Emp Name")
        self.tr1.column('#1', minwidth=0, width=80, stretch=NO)

        self.tr1.heading('#2', text="Task Name")
        self.tr1.column('#2', minwidth=0, width=80, stretch=NO)

        self.tr1.heading('#3', text="Start Date")
        self.tr1.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr1.heading('#4', text="End Date")
        self.tr1.column('#4', minwidth=0, width=80, stretch=NO)

        self.tr1.heading('#5', text="Status")
        self.tr1.column('#5', minwidth=0, width=80, stretch=NO)

        
        for i in data:
            self.tr1.insert('', 0, text = i[0], values=(i[1], i[2],str(i[3]), str(i[4]), i[5]))

        self.tr1.pack()    

    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        
        print("e = ",e.x)
        # get the column id
        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        print(gup)

        if col =="#2":
            self.assigntaskFrame(gup[0])
        
    def openProjectTask(self,data):
        print(data)
        # print(f'task data {taskData}')
        # self.taskFrame(taskData)

    def back(self):
        self.root.destroy()
        obj = homemenu.createhome_menu()
        obj.firstFrame()
    
    
if __name__=="__main__":
     obj=reportMenu()
     obj.firstFrame()
