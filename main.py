from tkinter import *
from pygame import mixer

root = Tk()

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