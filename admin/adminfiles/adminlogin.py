from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import homemenu
import database


class createLogin:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('LOG IN')

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

        # set background image
        self.image = ImageTk.PhotoImage(Image.open('images/login.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.config(bg="white")
        self.bgLabel.place(x = 330, y = 0,  width="490", height = "500")

        self.my_label=Label(self.root,text="LOGIN HERE!",font=("Mongolian Baiti",30),bg="white")
        self.my_label.place(x=10,y=40,width="300",height="50")

        self.UsernameLabel = Label(self.mainFrame, text="Username*",font=("Mongolian Baiti",16),bg="white")
        self.UsernameLabel.place(x = 30, y = 130, width="160",height="30")

        self.UsernameEntry = Entry(self.mainFrame)
        self.UsernameEntry.place(x = 45, y = 170, width="160",height="30")


        self.PasswordLabel = Label(self.mainFrame, text="Password*",font=("Mongolian Baiti",16),bg="white")
        self.PasswordLabel.place(x = 30, y = 240, width="160",height="30")

        self.PasswordEntry = Entry(self.mainFrame,show='*')
        self.PasswordEntry.place(x = 45, y =280, width="160",height="30")

        self.login = Button(self.mainFrame, text = "LOGIN", command=self.create,font=("Mongolian Baiti",16),bg="white",fg="black")
        self.login.place(x = 85, y = 360, width="80",height="30")


        self.root.mainloop()

    def create(self):
        data = (
            self.UsernameEntry.get(),
            self.PasswordEntry.get()
        )
        if(self.UsernameEntry.get()==""):
            messagebox.showinfo("alert","please enter your username and password")
        elif(self.PasswordEntry.get()==""):
            messagebox.showinfo("alert","please enter your password")
        else:
            print(data)
            res = database.adminLogin(data)
            if res:
                messagebox.showinfo('Success', 'login successfully.')
                self.root.destroy()
                obj = homemenu.createhome_menu()
                obj.firstFrame()
            else:
                messagebox.showinfo('Alert', 'Invalid username and/or password.')
        


        
if __name__=="__main__":
     obj=createLogin()
     obj.firstFrame()