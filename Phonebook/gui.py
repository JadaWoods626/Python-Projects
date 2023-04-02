import tkinter
from tkinter import *

import main
import function

class load_gui(self):

#LABEL
        self.lbl_Fname = tk.Label(self.master,text='First Name: ', font=("Helvetica", 14), fg='black', bg='lightpink')
        self.lbl_Fname.grid(row=0, column=0,  padx=(27, 0), pady=(10, 0), sticky=N+W)
        
        self.lbl_Lname = tk.Label(self.master,text='Last Name: ', font=("Helvetica", 14), fg='black', bg='lightpink')
        self.lbl_Lname.grid(row=2, column=0, padx=(27, 0), pady=(10, 0)sticky=N+W)
        
        self.lbl_Phone = tk.Label(self.master,text='Phone', font=("Helvetica", 14), fg='black', bg='lightpink')
        self.lbl_Phone.grid(row=4, column=0, padx=(27, 0), pady=(10, 0)sticky=N+W)

        self.lbl_Email = tk.Label(self.master,text='Email', font=("Helvetica", 14), fg='black', bg='lightpink')
        self.lbl_Email.grid(row=6, column=0, padx=(27, 0), pady=(10, 0)sticky=N+W)

        self.lbl_User = tk.Entry(self.master,text=self.varLname, font=("Helvetica", 14), fg='black', bg='lightblue')
        self.lbl_User.grid(row=0, column=2, padx=(0, 0), pady=(10, 0)sticky=N+W)
        
#TEXT
        self.txt_Fname = tk.Entry(self.master,text=self.varFname, font=("Helvetica", 14), fg='black', bg='lightblue')
        self.txt_Fname.grid(row=1, column=0, padx=(30, 40), pady=(10, 0)sticky=N+E+W)
        
        self.txt_Lname = tk.Entry(self.master,text=self.varLname, font=("Helvetica", 14), fg='black', bg='lightblue')
        self.txt_Lname.grid(row=3, column=0, padx=(30, 40), pady=(10, 0)sticky=N+E+W)
        
        self.txt_Phone = tk.Entry(self.master,text=self.varFname, font=("Helvetica", 14), fg='black', bg='lightblue')
        self.txt_Phone.grid(row=5, column=0, padx=(30, 40), pady=(10, 0)sticky=N+E+W)
        
        self.txt_Email = tk.Entry(self.master,text=self.varLname, font=("Helvetica", 14), fg='black', bg='lightblue')
        self.txt_Email.grid(row=7, column=0, padx=(30, 40), pady=(10, 0)sticky=N+E+W)
        
#Define the listbox with a scrollbar and grid them
        self.scollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar.set)
        self.lstList1.bind('<<ListboxSelect>>',lambda event:phonebook-function.onSelect(self,event))
        self.scrollbar1.grid(row=1,column=2,rowspan=7,columspan=1,padx=(0,0),pady=(0,0),stitcky=N+E+S)
        self.lstList1.grid(row=1,column=2,rowspan=7,columspan=3,padx=(0,0),pady=(0,0),stitcky=N+E+S+W)
        
        
#BUTTON
        self.btn_add = tk.Button(self.master, text="Add", width=12, height=2, command=lambda: phonebook_function.addToList(self), bg='lightblue')
        self.btn_add.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
        
        self.btn_update = tk.Button(self.master, text="Update", width=12, height=2, command=lambda: phonebook_function.onUpdate(self), bg='lightblue')
        self.btn_update.grid(row=8, column=1, padx=(15, 0), pady=(45, 10), sticky=W)
        
        self.btn_delete = tk.Button(self.master, text="Delete", width=12, height=2, command=lambda: phonebook_function.onDelete(self), bg='lightblue')
        self.btn_delete.grid(row=8, column=2, padx=(15, 0), pady=(45, 10), sticky=W)
        
        self.btn_close = tk.Button(self.master, text="Close", width=12, height=2, command=lambda: phonebook_function.ask_quit(self), bg='lightblue')
        self.btn_close.grid(row=8, column=4, padx=(15, 0), pady=(15, 10), sticky=E)
        
function.create_db(self)
function.onRefresh(self)

if __name__ == "__main__":
  pass
