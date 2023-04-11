import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 8")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadetason():
    response = messagebox.askokcancel("Info", "This will download an IPA File to your computer. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://onejailbreak.com/site/templates/IPA/etasonJB-RC5.ipa")
choosejailbreak = tk.Label(frame, text="Choose an iOS 8 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

phoenixjailbreakbutton = tk.Button(frame, text="Etason JB", width="18", command=downloadetason)
phoenixjailbreakbutton.place(x=180, y=100)

root.mainloop()
