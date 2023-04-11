import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 13")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadunc0ver():
    response = messagebox.askokcancel("Info", "This will download an IPA File to your Downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://unc0ver.dev/downloads/8.0.2/9e44edfbfd1905cadf23c3b9ad1d5bed683ce061/unc0ver_Release_8.0.2.ipa")

                                   
def downloadcheckra1n():
    response = messagebox.askokcancel("Info", "This is a macOS App. To jailbreak your idevice with Checkra1n, you will have to install the app on your Mac, then connect your iDevice to your computer and click the 'Start' button in the app. Then follow the instructions.")

    if response == True:
        webbrowser.open("https://assets.checkra.in/downloads/macos/754bb6ec4747b2e700f01307315da8c9c32c8b5816d0fe1e91d1bdfc298fe07b/checkra1n%20beta%200.12.4.dmg")

choosejailbreak = tk.Label(frame, text="Choose an iOS 13 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

checkra1njailbreakbutton = tk.Button(frame, text="Checkra1n", width="18", command=downloadcheckra1n)
checkra1njailbreakbutton.place(x=180, y=135)

unc0verjailbreakbutton = tk.Button(frame, text="Unc0ver", width="18", command=downloadunc0ver)
unc0verjailbreakbutton.place(x=180, y=100)


root.mainloop()

