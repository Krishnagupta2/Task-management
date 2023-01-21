
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import viewaddemployee
import homemenu
import database

class createAddEmployee:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Employee')

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
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.mainFrame,text="EMPLOYEE DETAIL!",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=400,width="70",height=40)

        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('images/empimg1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "500")

        self.EmpIdLabel = Label(self.mainFrame, text="Emp Id",font=("Mongolian Baiti",16),bg="white")
        self.EmpIdLabel.place(x = 36, y = 100, width="100")

        self.EmpIdEntry = Entry(self.mainFrame)
        self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)


        self.NameLabel = Label(self.mainFrame, text="Name",font=("Mongolian Baiti",16),bg="white")
        self.NameLabel.place(x = 30, y = 140, width="100")

        self.NameEntry = Entry(self.mainFrame)
        self.NameEntry.place(x = 150, y = 140, width="150",height=30)

        self.EmailLabel = Label(self.mainFrame, text="Email",font=("Mongolian Baiti",16),bg="white")
        self.EmailLabel.place(x = 30, y = 180, width="100")

        self.EmailEntry = Entry(self.mainFrame)
        self.EmailEntry.place(x = 150, y = 180, width="150",height=30)

        self.PasswordLabel = Label(self.mainFrame, text="Password",font=("Mongolian Baiti",16),bg="white")
        self.PasswordLabel.place(x = 42, y = 220, width="100")

        self.PasswordEntry = Entry(self.mainFrame,show='*')
        self.PasswordEntry.place(x = 150, y = 220, width="150",height=30)

        self.ContactLabel = Label(self.mainFrame, text="Contact",font=("Mongolian Baiti",16),bg="white")
        self.ContactLabel.place(x = 36, y = 260, width="100")

        self.ContactEntry = Entry(self.mainFrame)
        self.ContactEntry.place(x = 150, y = 260 , width="150",height=30)

        self.AddressLabel = Label(self.mainFrame, text="Address",font=("Mongolian Baiti",16),bg="white")
        self.AddressLabel.place(x = 36, y = 300, width="100")

        self.AddressEntry = Entry(self.mainFrame)
        self.AddressEntry.place(x = 150, y = 300, width="150",height=30)

        self.JoiningdateLabel = Label(self.mainFrame, text="DOJ",font=("Mongolian Baiti",16),bg="white")
        self.JoiningdateLabel.place(x = 28, y = 340, width="100")

        self.joinData = StringVar()
        self.JoiningdateEntry = DateEntry(self.mainFrame, textVariable = self.joinData,date_pattern='yyyy-MM-dd')
        self.JoiningdateEntry.place(x = 150, y = 340, width="150",height=30)

        self.submit = Button(self.mainFrame, text = "Submit",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.submit.place(x = 50, y = 400)

        self.root.mainloop()

    def create(self):
        self.data = [
            self.EmpIdEntry.get(), 
            self.NameEntry.get(), 
            self.EmailEntry.get(),
            self.PasswordEntry.get(), 
            self.ContactEntry.get(), 
            self.AddressEntry.get(),
            self.JoiningdateEntry.get()
        ]
        if (self.EmpIdEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your EmpId.')
        elif(self.EmpIdEntry.get().isalpha()):
            messagebox.showinfo('alert','enter valid EmpId')
        elif self.NameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Name.')
        elif self.EmailEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Email.')
        elif self.PasswordEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Password.')
        elif self.ContactEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Contact.')
        elif(self.ContactEntry.get().isalpha()):
            messagebox.showinfo('alert','enter valid Contact')
        elif self.AddressEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Address.')
        elif self.JoiningdateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your joining date.')
        else:
            res = database.addEmp(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.root.destroy()
                obj = viewaddemployee.viewAddEmployee()
                obj.manageEmployee()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')


    def back(self):
        self.root.destroy()
        obj = homemenu.createhome_menu()
        obj.firstFrame()





if __name__ == '__main__':
    obj = createAddEmployee()
    obj.firstFrame()