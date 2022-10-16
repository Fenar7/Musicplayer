from pygame import *
from tkinter import *
from tkinter import ttk, filedialog
from pygame import mixer
import os

#Main screen 
master = Tk()
master.title("Spokify")
master.geometry("1000x600")
master.configure(bg="#0f1a2b")
master.resizable(False,False)

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

#ic
img_ic=PhotoImage(file="icon.png")
master.iconphoto(False,img_ic)

#background

bg=PhotoImage(file="background.png")
Label(master,image=bg).pack()

#cover image
img_cover=PhotoImage(file="cover.png")
Label(master,image=img_cover,bg="#2a3976").place(x=130,y=200)

#buttons
play_button=PhotoImage(file="play.png")
Button(master,image=play_button,bg="#313b7b",bd=0,command=play).place(x=175,y=440)

pause_button=PhotoImage(file="pause.png")
Button(master,image=pause_button,bg="#313b7b",bd=0,command=mixer.music.pause).place(x=115,y=440)

stop_button=PhotoImage(file="stop.png")
Button(master,image=stop_button,bg="#313b7b",bd=0,command=mixer.music.stop).place(x=295,y=440)

resume_button=PhotoImage(file="resume.png")
Button(master,image=resume_button,bg="#313b7b",bd=0,command=mixer.music.unpause).place(x=235,y=440)

#music
music_frame=Frame(master,bd=2,relief=RIDGE)
music_frame.place(x=612,y=165,width=296,height=375)

#music-info-show-section
music=Label(master,text="",font=("arial",15),fg="white",bg="#313b7b")
music.place(x=226,y=420,anchor="center")

#open----button----
#Button(master,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="green",command=open_folder).place(x=838,y=26)
open_button=PhotoImage(file="open_button.png")
Button(master,image=open_button,bg="#0F1011",bd=0,command=open_folder).place(x=838,y=26)
#music scrollbar frame
scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=296,height=375,font=("arial",10),bg="#1d346c",fg="white",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

master.mainloop()
