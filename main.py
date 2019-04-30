from tkinter import *
import os
import tkinter.messagebox
from tkinter import filedialog
import webbrowser
from pygame import mixer
from mutagen.mp3 import MP3

root = Tk()

# Create the menubar

menubar = Menu(root)
root.config(menu=menubar)



def openFile():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

# Create the submenu

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
fileLabel = Label(root, text='Let\'s make some noise')
fileLabel.pack(pady = 10, padx = 10)

lengthLabel = Label(root, text='Total Length is --:--')
lengthLabel.pack(pady = 10, padx = 10)


def showDetails():
    fileLabel['text'] = "Playing " + os.path.basename(filename)
    fileExtention = os.path.splitext(filename)

    if(fileExtention[1] == '.mp3'):
        a = MP3(filename)
        total_length = a.info.length

    else:
        a = mixer.Sound(filename)
        total_length = a.get_length()




    #div - total_length / 60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeFormat = '{:02d}:{:02d}'.format(mins, secs)
    lengthLabel['text'] = 'Total Length is ' + timeFormat



def playMusic():
    global paused
    if(paused):
        mixer.music.unpause()
        statusbar['text'] = "Playing " + os.path.basename(filename)
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing "+ os.path.basename(filename)
            showDetails()

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

def rewindMusic():
    playMusic()
    statusbar['text'] = "Music rewinded"

def set_vol(val):
    global volume
    volume = int(val) / 100
    mixer.music.set_volume(volume)

muted = FALSE
def muteMusic():
    global muted
    if muted:
        mixer.music.set_volume(50)
        scale.set(50)
        unmuteBtn.configure(image=unmutePhoto)
        muted = FALSE
    else:
        muted = TRUE
        mixer.music.set_volume(0)
        scale.set(0)
        unmuteBtn.configure(image=mutePhoto)



middleFrame = Frame(root)
middleFrame.pack(pady = 30, padx = 30)

#Adding play button

playPhoto = PhotoImage(file='images/play.png')
playBtn = Button(middleFrame, image=playPhoto, command=playMusic)
playBtn.grid(row = 0, column = 0, padx = 10)

#Adding stop button

stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = Button(middleFrame, image=stopPhoto, command=stopMusic)
stopBtn.grid(row = 0, column = 1, padx = 10)

#Add pause button

pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = Button(middleFrame, image=pausePhoto, command=pauseMusic)
pauseBtn.grid(row = 0, column = 2, padx = 10)

#Add bottom frame

bottomFrame = Frame(root)
bottomFrame.pack(pady = 10)

#Add rewind button

rewindPhoto = PhotoImage(file='images/rewind.png')
rewindBtn = Button(bottomFrame, image=rewindPhoto, command=rewindMusic)
rewindBtn.grid(row = 0, column = 0)

#Adding Mute button

unmutePhoto = PhotoImage(file='images/unmute.png')
mutePhoto = PhotoImage(file='images/mute.png')
unmuteBtn = Button(bottomFrame, image=unmutePhoto, command=muteMusic)
unmuteBtn.grid(row = 0, column = 1)

#Adding volume level

scale = Scale(bottomFrame, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
scale.grid(row = 0, column = 2)

# Adding satusbar
statusbar = Label(root, text="***Welcome to the world of music***", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
