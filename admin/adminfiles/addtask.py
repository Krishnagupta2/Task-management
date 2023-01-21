from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import homemenu
import viewaddtask
import database


class createAddTask:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Task')

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

        self.my_label=Label(self.root,text="Add Task",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=30,width="200")


        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/taskimg.webp'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "500")

        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)
        self.projectLabel = Label(self.mainFrame, text="Project",font=("Mongolian Baiti",16))
        self.projectLabel.place(x = 15, y = 100, width="120")

        self.project = database.namePro()
        print(self.project)
        # self.project = ['a', 'b', 'c']
        self.projectName = StringVar()
        self.projectEntry = ttk.Combobox(self.mainFrame,value=self.project, textvariable=self.projectName)
        self.projectEntry.place(x = 150, y = 100, width="150",height=30)


        self.Taskname = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.Taskname.place(x = 30, y = 160, width="120")

        self.TasknameEntry = Entry(self.mainFrame)
        self.TasknameEntry.place(x = 150, y = 160, width="150",height=30)
       

        self.submit = Button(self.mainFrame, text = "Submit", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.submit.place(x = 80, y = 240, width="70")
        
        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=240,width="70",height=40)
        
        self.root.mainloop()

    def create(self):

        # print(tuple(self.projectName.get()))
        # print(self.projectName.get()[0])
        self.data = [
            self.projectEntry.get(),
            self.TasknameEntry.get()
        ]

        if self.projectEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Project.')
        elif self.TasknameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Tasks.')
        else:
            res = database.addtask(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.root.destroy()
                obj = viewaddtask.viewAddTask()
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