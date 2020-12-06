from tkinter import *
import os
import tkinter.font
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import colorchooser


def new():
    global file
    root.title("untitled-NotesTaker")
    file = None
    area.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        area.delete(1.0, END)
        f1 = open(file, "r")
        area.insert(1.0, f1.read())
        f1.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+" - NotesTaker")
    else:
        f = open(file, "w")
        f.write(area.get(1.0, END))
        f.close()


def saveas():
    global file
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                             filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    if file == None:
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+" - NotesTaker")
    else:
        f = open(file, "w")
        f.write(area.get(1.0, END))
        f.close()
        root.title(os.path.basename(file)+" - NotesTaker")

def end():
    root.quit()


def cut():
    area.event_generate("<<Cut>>")


def copy():
    area.event_generate("<<Copy>>")


def paste():
    area.event_generate("<<Paste>>")


def zoomin():
    global w
    m = w.actual("size")
    w.config(size=m+1)
    area.config(font=w)


def zoomout():
    global w
    m = w.actual("size")
    if m-1 == 0:
        w.config(size=1)
    else:
        w.config(size=m-1)
    area.config(font=w)


def aboutnote():
    messagebox.showinfo("NotesTaker", "This is an attempt at replicating Notepad, a popular platform to "
                                      "help write and maintain notes."
                                      "Try this application to ensure a colorful, "
                                      "enhanced and organised note-making process!")


def color1():
    o = colorchooser.askcolor(title="Choose font color")
    area.config(fg=o[1])


def change(ind):
    global w
    w.config(family=ind)
    area.config(font=w)


def change1(ind):
    global w
    w.config(weight=ind)
    area.config(font=w)


def change2(ind):
    global w
    w.config(slant=ind)
    area.config(font=w)


def change3(ind):
    global w
    w.config(underline=ind)
    area.config(font=w)


def change4(ind):
    global w
    w.config(size=ind)
    area.config(font=w)


root = Tk()
root.title("Untitled-Notepad")
root.wm_iconbitmap("note.ico")
root.geometry("644x788")
s = "black"
area = Text(root, font="Lucida", height=600, width=740, fg=s)
file = None
F = tkinter.font.families()
w = tkinter.font.Font()
G = ["bold", "normal"]
H = [True, False]
R = ["italic", "roman"]
L = range(2, 100, 2)
area.pack()
menu = Menu(root)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=saveas)
filemenu.add_command(label="Exit", command=end)
menu.add_cascade(label="File", menu=filemenu)
edit = Menu(menu, tearoff=0)
edit.add_command(label="Cut", command=cut)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
menu.add_cascade(label="Edit", menu=edit)
view = Menu(menu, tearoff=0)
view.add_command(label="Zoom in", command=zoomin)
view.add_command(label="Zoom out", command=zoomout)
menu.add_cascade(label="View", menu=view)
about = Menu(menu, tearoff=0)
about.add_command(label="About", command=aboutnote)
menu.add_cascade(label="About", menu=about)
font = Menu(menu, tearoff=0)
font.add_command(label="Choose color", command=color1)
format1 = Menu(font)
for y in F:
    format1.add_command(label=y, command=lambda u=y: change(u))
font.add_cascade(label="Font", menu=format1)
under1 = Menu(font)
for o in H:
    under1.add_command(label=o, command=lambda c=o: change3(c))
font.add_cascade(label="Underline", menu=under1)
size1 = Menu(font)
for l in L:
    size1.add_command(label=str(l), command=lambda k=l: change4(k))
font.add_cascade(label="Size", menu=size1)
weight1 = Menu(font)
for v in G:
    e = v[0].upper()+v[1:]
    weight1.add_command(label=e, command=lambda x=v: change1(x))
font.add_cascade(label="Weight", menu=weight1)
slant1 = Menu(font)
for q in R:
    d = q[0].upper()+q[1:]
    slant1.add_command(label=d, command=lambda z=q: change2(z))
font.add_cascade(label="Slant", menu=slant1)
menu.add_cascade(label="Format", menu=font)
root.config(menu=menu)
root.mainloop()
