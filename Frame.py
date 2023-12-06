import time
from tkinter import *
from tkinter import ttk
from pywinauto import *
import win32gui
from PIL import ImageGrab


def Frame():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    hwnd = win32gui.FindWindow(None, "Waven")
    if (hwnd != 0):
        win32gui.MoveWindow(hwnd, -8, 0, 1366,900, True)
        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        win32gui.SetForegroundWindow(hwnd)
        found = True
    else :
        found = False


    root = Tk()
    resolution = str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())
    root.geometry("400x200")
    root.geometry("+1340+0")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Waventure").grid(column=0, row=0)
    start_button = ttk.Button(frm, text="Start", command=root.destroy,width=20).grid(column=0, row=1, padx=50, pady=20)
    Quit_button = ttk.Button(frm, text="Quit", command=root.destroy,width=20).grid(column=0, row=2, padx=50, pady=20)
    if(found):
        ttk.Label(frm, text="Game found everyting is working").grid(column=0, row=3)
    else:
        ttk.Label(frm, text="Game not found please lunch it and restart the program").grid(column=0, row=3)
    root.mainloop()

Frame()
