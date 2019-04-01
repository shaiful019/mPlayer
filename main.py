from tkinter import *
import tkinter.messagebox
import webbrowser
from pygame import mixer

root = Tk()

#Create the menubar

menubar = Menu(root)
root.config(menu = menubar)

#Create the submenu

subMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "Open")
subMenu.add_command(label = "Exit", command = root.destroy)

def aboutUs():
    tkinter.messagebox.showinfo("Mplayer", 'This is a music player build using python Tkinter By,\nShaiful Islam')
    webbrowser.open('http://www.shaifulislam.com')

subMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = subMenu)
subMenu.add_command(label = "About Us", command = aboutUs)


mixer.init()    #Initializing the mixer


root.title("mPlayer")
root.geometry("600x480")

text = Label(root, text = 'Let\'s make some noise')
text.pack()

def playMusic():
    mixer.music.load("song1.mp3")
    mixer.music.play()
    print("Hey! This play button works pretty well.")

playPhoto = PhotoImage(file = 'play.png')
playBtn = Button(root, image = playPhoto, command = playMusic)
playBtn.pack()

def stopMusic():
    mixer.music.stop()

stopPhoto = PhotoImage(file = 'stop.png')
stopBtn = Button(root, image = stopPhoto, command = stopMusic)
stopBtn.pack()

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

scale = Scale(root, from_=0, to = 100, orient = HORIZONTAL, command = set_vol)
scale.set(50)
scale.pack()

root.mainloop()