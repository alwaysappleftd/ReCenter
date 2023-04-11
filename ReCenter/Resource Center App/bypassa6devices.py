import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Bypass A6 Devices")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadpalera1n():
    response = messagebox.askokcancel("Info", """This bypass is untethered for all A6 devices. 
First, download Sliver.

Once you have the app in your applications, open it and click the 'Ramdisk iCloud Bypass' option

Click the 'Bypass A6 Devices' button, then select your model of A6 Device. Next, follow the steps in the tool down one by one.

When the process is completed, your iPhone should reboot to the 'Press home to unlock' screen'.

""")

    if response == True:
        webbrowser.open("https://www.appletech752.com/Downloads/SliverV6.2.dmg")
choosebypass = tk.Label(frame, text="Choose a bypass for A6 Devices...", font=("helvetica", 20))
choosebypass.place(x=130, y=14)

sliverbypassbutton = tk.Button(frame, text="Sliver", width="18", command=downloadpalera1n)
sliverbypassbutton.place(x=180, y=100)

root.mainloop()

