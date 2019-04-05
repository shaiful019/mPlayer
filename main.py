from tkinter import *
import os
import tkinter.messagebox
from tkinter import filedialog
import webbrowser
from pygame import mixer

root = Tk()

# Create the menubar

menubar = Menu(root)
root.config(menu=menubar)


# Create the submenu

def openFile():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=openFile)
subMenu.add_command(label="Exit", command=root.destroy)


def aboutUs():
    tkinter.messagebox.showinfo("Mplayer", 'This is a music player build using python Tkinter By,\nShaiful Islam')
    webbrowser.open('http://www.shaifulislam.com')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=aboutUs)

mixer.init()  # Initializing the mixer

root.title("mPlayer")
root.geometry('400x400+200+190')

text = Label(root, text='Let\'s make some noise')
text.pack()


def playMusic():
    global paused
    if(paused):
        mixer.music.unpause()
        statusbar['text'] = "Playing " + os.path.basename('song1.mp3')
    else:
        try:
            mixer.music.load('song1.mp3')
            mixer.music.play()
            statusbar['text'] = "Playing "+ os.path.basename('song1.mp3')

        except:
            tkinter.messagebox.showerror('File not found', "Please load a music file first.")


def stopMusic():
    global paused
    mixer.music.stop()
    paused = FALSE
    statusbar['text'] = "Music stopped"

paused = FALSE
def pauseMusic():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

#Adding play button

playPhoto = PhotoImage(file='images/play.png')
playBtn = Button(root, image=playPhoto, command=playMusic)
playBtn.pack()

#Adding stop button

stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = Button(root, image=stopPhoto, command=stopMusic)
stopBtn.pack()

#Add pause button

pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pauseMusic)
pauseBtn.pack()

#Adding volume level

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
scale.pack()

# Adding satusbar
statusbar = Label(root, text="***Welcome to the world of music***", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
