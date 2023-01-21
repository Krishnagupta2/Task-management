from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk

import emphomemenu
import Database
# import viewfeedback

class createAddFeedback:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Feedback')

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
        

    def firstFrame(self, data):
        self.data = data
        # create a frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.root,text="FEEDBACK!",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=70,width="200")

        self.backBtn=Button(self.root,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=210,y=300,width="70",height=40)
        

        # set background image
        self.image = ImageTk.PhotoImage(Image.open('image/feedbackimg1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 300, y =  0,  width="800", height = "500")

        self.TaskNameLabel = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.TaskNameLabel.place(x = 18, y = 150, width="120")

        self.task = Database.allEmpTaskName(self.data)
        self.taskname = StringVar()
        self.TaskNameEntry = ttk.Combobox(self.mainFrame,value=self.task, textvariable=self.taskname)
        self.TaskNameEntry.place(x = 130, y = 150, width="150",height=30)

        self.EmpId = Label(self.mainFrame, text="EmpId",font=("Mongolian Baiti",16))
        self.EmpId.place(x = 3, y = 200, width="120")

        self.emp = Database.allEmpName(self.data)
        self.empName = StringVar()
        self.EmpIdEntry = ttk.Combobox(self.mainFrame,value=self.emp, textvariable=self.empName)
        self.EmpIdEntry.place(x = 130, y = 200, width="150",height=30)      

        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 130, y = 200, width="150",height=30)

        self.FeedbackLabel = Label(self.mainFrame, text="Feedback",font=("Mongolian Baiti",16))
        self.FeedbackLabel.place(x = 15, y = 250, width="120")

        self.FeedbackEntry = Entry(self.mainFrame)
        self.FeedbackEntry.place(x = 130, y = 250, width="150",height=30)

        self.submit = Button(self.mainFrame, text = "Submit", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.submit.place(x = 130, y = 300, width="70")

        a = Database.allEmpTaskName(self.data)
        self.TaskNameEntry.insert(0,a[0])
        b = Database.allEmpName(self.data)
        self.EmpIdEntry.insert(0,b[0])

        self.EmpIdEntry.config(state='disabled')

        self.root.mainloop()

    def create(self):
        self.datas = [
            self.TaskNameEntry.get(), 
            self.data[0],
            self.FeedbackEntry.get(),
           
        ]
        if (self.TaskNameEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your task.')
        elif self.FeedbackEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Task Name.')
        
        else:
            res = Database.addFeedbacks(self.datas)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.root.destroy()
                obj = emphomemenu.createEmphomemenu()
                obj.firstFrame((self.data, ), '')
            else:
                messagebox.showinfo('Alert', 'Something went wrong')
        
           
    def back(self):
        self.root.destroy()
        obj = emphomemenu.createEmphomemenu()
        obj.firstFrame((self.data, ), 'logged')





if __name__ == '__main__':
    obj = createAddFeedback()
    obj.firstFrame()