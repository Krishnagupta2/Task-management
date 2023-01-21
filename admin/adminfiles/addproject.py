
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import viewaddemployee
import viewaddproject
import homemenu
import database

class createAddProject:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Project')

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

        self.my_label=Label(self.mainFrame,text="Project Details",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=250,width="70",height=40)

        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('images/empimg1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "500")


        self.NameLabel = Label(self.mainFrame, text="Name",font=("Mongolian Baiti",16),bg="white")
        self.NameLabel.place(x = 30, y = 100, width="100")

        self.NameEntry = Entry(self.mainFrame)
        self.NameEntry.place(x = 150, y = 100, width="150",height=30)

        self.DetailsLabel = Label(self.mainFrame, text="Details",font=("Mongolian Baiti",16),bg="white")
        self.DetailsLabel.place(x = 36, y = 160, width="100")

        self.DetailsEntry = Entry(self.mainFrame)
        self.DetailsEntry.place(x = 150, y = 160, width="150",height=30)

        # self.dateLabel = Label(self.mainFrame, text="Date",font=("Mongolian Baiti",16),bg="white")
        # self.dateLabel.place(x = 28, y = 220, width="100")

        # self.joinData = StringVar()
        # self.dateEntry = DateEntry(self.mainFrame, textVariable = self.joinData)
        # self.dateEntry.place(x = 150, y = 220, width="150",height=30)
    
        self.submit = Button(self.mainFrame, text = "Submit",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.submit.place(x = 50, y = 250)

        self.root.mainloop()

    def create(self):
        self.data = [
            # self.ProIDEntry.get(), 
            self.NameEntry.get(),  
            # self.dateEntry.get(),
            self.DetailsEntry.get()
        ]
        # if (self.ProIDEntry.get() == ''):
        #     messagebox.showinfo('Alert', 'Enter your ProID.')
        # elif(self.ProIDEntry.get().isalpha()):
        #     messagebox.showinfo('alert','enter valid EmpId')
        if self.NameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Name.')
        elif self.DetailsEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Details.')
        # elif self.dateEntry.get() == '':
        #     messagebox.showinfo('Alert', 'Enter your  date.')
        else:
            res = database.addPro(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.root.destroy()
                obj = viewaddproject.viewAddProject()
                obj.manageTask()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')

    def back(self):
        self.root.destroy()
        obj = homemenu.createhome_menu()
        obj.firstFrame()



if __name__ == '__main__':
    obj = createAddProject()
    obj.firstFrame()