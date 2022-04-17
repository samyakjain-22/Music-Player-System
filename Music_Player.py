def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()

def unmutemusic():
    global currentvol
    root.unMuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.unMuteButton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)

def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused')

def playmusic():
    ad=musictrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing...')

def musicurl():
    dd=filedialog.askopenfilename()
    print(dd)
    musictrack.set(dd)

def createwidthes():
    global mplay,mpause,mstop,mv1,mv2,mbrowse,mresume,mmute,munmute
    global AudioStatusLabel

    ############################################################################################################################ Images register

    mplay=PhotoImage(file='youtube.png')
    mpause=PhotoImage(file='pause (1).png')
    mstop=PhotoImage(file='stop.png')
    mv1=PhotoImage(file='increase-volume.png')
    mv2=PhotoImage(file='reduce-volume.png')
    mbrowse=PhotoImage(file='search.png')
    mresume=PhotoImage(file='youtube.png')
    mmute=PhotoImage(file='mute.png')
    munmute=PhotoImage(file='increase-volume.png')


    ################################################################################################################################# Image size

    mplay=mplay.subsample(10,10)
    mpause=mpause.subsample(10,10)
    mstop=mstop.subsample(10,10)
    mbrowse=mbrowse.subsample(10,10)
    mv1=mv1.subsample(10,10)
    mv2=mv2.subsample(10,10)
    mresume=mresume.subsample(10,10)
    mmute=mmute.subsample(10,10)
    munmute=munmute.subsample(10,10)

    ######################################################################################################################################labels

    Tracklabel=Label(root,text="Select Audio Track:",bg='dimgrey',font=('ariel',16,'italic bold'))
    Tracklabel.grid(column=0,row=0,padx=20,pady=20)
    AudioStatusLabel=Label(root,text=" ",bg='beige',font=('ariel',16,'italic bold'),width=20)
    AudioStatusLabel.grid(row=3,column=0)

    ######################################################################################################################################## Entry box

    TracklabelEntry=Entry(root,font=('ariel',16,'bold'),width=35,textvariable=musictrack)
    TracklabelEntry.grid(row=0,column=1,padx=20,pady=20)

    ######################################################################################################################################### BUttons

    BrowseButton=Button(root,text='SEARCH',bg='dimgrey',font=('ariel',13,'bold')
                        ,width=200,bd=4,activebackground='whitesmoke',
                        image=mbrowse, compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root, text='PLAY', bg='dimgrey', font=('ariel', 13, 'bold'),
                        width=200, bd=4,activebackground='whitesmoke',
                        image=mplay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1, column=1, padx=20, pady=20)

    root.PauseButton = Button(root, text='PAUSE', bg='dimgrey', font=('ariel', 13, 'bold'),
                              width=200, bd=4,activebackground='whitesmoke',
                              image=mpause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=2, column=1, padx=20, pady=20)

    root.ResumeButton  = Button(root, text='RESUME', bg='dimgrey', font=('ariel', 13, 'bold'),
                                width=200, bd=4,activebackground='whitesmoke',
                                image=mpause, compound=RIGHT, command=resumemusic)
    root.ResumeButton.grid(row=2, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    root.MuteButton=Button(root,text='MUTE',width=200,bg='dimgrey',bd=5,image=mmute,
                           compound=RIGHT,command=mutemusic)
    root.MuteButton.grid(row=4,column=2,padx=20,pady=20)

    root.unMuteButton=Button(root,text='UNMUTE',width=200,bg='dimgrey',bd=5,
                             image=munmute,compound=RIGHT,command=unmutemusic)
    root.unMuteButton.grid(row=4,column=2,padx=20,pady=20)
    root.unMuteButton.grid_remove()


    StopButton = Button(root, text='STOP', bg='dimgrey', font=('ariel', 13, 'bold'),
                        width=200, bd=4,activebackground='whitesmoke',
                        image=mstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=3, column=1, padx=20, pady=20)

    Volume1Button = Button(root, text='VOLUME UP', bg='dimgrey', font=('ariel', 13, 'bold'),
                           width=200, bd=4,activebackground='whitesmoke',
                           image=mv1,compound=RIGHT,command=volumeup)
    Volume1Button.grid(row=2, column=0, padx=20, pady=20)

    Volume2Button = Button(root, text='VOLUME DOWN', bg='dimgrey', font=('ariel', 13, 'bold'),
                           width=200, bd=4,activebackground='whitesmoke',
                           image=mv2,compound=RIGHT,command=volumedown)
    Volume2Button.grid(row=2, column=2, padx=20, pady=20)
###############################################################################################################################

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import tkinter as tk
root=Tk()
root.geometry('1100x600+400+150')
root.title("My Music Player")
root.iconbitmap('music.ico')
root.configure(bg='darkgrey')

######################################################################################################################################### global variables

musictrack=StringVar()
currentvol=0

######################################################################################################################################### SLIDER

ss="DEVELOPED BY SAMYAK"
count=0
text=''
SliderLabel=Label(root,text=ss,bg='darkgrey', font=('ariel', 30, 'italic bold'))
SliderLabel.grid(row=5,column=0,padx=20,pady=20,columnspan=3)
def IntroLabel():
    global count,text
    if (count>=len(ss)):
        count=-1
        text=''

        SliderLabel.configure(text=text)
    else:
        text=text+ss[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200,IntroLabel)
IntroLabel()
mixer.init( )

root.resizable(False,False)
createwidthes()
root.mainloop()