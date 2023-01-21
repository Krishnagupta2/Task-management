from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import homemenu
import viewaddtask
import database


class createEditTask:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Edit Task')

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
        

    def firstFrame(self,gup):
        self.data = gup[0]
        # create a frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.root,text="Edit Task",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=30,width="200")


        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/edittask.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 320, y =  0,  width="600", height = "500")

        self.ProjectName = Label(self.mainFrame, text="Project Name",font=("Mongolian Baiti",16))
        self.ProjectName.place(x = 30, y = 100, width="120")

        self.project = database.namePro()
        self.projectName = StringVar()
        self.ProjectNameEntry = ttk.Combobox(self.mainFrame, value=self.project, textvariable=self.projectName)
        self.ProjectNameEntry.place(x = 150, y = 100, width="150",height=30)       
        
        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)

        self.Taskname = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.Taskname.place(x = 25, y = 180, width="120")

        self.TasknameEntry = Entry(self.mainFrame)
        self.TasknameEntry.place(x = 150, y = 180, width="150",height=30)

        # self.Status = Label(self.mainFrame, text="Status",font=("Mongolian Baiti",16))
        # # self.Status.place(x = 10, y = 260, width="120")

        # self.task = ['completed','pending']
        # self.StatusEntry = ttk.Combobox(self.mainFrame,value=self.task)
        # # self.StatusEntry.place(x = 150, y = 260, width="150",height=30)


        self.update = Button(self.mainFrame, text = "Update", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.update.place(x = 50, y = 250, width="70")
        
        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=250,width="70",height=40)
        
        print(f'edit files {database.get_task(gup)}')
        a = database.get_task(gup)
        print(f'data - {a}')
        self.ProjectNameEntry.insert(0,(a[0],a[1]))
        self.TasknameEntry.insert(0,a[2])

        # self.ProjectNameEntry.config(state='disabled')
        # self.TasknameEntry.config(state='disabled')
        self.root.mainloop()

    def create(self):
        self.value = (
            self.ProjectNameEntry.get()[0],
            self.TasknameEntry.get(), 
            self.data
        )
        print("data = ",self.value)
        if self.ProjectNameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Project.')
        elif self.TasknameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Task.')
        else:
            res = database.update_task(self.value)
            if res:
                messagebox.showinfo('Alert','Updated Successfully')
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
    obj = createEditTask()
    obj.firstFrame('gup')