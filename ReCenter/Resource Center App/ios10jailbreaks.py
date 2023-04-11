import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 10")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadh3lix():
        win = tk.Toplevel()
        win.title("Version")
        message = "There are 2 versions of H3lix."
        tk.Label(win, text="There are 2 versions of H3lix. Choose your matching one...").pack()
        tk.Button(win, text='H3lix - iPhone 5', command=downloadh3lix32bit).pack()
        tk.Button(win, text='doubleH3lix - iPhone 5s to iPhone 7',command=downloadh3lix64bit).pack()

def downloadh3lix32bit():
    response = messagebox.askokcancel("Info", "This will open a website to download the file. Just click the green 'Download' button to download it. There will an IPA File in your downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://mega.nz/file/T0lTxASD#u8OJ2x9xNCSDkHhCPbX403zG_GOWgMQu3Sguv3rK2lQ")
        

def downloadh3lix64bit():
    response = messagebox.askokcancel("Info", "This will download the file to your computer. There will an IPA File in your downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://ios.vsharepe.com/jailbreak/doubleh3lix-rc8.ipa")
        

        
choosejailbreak = tk.Label(frame, text="Choose an iOS 10 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

phoenixjailbreakbutton = tk.Button(frame, text="H3lix", width="18", command=downloadh3lix)
phoenixjailbreakbutton.place(x=180, y=100)

root.mainloop()

