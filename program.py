import tkinter
import sqlconnfunctions
import groupfunctions
import webbrowser
import os

index=0

# create database connection
conn = sqlconnfunctions.create_connection()

# build queries
cur_entry = sqlconnfunctions.select_all_tasks(conn,index+1)
journal_txt = cur_entry[0][1].replace("\n","")
cols = sqlconnfunctions.get_all_columnnames(conn)

# root wondow
window = tkinter.Tk()

# set app to run at full screen
window.attributes("-fullscreen", True)
window.title("Undersøkelse LVI i allmennpraksis")

# configure grid GUI
window.grid()
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

window.rowconfigure(1,weight=8)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

window.rowconfigure(2,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

# Heading frame
frame1 = tkinter.Frame(window, bg="cornflower blue")
frame1.grid(row=0,column=0, columnspan=2, sticky="wens")

# Journal text frame
frame2 = tkinter.Frame(window, bg="black")
frame2.grid(row=1,column=0, sticky="wens")

# Structured text frame
frame3 = tkinter.Frame(window, bg="grey")
frame3.grid(row=1,column=1, sticky="wens")

# Subframe with buttons
frame4 = tkinter.Frame(window, bg="royalblue")
frame4.grid(row=2,column=0, sticky="wens")

frame5 = tkinter.Frame(window, bg="royalblue")
frame5.grid(row=2,column=1, sticky="wens")

header = tkinter.Label(frame1, font=(None, 44), text = "Undersøkelse LVI i allmennpraksis", bg=frame1["background"])
header.place(relx=.5,rely=.5,anchor="center")
#header.place(x=125,y=25,anchor="center")
#tkinter.Label(window, text = "Journaltekst <-----> Struktur", fg = "white", bg = "darkgrey").pack(fill = "x")

vartext1 = tkinter.StringVar()
vartext2 = tkinter.StringVar()
vartext3 = tkinter.StringVar()

# load in data
def callback_forward():
    global index,cur_entry,journal_txt
    index += 1
    cur_entry = sqlconnfunctions.select_all_tasks(conn,index)
    journal_txt = cur_entry[0][1].replace("\n","")
    vartext1.set(journal_txt)
    vartext2.set(groupfunctions.nicify_group2str(cur_entry,cols))
    vartext3.set(str(index) + "  >>>")

# call browser
def callback_toweb():
    stringbuilder = ""

    stringbuilder += str(cur_entry[0][6]) + ","  
    stringbuilder += str(cur_entry[0][7]) + ","
    stringbuilder += str(cur_entry[0][8]) + ","
    stringbuilder += str(cur_entry[0][9]) + ","
    stringbuilder += str(cur_entry[0][10]) + ","
    stringbuilder += str(cur_entry[0][11]) + ","
    stringbuilder += str(cur_entry[0][2]) + ","
    stringbuilder += str(cur_entry[0][3]) + ","
    stringbuilder += str(cur_entry[0][4]) + ","
    stringbuilder += str(cur_entry[0][5]) + ","

    counter = 12
    while (counter < 36):
        stringbuilder += str(cur_entry[0][counter]) + ","
        counter+=1

    my_file = open("strukturparams.txt","w", encoding="utf8")
    my_file.write(stringbuilder)
    my_file.close()

    webbrowser.open("file://" + os.path.realpath("struktur.html"))

callback_forward()

# label for journal text
d=tkinter.Label(frame2, 
font=("Courier", 16), 
anchor="nw",
bg="black",
fg="white",
height=frame2["height"],
width=frame2["width"],
justify="left",
wraplength=window.winfo_screenwidth()/2-100,
textvariable = vartext1)
d.grid(row=1,column=0, sticky="wens")
frame2.grid_propagate(0)

# label for structured text
tkinter.Label(frame3, 
font=("Courier", 16), 
anchor="nw",
justify="left",
wraplength=window.winfo_screenwidth()/2-100,
textvariable = vartext2,
fg = "white", 
bg = "grey").grid(row=1, column=1, sticky="wens")
frame3.grid_propagate(0)

# buttons
tkinter.Button(frame4, textvariable = vartext3, command=callback_forward).place(relx=.5,rely=.5,anchor="center")
tkinter.Button(frame5, text = "Vis struktur i browser...", command=callback_toweb).place(relx=.5,rely=.5,anchor="center")
tkinter.Button(frame5, text = "QUIT!", command=quit).pack(side="right")

# some handy keyboard shortcuts
def rightkey(event):
    callback_forward()
def leftkey(event):
    global index
    if index==1:
        return
    index-=2
    callback_forward()

window.focus_set()
window.bind('<Right>',rightkey)
window.bind('<Left>',leftkey)
window.bind('q', quit)

window.mainloop()