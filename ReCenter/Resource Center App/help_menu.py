import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

root.title("About")

frame = tk.Frame(root, width="305", height="230")
frame.pack()

appicon = ImageTk.PhotoImage(Image.open("AppIcon2.png"))
appIconLabel = tk.Label(frame, image = appicon)
appIconLabel.place(x=110, y=30)
    
versionLabel = tk.Label(frame, text="Version 1.1", font=("helvetica", 14))
versionLabel.place(x=110, y=120)

copyrightLabel = tk.Label(frame, text="Copyright © 2023 Always Apple FTD. All rights reserved.", font=("helvetica", 12))
copyrightLabel.place(x=10, y=150)

root.mainloop()
