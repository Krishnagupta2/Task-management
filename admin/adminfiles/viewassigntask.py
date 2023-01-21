from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import homemenu
import database
import editassigntask

class viewAssignTask():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('View Assign Task')

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
        
    def manageTask(self):
        self.fr = Frame(self.root, bg="Grey")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#1', text="Emp Name")
        self.tr.column('#1', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#2', text="Task Name")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#3', text="Start Date")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="End Date")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#5', text="Status")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#6', text="Edit")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="Delete")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        data = database.allassignTask()
        print(data)
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2],str(i[3]), str(i[4]), i[5], 'Edit', 'Delete'))

        self.backBtn=Button(self.root,text="Back",font=("Mongolian Baiti",20),bg="white", command= self.back)
        self.backBtn.place(x=720,y=450,width="70",height=40)
        

            
      
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width=800)
        self.root.mainloop()
    
    def back(self):
        self.root.destroy()
        obj = homemenu.createhome_menu()
        obj.firstFrame()


    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        print(gup)
       
        if col == '#7':
            response = messagebox.askyesno('Delete','Do you really want to delete?')
            if response:
                a = database.deleteTask(gup)
                if a:
                    messagebox.showinfo('Success', 'task deleted successfully.')
                    self.root.destroy()
                    obj = viewAssignTask()
                    obj.manageTask()
                else:
                    messagebox.showinfo('Alert', 'Something went wrong.')

        if col =="#6":
            self.root.destroy()
            obj = editassigntask.createAssignTask()
            obj.firstFrame(gup)




if __name__ == '__main__':
    obj = viewAssignTask()
    obj.manageTask()
        
            