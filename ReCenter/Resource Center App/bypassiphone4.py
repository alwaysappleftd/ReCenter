import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Bypass iPhone 4")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadpalera1n():
    response = messagebox.askokcancel("Info", """Sliver is an untethered bypass for the iPhone 4. First, download Sliver.

Once you have the app in your applications, open it and click the 'Ramdisk iCloud Bypass' option

Click the 'Bypass A4 Devices' button, then select your model of iPhone 4. Next, follow the steps in the tool down one by one.

When the process is completed, your iPhone should reboot to the 'Slide to unlock' screen.

""")

    if response == True:
        webbrowser.open("https://phoenixpwn.com/download.php")
choosebypass = tk.Label(frame, text="Choose a bypass for the iPhone 4...", font=("helvetica", 20))
choosebypass.place(x=130, y=14)

sliverbypassjailbreakbutton = tk.Button(frame, text="Sliver", width="18", command=downloadpalera1n)
sliverbypassjailbreakbutton.place(x=180, y=100)

root.mainloop()

