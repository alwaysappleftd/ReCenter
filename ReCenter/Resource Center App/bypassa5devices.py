import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()

root.title("Bypass A5 Devices")

root.iconphoto(False, tk.PhotoImage(file='AppIcon.png'))

frame = tk.Frame(root, height="270", width="570")
frame.pack()

def arduinobypass():
    response = messagebox.askokcancel("Info", """The Arduino Exploit is the only way to bypass A5 Devices.
You will have to purchase a circuit board and then run the exploit through the board to the iDevice.
I would STRONGY reccomend watching a tutorial.
""")

    if response == True:
        webbrowser.open("https://www.youtube.com/watch?v=fYQtJ9ApDys")

def ipad2bypass():          
    response = messagebox.askokcancel("Info", """This will ONLY work with the iPad 2.

Would you still like to continue?""")

    if response == True:
        response2 = messagebox.askokcancel("Info", """This will open up a YouTube tutorial on how to do this bypass.

Please follow all the steps correctly.""")
    if response2 == True:
        webbrowser.open("https://www.youtube.com/watch?v=kL8nhoJ0ePc&t=432s")

choosebypass = tk.Label(frame, text="Choose a bypass for A5 Devices...", font=("helvetica", 20))
choosebypass.place(x=130, y=14)

arduinobypassbutton = tk.Button(frame, text="Arduino", width="18", command=arduinobypass)
arduinobypassbutton.place(x=180, y=100)

ipad2withoutarduinobutton = tk.Button(frame, text="Bypass iPad 2 without Arduino", width="22", command=ipad2bypass)
ipad2withoutarduinobutton.place(x=160, y=130)

root.mainloop()
