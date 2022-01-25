import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width=200, height=100)
canvas1.pack()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot() # screenshot(region=(x축, y축, 가로길이, 세로길이))
    save_path = asksaveasfilename()
    myScreenshot.save(save_path+"_screenshot.png")

myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)
canvas1.create_window(100, 50, window=myButton)

root.mainloop()