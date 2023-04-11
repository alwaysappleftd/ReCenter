import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 15")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadpalera1n():
    response = messagebox.askokcancel("Info", """IMPORTANT! PYTHON3 MUST BE INSTALLED!!!

This will download the tool to your downloads. First, run the tool by opening up a new terminal window then typing 'cd', pressing the space bar and drag-and-dropping the PaleRa1n-GUI folder into the window. Then press enter. Type 'python3 palera1n.py' then press enter. The tool should open. Click the 'Semi-Tethered' button to jailbreak.""")

    if response == True:
        webbrowser.open("https://download2277.mediafire.com/dhjtx5hsxoqg/vd0hujexqg9462y/Palera1n+GUI-v1.2.4.zip")
choosejailbreak = tk.Label(frame, text="Choose an iOS 15 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

palera1njailbreakbutton = tk.Button(frame, text="PaleRa1n", width="18", command=downloadpalera1n)
palera1njailbreakbutton.place(x=180, y=100)

root.mainloop()

