import time
from tkinter import *
from tkinter import ttk
import pywinauto
import win32gui,win32com.client
from PIL import ImageGrab
from Arti_Ficelle import *
from Read_Data import *

def Frame():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    hwnd = win32gui.FindWindow(None, "Waven")
    if (hwnd != 0):
        found = True 
        win32gui.MoveWindow(hwnd, -8, 0, 1366,900, True)
        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        win32gui.SetForegroundWindow(hwnd)
    else :
        found = False


    root = Tk()
    resolution = str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())
    root.geometry("400x200")
    root.geometry("+1340+0")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Waventure").grid(column=0, row=0)
    start_button = ttk.Button(frm, text="Start", command=start_waventure,width=20).grid(column=0, row=1, padx=50, pady=20)
    Quit_button = ttk.Button(frm, text="Quit", command=root.destroy,width=20).grid(column=0, row=2, padx=50, pady=20)
    if(found):
        ttk.Label(frm, text="Game found everyting is working").grid(column=0, row=3)
    else:
        ttk.Label(frm, text="Game not found please lunch it and restart the program").grid(column=0, row=3)
    root.mainloop()

def apply_instructions(instructions):

            for i in range (len(instructions)):
                if (len(instructions[i])!=0):
                    if(instructions[i][0]==1):
                        pywinauto.mouse.click(button="left",coords=mouse_coordinates[str(instructions[i][1][0])+"."+str(instructions[i][1][1])])
                        pywinauto.mouse.press(button="left",coords=mouse_coordinates[str(instructions[i][1][0])+"."+str(instructions[i][1][1])])
                        time.sleep(5)
                        pywinauto.mouse.move(coords=mouse_coordinates[str(instructions[i][2][0])+"."+str(instructions[i][2][1])])
                        pywinauto.mouse.release(button="left",coords=mouse_coordinates[str(instructions[i][2][0])+"."+str(instructions[i][2][1])])
                    elif(instructions[i][0]==2):
                        pywinauto.mouse.click(button="left",coords=mouse_coordinates[str(instructions[i][1][0])+"."+str(instructions[i][1][1])])
                        pywinauto.mouse.press(button="left",coords=mouse_coordinates[str(instructions[i][1][0])+"."+str(instructions[i][1][1])])
                        time.sleep(5)
                        pywinauto.mouse.move(coords=mouse_coordinates[str(instructions[i][2][0])+"."+str(instructions[i][2][1])])
                        pywinauto.mouse.move(coords=mouse_coordinates[str(instructions[i][3][0])+"."+str(instructions[i][3][1])])
                        pywinauto.mouse.release(button="left",coords=mouse_coordinates[str(instructions[i][3][0])+"."+str(instructions[i][3][1])])
                    elif(instructions[i][0]==3):
                        pywinauto.mouse.press(button="left",coords=mouse_coordinates["spells"+"."+str(instructions[i][1])])
                        pywinauto.mouse.move(coords=mouse_coordinates[str(instructions[i][2][0])+"."+str(instructions[i][2][1])])
                        pywinauto.mouse.release(button="left",coords=mouse_coordinates[str(instructions[i][2][0])+"."+str(instructions[i][2][1])])
            pywinauto.mouse.click(button="left",coords=mouse_coordinates["end_turn"])
            time.sleep(1)

def start_waventure():
    hwnd = win32gui.FindWindow(None, "Waven")
    pywinauto.mouse.click(button="left", coords=(700,825))
    if (hwnd == 0):
        root = Tk()
        root.geometry("275x100")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Game not found ").grid(column=0, row=0)
        Quit_button = ttk.Button(frm, text="Quit", command=root.destroy,width=20).grid(column=0, row=2, padx=50, pady=20)
        root.mainloop()
    else:
        pywinauto.mouse.click(button="left", coords=(700,825))
        time.sleep(12)
        combat_launched = True
        while(combat_launched):
            #(33, 182, 255)
            image = ImageGrab.grab(bbox = (844,800,1000,900))
            if(not notsamepixel(image.getpixel((100,50)),[(0, 0, 0)])):               
                char_list = [1]
                spellist = []
                our_instructions = []
                reco_board(char_list,spellist)
                current_board = board("0",char_list,[[]],spellist,spells)
                print(char_list)
                launch_simulation([[current_board]],our_instructions,1)
                print(our_instructions)
                apply_instructions(our_instructions)
            image = ImageGrab.grab(bbox=(0,0,1343,882))
            #if(not notsamepixel(image.getpixel((560,160)),[(0, 255, 248)])):
            combat_launched = False
            time.sleep(10)
            pywinauto.mouse.click(button="left", coords=(700,775))
            time.sleep(7)
            pywinauto.mouse.move(coords=(762,470))
            pywinauto.mouse.press(button="left", coords=(762,470))
            time.sleep(0.2)
            pywinauto.mouse.release(button="left", coords=(762,470))
            time.sleep(0.2)
            pywinauto.mouse.click(button="left", coords=(790,410))
                

Frame()
