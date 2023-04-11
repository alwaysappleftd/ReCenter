import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Bypass iPhone 6")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadcheckm8andcheckra1n():
    response = messagebox.askokcancel("Info", """This bypass is a TETHERED bypass. That means that every time you reboot the device, let the battery die or the device turns off for any reason, you will have to rebypass the device. 
First, download the required tools.

When you select OK, you will get a prompt to download 2 tools. Just click on both of the links and allow downloads.

Once you have both apps in your applications, open the 'Checkra1n' app. Make sure your device is connected to the computer. Click the 'Start' button and follow the steps to complete the jailbreak.

If for some reason you failed to enter DFU Mode the first time, just keep trying. There's no harm in getting it wrong in fact I got it wrong SO many times when I was trying to learn ;)

Once that process has completed and your device has booted up, Open the 'Checkm8.info software' app in your applications. 

MAKE SURE that your device is on any screen BUT the iCloud Lock! The bypass will not complete if not so.

Then click the 'Start' button.

Now set up your device! It should skip right over the lock screen! 

""")

    if response == True:
        win = tk.Toplevel()
    win.title('Download Tools')
    message = "These are the tools for bypassing the iPhone 6..."
    tk.Label(win, text="These are the tools for bypassing the iPhone 6...").pack()
    tk.Button(win, text='Checkra1n', command=downloadcheckra1n).pack()
    tk.Button(win, text='Checkm8',command=downloadcheckm8).pack()


def downloadcheckra1n():
    webbrowser.open("https://assets.checkra.in/downloads/macos/754bb6ec4747b2e700f01307315da8c9c32c8b5816d0fe1e91d1bdfc298fe07b/checkra1n%20beta%200.12.4.dmg")


def downloadcheckm8():
    webbrowser.open("https://checkm8.info/download-free-software")

def downloadf3arra1n():
    messagebox.showinfo("Not Available", "Coming soon! Check back in a few weeks...")

choosebypass = tk.Label(frame, text="Choose a bypass for the iPhone 6...", font=("helvetica", 20))
choosebypass.place(x=130, y=14)

sliverbypassbutton = tk.Button(frame, text="Checkm8", width="18", command=downloadcheckm8andcheckra1n)
sliverbypassbutton.place(x=180, y=100)

f3arra1nbypassbutton = tk.Button(frame, text="F3arRa1n", width="18", command=downloadf3arra1n)
f3arra1nbypassbutton.place(x=180, y=135)


root.mainloop()

