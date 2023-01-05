'''
simple graphical interface for data-strip and data-strip_pH
to make the setup and run of these tools less manual

using tkinter for gui setup

#41b6e6 is Pantone P298 - FYI

sam karpiniec

05jan2023 v0.1  set up basic, functional layout
                add data-strip and data-strip_pH methods, taking name/path info from entry fields
'''

import tkinter as tk
import tkinter.messagebox as messagebox
import glob
import math

def processCond():
    ff='Conductivity Data - ' + fileEntry.get() + '.csv'
    pp=pathEntry.get()
    messagebox.showinfo('Processing Conductivity Data', 'Filename: ' + ff)

    list=open(ff,'a+')
    list.write('filename,conductivity,\n')

    for datafilez in sorted(glob.iglob(pp+'/*.CSV')):
        csv=open(datafilez,'r')
        print(datafilez)
        lines=csv.readlines()
        csv.close()

        values=[]

        for x in range(3,len(lines)):
            if len(lines[x])!=1:
                values.append(float(lines[x][20:26]))

        avg=sum(values)/len(values)

        list.write(datafilez[-10:]+',')
        list.write(str(avg)+'\n')

    list.close()

def process_pH():
    ff='pH Data - ' + fileEntry.get() + '.csv'
    pp=pathEntry.get()
    
    messagebox.showinfo('Processing pH Data', 'Filename: '+ff)

    list=open(ff,'a+')
    list.write('filename,pH-avg,pH-conv-avg\n')

    for datafilez in sorted(glob.iglob(pp+'/*.CSV')):
        csv=open(datafilez,'r')
        print(datafilez)
        lines=csv.readlines()
        csv.close()

        values=[]
        Hvalues=[]

        for x in range(3,len(lines)):
           if len(lines[x])!=1: 
                z=float(lines[x][31:37])
                values.append(z)
                Hvalues.append(10**((-1)*z))

        avg=sum(values)/len(values)
        Havg=math.log((sum(Hvalues)/len(Hvalues)),10)*(-1)

        print(avg,Havg)

        list.write(datafilez[-10:]+',')
        list.write(str(avg)+',')
        list.write(str(Havg)+'\n')

    list.close()

mainWin=tk.Tk()
mainWin.title("Waste Data GUI v0.1")

frame=tk.Frame(master=mainWin, width=600, height=300, bg="#2288ff")
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title=tk.Label(
    master=frame,
    text="\n  Data Processor for pH and Conductivity Readings  \n",
    foreground="white",
    background="#2288ff",
    relief=tk.GROOVE
    )
title.place(x=10,y=10)
    
fileTitle=tk.Label(
    master=frame,
    text="Time period (e.g. Q4 2022):",
    foreground="white",
    background="#2288ff",
    )
fileTitle.place(x=10,y=70)

fileEntry = tk.Entry(
    master=frame,
    fg="black",
    bg="#cccccc",
    width=50
    )
fileEntry.insert(0,'Q4 2022')
fileEntry.place(x=10, y=95)

pathTitle=tk.Label(
    master=frame,
    text="Source directory containing raw data: (e.g. c:/tmp/test)",
    foreground="white",
    background="#2288ff",
    )
pathTitle.place(x=10, y=120)


pathEntry = tk.Entry(
    master=frame,
    fg="black",
    bg="#cccccc",
    width=50
    )
pathEntry.insert(0,'c:/tmp/test')
pathEntry.place(x=10,y=145)

processButton=tk.Button(
    text="Process pH and Conductivity Values",
    width=50,
    height=1,
    bg="#2288ff",
    fg="white",
    command=lambda:[processCond(),process_pH()]
    )
processButton.place(x=10, y=195)    

'''
condButton=tk.Button(
    text="Process Conductivity Values",
    width=50,
    height=1,
    bg="#2288ff",
    fg="white",
    command=processCond
    )
condButton.place(x=10, y=195)

pHButton=tk.Button(
    text="Process pH Values",
    width=50,
    height=1,
    bg="#2288ff",
    fg="white",
    command=processpH
    )
pHButton.place(x=10,y=230)
'''

mainWin.mainloop()
