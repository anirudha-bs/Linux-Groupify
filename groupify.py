import os,shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def dialog():
   global group_path
   group_path=filedialog.askdirectory()
   global entryText
   entryText.set(group_path)


def arrange():
    
    global group_path 
    os.chdir(group_path)
    files=os.listdir(group_path)
 
    if len(files)==0:
        messagebox.showerror("Error","No files found in the specified directory")


    for file in files:
        if "." in file:
            folder=(file.split(".")[-1]).upper()
            try:
                os.makedirs(folder)
            except:
                pass
            finally:
                file_path=os.path.realpath(file)
                folder_path=os.path.realpath(folder)
                try:
                    shutil.move(file_path,folder_path)
                except:
                    pass

    messagebox.showinfo("Success","All the similar files are succesfully grouped together")
    global entryText
    entryText.set( "" )



myapp=Tk()

group_path=''

myapp.configure(background="#191919")
myapp.configure(highlightcolor="black")
myapp.title("Groupify")
myapp.geometry("600x450+634+328")

entryText = StringVar()
e1 = Entry(myapp,textvariable=entryText)
e1.place(relx=0.217, rely=0.293,height=26, relwidth=0.443)
e1.configure(background="white")
e1.configure(font="TkFixedFont")
group_path = e1.get()

l1 = Label(myapp)
l1.place(relx=0.233, rely=0.135, height=37, width=300)
l1.configure(background="#191919")
l1.configure(borderwidth="10")
l1.configure(foreground="#ffffff")
l1.configure(text='''Enter the path name or select from file menu''')
  
b1 = Button(myapp)
b1.place(relx=0.4, rely=0.541, height=27, width=111)
b1.configure(background="#d6d6d6")
b1.configure(text='''Groupify''',command=arrange)
  
l2 = Label(myapp)
l2.place(relx=0.367, rely=0.383, height=17, width=139)
l2.configure(background="#191919")
l2.configure(foreground="#ffffff")
l2.configure(text='''Actions cannot be undone''')

b2 = Button(myapp)
b2.place(relx=0.7, rely=0.293, height=27, width=31)
b2.configure(background="#303030",command=dialog)
photo_location = "/usr/share/pixmaps/folder_icon.png"
global _img0
_img0 = PhotoImage(file=photo_location)
b2.configure(image=_img0)


myapp.mainloop()



