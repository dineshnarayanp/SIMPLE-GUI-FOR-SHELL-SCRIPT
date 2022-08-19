import shlex
import sys
import os
import subprocess
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import itertools
from colorama import Fore
from cmd import Cmd
from tkinter import filedialog

root = tk.Tk()
root.title('GUI for shell interpreter')
root.geometry('1980x1080')
# root.iconbitmap("D:\os_project\icon.png")
root.configure(bg='light grey')

bg= ImageTk.PhotoImage(Image.open(requests.get("https://www.pixel4k.com/wp-content/uplo"
                            "ads/2018/11/anime-cityscape-landscape-scenery-4k_1541975011.jpg", stream=True).raw))
label1 = Label(root, image=bg)
label1.place(x=0, y=0,relwidth=1,relheight=1)

def run_block():
    value = usd_text.get(1.0, "end-1c")
    p1 = subprocess.Popen(value, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = p1.communicate()
    if value == 'exit':
        sys.exit()
    if p1.returncode == 0:
        output.insert(END, '\nout: {0}'.format(out))
        output.insert(END, 'command : success')
    else:
        output.insert(END, '\ncommand : failed','warning')
        output.insert(END, ("\nError occured with execution: {0}".format(err)), 'warning')

def math_calc():
    value = usd_text.get(1.0, "end-1c")
    if value == 'exit':
        sys.exit()
    try:
        out = eval(value)
        if out: output.insert(END,out)
    except:
        try:
            exec(value)
        except Exception as e:
            output.insert(END, "\n")
            output.insert(END,("Error occured with execution: {0}".format(e)),'warning')

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Template files", "*.tplate"),("HTML files", ".html;.htm"),
                                                     ("Text files",".txt"),("all files""."),("python files",".py")))

    usd_text.insert(END,"python "+filename)

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


def listdir():
    value = usd_text.get(1.0, "end-1c")
    out=os.listdir(value)
    for i in out:
        output.insert(END,i)
        output.insert(END,"\n")

label_file_explorer = Label(root,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
#1st horizontal
#1_1
button_explore = Button(root,height=3, width=25,
                        text = "Browse Files",
                        command = browseFiles)
button_explore.grid(padx=40, pady=80,row=0 ,column=0)
#1_2
usd_text = Text(root, height=1, width=52,fg="green")
usd_text.insert(END, '>>Enter the shell cmd here..')
usd_text.grid(padx=0, pady=15, row=0 ,column=1)
#1_3
convert_button = Button(root, height=2,
                    width=20,
                    text="Run", command=run_block)
convert_button.grid(padx=5, pady=15, row=0 ,column=2)



#2nd horizontal
#2_1
math_button = Button(root, height=2,
                    width=20,
                    text="calculate", command=math_calc)
math_button.grid(padx=1, pady=15, row=1,column=1)
#2_2
list_button = Button(root, height=2,
                    width=20,
                    text="list directory", command=listdir)
list_button.grid(padx=1, pady=15,row=1 ,column=2)

#3rd horizontal
#3_1
img = ImageTk.PhotoImage(Image.open(requests.get("https://th.bing.com/th/id/OIP.OoIUFAX0X3M_JbY_Fj64OQAAAA?pid=ImgDet&rs=1",
                                                 stream=True).raw))

panel = Label(root, image=img)
panel.grid(padx=5, pady=15, row=2 ,column=0)
#3_2
output = Text(root, height=30,
              width=120,
              bg="light blue", fg="blue")
output.tag_config('warning', foreground="red")
output.grid(padx=5, pady=15, row=2 ,column=1)
#3_3
img2 = ImageTk.PhotoImage(Image.open(requests.get("https://th.bing.com/th/id/OIP.OoIUFAX0X3M_JbY_Fj64OQAAAA?pid=ImgDet&rs=1",

                                                  stream=True).raw))

panel1 = Label(root, image=img2)
panel1.grid(padx=30, pady=15, row=2 ,column=2)
root.mainloop()


