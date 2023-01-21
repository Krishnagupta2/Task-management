from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

from PIL import Image, ImageTk
import viewassigntask
import homemenu
import database

class createAssignTask:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Edit Assign Task')

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
        self.Id = gup[0] 
        # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.mainFrame,text="Edit Assign Task",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
    
        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('images/editemp.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="800", height = "500")

        self.EmpIdLabel = Label(self.mainFrame, text="Emp Id",font=("Mongolian Baiti",16),bg="white")
        self.EmpIdLabel.place(x = 36, y = 100, width="100")

        self.emp = database.nameEmp()
        self.empName = StringVar()
        self.EmpIdEntry = ttk.Combobox(self.mainFrame,value=self.emp, textvariable=self.empName)
        self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)


        self.TaskNameLabel = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16),bg="white")
        self.TaskNameLabel.place(x = 30, y = 160, width="100")

        self.Task = database.nameTask()
        self.TaskName = StringVar()
        self.TaskNameEntry = ttk.Combobox(self.mainFrame,value=self.Task, textvariable=self.TaskName)
        self.TaskNameEntry.place(x = 150, y = 160, width="150",height=30)

        self.StartDateLabel = Label(self.mainFrame, text="Start Date",font=("Mongolian Baiti",16),bg="white")
        self.StartDateLabel.place(x = 28, y = 220, width="100")

        self.joinData = StringVar()
        self.StartDateEntry = DateEntry(self.mainFrame, textVariable = self.joinData,date_pattern='yyyy-MM-dd')
        self.StartDateEntry.place(x = 150, y = 220, width="150",height=30)
        # self.DateEntry.configure(validate='none')
        self.StartDateEntry.delete(0,'end')

        self.EndDateLabel = Label(self.mainFrame, text="End Date",font=("Mongolian Baiti",16),bg="white")
        self.EndDateLabel.place(x = 28, y = 280, width="100")

        self.endData = StringVar()
        self.EndDateEntry = DateEntry(self.mainFrame, textVariable = self.endData,date_pattern='yyyy-MM-dd')
        self.EndDateEntry.place(x = 150, y = 280, width="150",height=30)
        self.EndDateEntry.delete(0,'end')

        self.Status = Label(self.mainFrame, text="Status",font=("Mongolian Baiti",16),bg="white")
        self.Status.place(x = 28, y = 340, width="100")

        self.StatusEntry = Entry(self.mainFrame)
        self.StatusEntry.place(x = 150, y = 340, width="150",height=30)

        self.update= Button(self.mainFrame, text = "Update",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.update.place(x = 50, y = 400)

        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=400,width="70",height=40)

        print(f'edit files {database.get_employee(gup)}')
        self.joinData.set("")

        a = database.get_assigntask(gup)
        print("data = ", a)
        self.EmpIdEntry.insert(0,(a[0], a[1]))
        self.TaskNameEntry.insert(0,(a[6],a[2]))
        self.StartDateEntry.insert(0,a[3])
        self.EndDateEntry.insert(0,a[4])
        self.StatusEntry.insert(0,a[5])
       
        self.root.mainloop()

    def create(self):
        # print(self.EmpIdEntry.get())
        self.data = (
            self.EmpIdEntry.get()[0], 
            self.TaskNameEntry.get()[0], 
            self.StartDateEntry.get(),
            self.EndDateEntry.get(),
            self.StatusEntry.get(),
            self.Id
        )
        print(f'updated data - {self.data}')
        if (self.EmpIdEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your EmpId.')
        elif(self.EmpIdEntry.get().isalpha()):
            messagebox.showinfo('alert','enter valid EmpId')
        elif self.TaskNameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your TaskName.')
        elif self.StartDateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Start Date.')
        elif self.EndDateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your End Date.')
        elif self.StatusEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter Status.')
        else:
            print("editing",self.data)
            res = database.update_assigntask(self.data)
            if res:
                messagebox.showinfo('Alert','Updated Successfully')
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
    obj = createAssignTask()
    obj.firstFrame('gup')