import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Jailbreak iOS 12")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def downloadunc0ver():
    response = messagebox.askokcancel("Info", "This will download an IPA File to your Downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")

    if response == True:
        webbrowser.open("https://unc0ver.dev/downloads/8.0.2/9e44edfbfd1905cadf23c3b9ad1d5bed683ce061/unc0ver_Release_8.0.2.ipa")

                                   
def downloadcheckra1n():
    response = messagebox.askokcancel("Info", "This is a macOS App. To jailbreak your idevice with Checkra1n, you will have to install the app on your Mac, then connect your iDevice to your computer and click the 'Start' button in the app. Then follow the instructions.")

def downloadchimera():
    win = tk.Toplevel()
    win.title('Options')
    message = "This IPA Supports iOS 12.5.6, but you will need a separate IPA."
    tk.Label(win, text="This IPA Supports iOS 12.5.6, but you will need a separate IPA.").pack()
    tk.Button(win, text='iOS 12 to 12.5.5', command=downloadchimeraoriginal).pack()
    tk.Button(win, text='iOS 12.5.6',command=downloadchimera1256).pack()

def downloadchimeraoriginal():
    response = messagebox.askokcancel("Info", "Download Chimera for iOS 12 to 12.5.5? There will be an IPA File in your Downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")
    
    if response == True:
        webbrowser.open("https://github.com/coolstar/electra-ipas/raw/master/chimera/1.6.4-12.2-12.5.ipa")

def downloadchimera1256():
    response = messagebox.askokcancel("Info", "Download Chimera for iOS 12.5.6? There will be an IPA File in your Downloads. To install it you must sideload the IPA to your iDevice. I would recomend AltServer at: https://altstore.io.")
    
    if response == True:
        webbrowser.open("https://file.jb-apps.me/ChimeraJB_12_5_6.ipa")


choosejailbreak = tk.Label(frame, text="Choose an iOS 12 Jailbreak...", font=("helvetica", 20))
choosejailbreak.place(x=150, y=14)

checkra1njailbreakbutton = tk.Button(frame, text="Checkra1n", width="18", command=downloadcheckra1n)
checkra1njailbreakbutton.place(x=180, y=135)

unc0verjailbreakbutton = tk.Button(frame, text="Unc0ver", width="18", command=downloadunc0ver)
unc0verjailbreakbutton.place(x=180, y=100)

chimerajailbreakbutton = tk.Button(frame, text="Chimera", width="18", command=downloadchimera)
chimerajailbreakbutton.place(x=180, y=170)



root.mainloop()

