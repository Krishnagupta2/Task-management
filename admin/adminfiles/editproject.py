from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

from PIL import Image, ImageTk
import viewaddproject
import homemenu
import database

class createEditProject:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Edit Project')

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

        self.my_label=Label(self.mainFrame,text="EDIT PROJECT",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
    
        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('images/editemp.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="800", height = "500")


        self.NameLabel = Label(self.mainFrame, text="Project Name",font=("Mongolian Baiti",16),bg="white")
        self.NameLabel.place(x = 30, y = 100, width="120")

        self.NameEntry = Entry(self.mainFrame)
        self.NameEntry.place(x = 150, y = 100, width="150",height=30)

        self.DetailsLabel = Label(self.mainFrame, text="Details",font=("Mongolian Baiti",16),bg="white")
        self.DetailsLabel.place(x = 30, y = 160, width="100")

        self.DetailsEntry = Entry(self.mainFrame)
        self.DetailsEntry.place(x = 150, y = 160, width="150",height=30)

        self.DateLabel = Label(self.mainFrame, text="Date",font=("Mongolian Baiti",16),bg="white")
        self.DateLabel.place(x = 28, y = 220, width="100")

        self.joinData = StringVar()
        self.DateEntry = DateEntry(self.mainFrame, textVariable = self.joinData,date_pattern='yyyy-MM-dd')
        self.DateEntry.place(x = 150, y = 220, width="150",height=30)
        
        self.DateEntry.delete(0,'end')
        # self.DateEntry.configure(validate='none')

    
        self.update= Button(self.mainFrame, text = "Update",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.update.place(x = 50, y = 300)

        self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        self.backBtn.place(x=230,y=300,width="70",height=40)

        # print(f'edit files {database.get_employee(gup)}')
        # self.joinData.set("")

        a = database.get_project(gup)
        self.NameEntry.insert(0,a[1])
        self.DetailsEntry.insert(0,a[3])
        self.DateEntry.insert(0,a[2])
       
        self.root.mainloop()

    def create(self):
        self.data = (
            self.NameEntry.get(),
            self.DateEntry.get(),
            self.DetailsEntry.get(),
            self.Id
        )
        if self.NameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Name.')
        elif self.DateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your joining date.')
        elif self.DetailsEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Details.')
        else:
            print("editing",self.data)
            res = database.update_project(self.data)
            if res:
                messagebox.showinfo('Alert','Updated Successfully')
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
    obj = createEditProject()
    obj.firstFrame('gup')