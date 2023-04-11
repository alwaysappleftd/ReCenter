import time
import tkinter as tk
import os
from PIL import ImageTk, Image
import webbrowser
from tkinter import messagebox
from tkinter.messagebox import showinfo
import plistlib
import glob

root = tk.Tk()

frame = tk.Frame(root, width="1200", height="700")
frame.pack()

root.title("ReCenter by @AlwaysAppleFTD")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

textwelcome = tk.Label(frame, text="Welcome to ReCenter!", font=("helvetica", 50))
textwelcome.place(x=350, y=15)

def downloadthreeutools():
    response = messagebox.askokcancel("WARNING", "This application is a Windows Application Only. Would You still like to download?",
                           icon='warning')

    if response == True:
        webbrowser.open("https://url.3u.com/zmAJjyaa")
    elif response == False:
        return

def downloadanytrans():
    webbrowser.open("https://www.imobie.com/go/download.php?product=atio&id=3")

def downloaddback():
    win = tk.Toplevel()
    win.title('Version')
    message = "This Application has 2 Versions."
    tk.Label(win, text="This Application has 2 Versions").pack()
    tk.Button(win, text='Mac', command=downloaddbackmac).pack()
    tk.Button(win, text='Windows',command=downloaddbackwindows).pack()

def downloaddbackmac():
    webbrowser.open("https://download.imyfone.com/imyfone-d-back-mac.zip")

def downloaddbackwindows():
    webbrowser.open("https://download.imyfone.com/imyfone-d-back_setup.exe")

def jailbreakios6():
    messagebox.showinfo("Info", "Coming Soon! Check back in a few weeks...")

def jailbreakios7():
    messagebox.showinfo("Info", "Coming Soon! Check back in a few weeks... ")

    
def jailbreakios8():
    os.system("python3 ios8jailbreaks.py")

def jailbreakios9():
    os.system("python3 ios9jailbreaks.py")

def jailbreakios10():
    os.system("python3 ios10jailbreaks.py")

def jailbreakios11():
    os.system("python3 ios11jailbreaks.py")

def jailbreakios12():
    os.system("python3 ios12jailbreaks.py")

def jailbreakios13():
    os.system("python3 ios13jailbreaks.py")

def jailbreakios14():
    os.system("python3 ios14jailbreaks.py")

def jailbreakios15():
    os.system("python3 ios15jailbreaks.py")

def jailbreakios16():
    os.system("python3 ios16jailbreaks.py")

def jailbreakios17():
    messagebox.showinfo("iOS 17 Not Released yet!", "Check back when Apple Releases iOS 17!")

def bypassiphone4():
    os.system("python3 bypassiphone4.py")

def bypassa5():
    os.system("python3 bypassa5devices.py")

def bypassa6():
    os.system("python3 bypassa6devices.py")

def bypassiphone5s():
    os.system("python3 bypassiphone5s.py")

def bypassiphone6():
    os.system("python3 bypassiphone6.py")


def bypassiphone6s():
    os.system("python3 bypassiphone6s.py")
    
def bypassiphone78x():
    os.system("python3 bypassiphone7-8-X.py")

def downgradea6():
    messagebox.showinfo("Not Available", "Coming Soon! Check back in a few weeks...")

def openhelpvideo():
    webbrowser.open("https://www.youtube.com/watch?v=uKJus8jQntg")

def youtubesubscribe():
    webbrowser.open("https://www.youtube.com/@alwaysappleftd?sub_confirmation=1")

def openhelpmenu():
    os.system("python3 help_menu.py")

def closeapplication(e):
    root.destroy()
    
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Close...", command=closeapplication, accelerator="Cmd+W")
menubar.add_cascade(label="File", menu=file_menu)

root.bind('<Command-w>', closeapplication)

options_menu = tk.Menu(menubar, tearoff=0)
jailbreaks_submenu = tk.Menu(options_menu, tearoff=0)
jailbreaks_submenu.add_command(label="Jailbreak iOS 6", command=jailbreakios6)
jailbreaks_submenu.add_command(label="Jailbreak iOS 7", command=jailbreakios7)
jailbreaks_submenu.add_command(label="Jailbreak iOS 8", command=jailbreakios8)
jailbreaks_submenu.add_command(label="Jailbreak iOS 9", command=jailbreakios9)
jailbreaks_submenu.add_command(label="Jailbreak iOS 10", command=jailbreakios10)
jailbreaks_submenu.add_command(label="Jailbreak iOS 11", command=jailbreakios11)
jailbreaks_submenu.add_command(label="Jailbreak iOS 12", command=jailbreakios12)
jailbreaks_submenu.add_command(label="Jailbreak iOS 13", command=jailbreakios13)
jailbreaks_submenu.add_command(label="Jailbreak iOS 14", command=jailbreakios14)
jailbreaks_submenu.add_command(label="Jailbreak iOS 15", command=jailbreakios15)
jailbreaks_submenu.add_command(label="Jailbreak iOS 16", command=jailbreakios16)
jailbreaks_submenu.add_command(label="Jailbreak iOS 17", command=jailbreakios17)
options_menu.add_cascade(label="Jailbreaks...", menu=jailbreaks_submenu)
root.bind('<Command-6>', jailbreakios6)
root.bind('<Command-7>', jailbreakios7)
root.bind('<Command-8>', jailbreakios8)
root.bind('<Command-9>', jailbreakios9)
root.bind('<Command-1><0>', jailbreakios10)
root.bind('<Command-1><l>', jailbreakios11)
root.bind('<Command-1><2>', jailbreakios12)
root.bind('<Command-1><3>', jailbreakios13)
root.bind('<Command-1><4>', jailbreakios14)
root.bind('<Command-1><5>', jailbreakios15)
root.bind('<Command-1><6>', jailbreakios16)
root.bind('<Command-1><7>', jailbreakios17)
bypasses_submenu = tk.Menu(options_menu, tearoff=0)
bypasses_submenu.add_command(label="Bypass iPhone 4", command=bypassiphone4)
bypasses_submenu.add_command(label="Bypass A5 Devices", command=bypassa5)
bypasses_submenu.add_command(label="Bypass A6 Devices", command=bypassa6)
bypasses_submenu.add_command(label="Bypass iPhone 5s", command=bypassiphone5s)
bypasses_submenu.add_command(label="Bypass iPhone 6", command=bypassiphone6)
bypasses_submenu.add_command(label="Bypass iPhone 6s", command=bypassiphone6s)
bypasses_submenu.add_command(label="Bypass iPhone 7/8/X", command=bypassiphone78x)
options_menu.add_cascade(label="Bypasses...", menu=bypasses_submenu)
menubar.add_cascade(label="Options", menu=options_menu)

extras_menu = tk.Menu(menubar, tearoff=0)
extras_menu.add_command(label="Downgrade A6 Devices...", command=downgradea6)
menubar.add_cascade(label="Extras...", menu=extras_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About ReCenter", command=openhelpmenu)
help_menu.add_command(label="ReCenter Video", command=openhelpvideo)
help_menu.add_command(label="Subscribe to Always Apple FTD on YouTube", command=youtubesubscribe)
menubar.add_cascade(label="Help", menu=help_menu)


root.config(menu=menubar)

getyoustrtd = tk.Label(frame, text="To get you started...", font=("helvetica", 20))
getyoustrtd.place(x=490, y=100)
img = ImageTk.PhotoImage(Image.open("3utools.png"))
threeutoolslabel = tk.Label(frame, image = img)
threeutoolslabel.place(x=105, y=170)
threeutoolstext = tk.Label(frame, text="3uTools", font=("helvetica", 25))
threeutoolstext.place(x=140, y=350)
img2 = ImageTk.PhotoImage(Image.open("images-3.jpeg"))
anytranslabel = tk.Label(frame, image = img2)
anytranslabel.place(x=490, y=170)
anytranstext = tk.Label(frame, text="AnyTrans", font=("helvetica", 25))
anytranstext.place(x=520, y=350)
img3 = ImageTk.PhotoImage(Image.open("images-2.jpeg"))
dbacklabel = tk.Label(frame, image = img3)
dbacklabel.place(x=910, y=170)
dbacktext = tk.Label(frame, text="D-Back", font=("helvetica", 25))
dbacktext.place(x=955, y=350)

downloadthreeutoolsbutton = tk.Button(frame, text="Download", command=downloadthreeutools)
downloadthreeutoolsbutton.place(x=140, y=390)
downloadanytransbutton = tk.Button(frame, text="Download", command=downloadanytrans)
downloadanytransbutton.place(x=530, y=390 )
downloaddbackbutton= tk.Button(frame, text="Download", command=downloaddback)
downloaddbackbutton.place(x=950, y=390)
jailbreakstext = tk.Label(frame, text="Jailbreaks", font=("helvetica", 25))
jailbreakstext.place(x=220, y=440)
ios6jailbreaksbutton = tk.Button(frame, text="iOS 6 Jailbreaks", command=jailbreakios6)
ios6jailbreaksbutton.place(x=50, y=490)
ios7jailbreaksbutton = tk.Button(frame, text="iOS 7 Jailbreaks", command=jailbreakios7)
ios7jailbreaksbutton.place(x=50, y=527)
ios8jailbreaksbutton = tk.Button(frame, text="iOS 8 Jailbreaks", command=jailbreakios8)
ios8jailbreaksbutton.place(x=50, y=564)
ios9jailbreaksbutton = tk.Button(frame, text="iOS 9 Jailbreaks", command=jailbreakios9)
ios9jailbreaksbutton.place(x=50, y=601)
ios10jailbreaksbutton = tk.Button(frame, text="iOS 10 Jailbreaks", command=jailbreakios10)
ios10jailbreaksbutton.place(x=210, y=490)
ios11jailbreaksbutton = tk.Button(frame, text="iOS 11 Jailbreaks", command=jailbreakios11)
ios11jailbreaksbutton.place(x=210, y=527)
ios12jailbreaksbutton = tk.Button(frame, text="iOS 12 Jailbreaks", command=jailbreakios12)
ios12jailbreaksbutton.place(x=210, y=564)
ios13jailbreaksbutton = tk.Button(frame, text="iOS 13 Jailbreaks", command=jailbreakios13)
ios13jailbreaksbutton.place(x=210, y=601)
ios14jailbreaksbutton = tk.Button(frame, text="iOS 14 Jailbreaks", command=jailbreakios14)
ios14jailbreaksbutton.place(x=370, y=490)
ios15jailbreaksbutton = tk.Button(frame, text="iOS 15 Jailbreaks", command=jailbreakios15)
ios15jailbreaksbutton.place(x=370, y=527)
ios16jailbreaksbutton = tk.Button(frame, text="iOS 16 Jailbreaks", command=jailbreakios16)
ios16jailbreaksbutton.place(x=370, y=564)
ios17jailbreaksbutton = tk.Button(frame, text="iOS 17 Not Out Yet!", command=jailbreakios17)
ios17jailbreaksbutton.place(x=370, y=601)

bypassestext = tk.Label(frame, text="Bypasses/Extras", font=("helvetica", 25))
bypassestext.place(x=800, y=440)
bypassiphone4button = tk.Button(frame, text="Bypass iPhone 4", command=bypassiphone4)
bypassiphone4button.place(x=680, y=490)
bypassa5devicesbutton = tk.Button(frame, text="Bypass A5 Devices", command=bypassa5)
bypassa5devicesbutton.place(x=680, y=527)
bypassa6devicesbutton = tk.Button(frame, text="Bypass A6 Devices", command=bypassa6)
bypassa6devicesbutton.place(x=680, y=564)
bypassiphone5sbutton = tk.Button(frame, text="Bypass iPhone 5s", command=bypassiphone5s)
bypassiphone5sbutton.place(x=680, y=601)
bypassiphone6button = tk.Button(frame, text="Bypass iPhone 6", command=bypassiphone6)
bypassiphone6button.place(x=840, y=490)
bypassiphone6sbutton = tk.Button(frame, text="Bypass iPhone 6s", command=bypassiphone6s)
bypassiphone6sbutton.place(x=840, y=527)
bypassiphone78xbutton = tk.Button(frame, text="Bypass iPhone 7/8/X", command=bypassiphone78x)
bypassiphone78xbutton.place(x=840, y=564)
downgradea6devicesbutton = tk.Button(frame, text="Downgrade All A6 Devices", command=downgradea6)
downgradea6devicesbutton.place(x=840, y=601)

root.mainloop()

