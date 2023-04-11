import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 11")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadunc0ver():
    response = messagebox.askokcancel("Info", "This will download an IPA File to your Downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://unc0ver.dev/downloads/8.0.2/9e44edfbfd1905cadf23c3b9ad1d5bed683ce061/unc0ver_Release_8.0.2.ipa")

                                   
def downloadelectra():
    response = messagebox.askokcancel("Info", "This jailbreak is LIMITED. It only supports iOS 11.0 to 11.1.2. There will an IPA File in your downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://electrajb.com/downloads/Electra%201.0.4.ipa")
        
choosejailbreak = tk.Label(frame, text="Choose an iOS 11 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

electrajailbreakbutton = tk.Button(frame, text="Electra", width="18", command=downloadelectra)
electrajailbreakbutton.place(x=180, y=135)

unc0verjailbreakbutton = tk.Button(frame, text="Unc0ver", width="18", command=downloadunc0ver)
unc0verjailbreakbutton.place(x=180, y=100)



root.mainloop()

