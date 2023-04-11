import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 9")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadphoenix():
    response = messagebox.askokcancel("Info", "This will open the Phoenix website. To download the jailbreak, you will need to scroll down and simply click the download button. There will be an IPA File in your downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://phoenixpwn.com/download.php")
choosejailbreak = tk.Label(frame, text="Choose an iOS 9 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

phoenixjailbreakbutton = tk.Button(frame, text="Phoenix", width="18", command=downloadphoenix)
phoenixjailbreakbutton.place(x=180, y=100)

root.mainloop()

