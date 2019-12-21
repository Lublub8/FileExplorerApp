# File Explorer App

from tkinter import *
from tkinter.ttk import *
root=Tk()

s=Style()
s.theme_use('clam')

s.configure('.', font=('verdana', 14),background='pink')
s.configure('TLabel',foreground='black',background='yellow')
s.configure('TFrame',foreground='orange',background='lightblue')
s.map('TButton',background=[('pressed','lightgreen'),('active','white')],foreground=[('pressed','red'),('active','orange')])
######################################################

root.configure(background='pink')
root.geometry("510x600")
root.title("File Explorer App")
root.resizable(False,False)

def search1():
    search_term1 = cmbvar1.get().lower()
    import os
    basedir = r'C:\Users\Redwan Ahmad'

    files = []

    for r, d, f in os.walk(basedir):
        for file in f:
            if file.find(search_term1) >= 0:
                files.append(os.path.join(r, file))

    print(f'{search_term1}:')
    print('*'*15)
    print(f'{len(files)} files Found! in the directory {basedir}')
    for f in files:
        print(f)
    print('*'*50)

def search2():
    search_term2 = cmbvar2.get().lower()
    import os
    basedir = r'C:\Users\Redwan Ahmad'

    files = []

    for r, d, f in os.walk(basedir):
        for file in f:
            if file.find(search_term2) >= 0:
                files.append(os.path.join(r, file))

    print(f'{search_term2}:')
    print('*' * 15)
    print(f'{len(files)} files Found! in the directory {basedir}')
    for f in files:
        print(f)
    print('*' * 50)

def search3():
    search_term3 = cmbvar3.get().lower()
    import os
    basedir = r'C:\Users\Redwan Ahmad'

    files = []

    for r, d, f in os.walk(basedir):
        for file in f:
            if file.find(search_term3) >= 0:
                files.append(os.path.join(r, file))

    print(f'{search_term3}:')
    print('*' * 15)
    print(f'{len(files)} files Found! in the directory {basedir}')
    for f in files:
        print(f)
    print('*' * 50)

def search4():
    search_term4 = cmbvar4.get().lower()
    import os
    basedir = r'C:\Users\Redwan Ahmad'

    files = []

    for r, d, f in os.walk(basedir):
        for file in f:
            if file.find(search_term4) >= 0:
                files.append(os.path.join(r, file))

    print(f'{search_term4}:')
    print('*' * 15)
    print(f'{len(files)} files Found! in the directory {basedir}')
    for f in files:
        print(f)
    print('*' * 50)

Label(root,text="File Explorer App",background='yellow').pack()

#Document
Tab1=Notebook(root,width=500)
Tab1.pack()

NewFrame = Frame(Tab1)
Tab1.add(NewFrame,text="Document")

#Pictures
Tab2=Notebook(root,width=500)
Tab2.pack()

NewFrame2 = Frame(Tab2)
Tab2.add(NewFrame2,text="Pictures")

#Music
Tab3=Notebook(root,width=500)
Tab3.pack()

NewFrame3 = Frame(Tab3)
Tab3.add(NewFrame3,text="Music")

#Video
Tab4=Notebook(root,width=500)
Tab4.pack()

NewFrame4 = Frame(Tab4)
Tab4.add(NewFrame4,text="Video")


file_ex = 'File Extensions'

Label1 = Label(NewFrame, text=file_ex, style='TLabel')
Label1.grid(row=0, column=0, sticky=NSEW)

Opt_doc = ['.DOCX','.TXT','.PDF','.ODT','.RTF','.HTML','.PPTX']
Opt_pic = ['.JPG','.PNG','.GIF','.TIFF','.PSD','.EPS','.AI','.INDD','.RAW']
Opt_mus = ['.WAV','.MP3','.WMA','.AAC','.FLAC','.MID','.MIDI']
Opt_vid = ['.MPEG','.MP4','.3GP','.OGG','.WMV','.WEBM','.HDV']

#Document
cmbvar1=StringVar(NewFrame)
cmbvar1.set(Opt_doc[0])
Combo1=Combobox(NewFrame,height=10,width=25,values=Opt_doc,textvariable=cmbvar1) #Height refers to number of values it will list without scroll
Combo1.grid(row=6,column=1,columnspan=2,sticky=NSEW)

#Button
Button(NewFrame,text="Search",command =search1).grid(row=6,column=3,sticky=NSEW)


#Pictures
cmbvar2=StringVar(NewFrame2)
cmbvar2.set(Opt_pic[0])
Combo2=Combobox(NewFrame2,height=10,width=25,values=Opt_pic,textvariable=cmbvar2) #Height refers to number of values it will list without scroll
Combo2.grid(row=6,column=1,columnspan=2,sticky=NSEW)

Label1 = Label(NewFrame2, text=file_ex, style='TLabel')
Label1.grid(row=0, column=0, sticky=NSEW)

#Button
Button(NewFrame2,text="Search",command =search2).grid(row=6,column=3,sticky=NSEW)

#Music
cmbvar3=StringVar(NewFrame3)
cmbvar3.set(Opt_mus[0])
Combo3=Combobox(NewFrame3,height=10,width=25,values=Opt_mus,textvariable=cmbvar3) #Height refers to number of values it will list without scroll
Combo3.grid(row=6,column=1,columnspan=2,sticky=NSEW)

Label1 = Label(NewFrame3, text=file_ex, style='TLabel')
Label1.grid(row=0, column=0, sticky=NSEW)

#Button
Button(NewFrame3,text="Search",command =search3).grid(row=6,column=3,sticky=NSEW)

#Video
cmbvar4=StringVar(NewFrame4)
cmbvar4.set(Opt_vid[0])
Combo4=Combobox(NewFrame4,height=10,width=25,values=Opt_vid,textvariable=cmbvar4) #Height refers to number of values it will list without scroll
Combo4.grid(row=6,column=1,columnspan=2,sticky=NSEW)

Label1 = Label(NewFrame4, text=file_ex, style='TLabel')
Label1.grid(row=0, column=0, sticky=NSEW)

#Button
Button(NewFrame4,text="Search",command =search4).grid(row=6,column=3,sticky=NSEW)

root.mainloop()

