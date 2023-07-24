from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import webbrowser
import datetime
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import glenn01_support



def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def drive_rangee():
    import drive_range


root = tk.Tk()

root.overrideredirect(True)
width = (600)
height = (1024)
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))
image_file = resource_path("achilles_raspi.gif")
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()



def vp_start_gui():
    
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    glenn01_support.init(root, top)
    root.mainloop()

w = None



def create_Toplevel1(root, *args, **kwargs):

    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    glenn01_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
g = 0
class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        fname =file=resource_path("main_cyclo_withlogo.gif")
        bg_image = tk.PhotoImage(file=fname)
        self.Canvas1 = tk.Canvas(top)
        startframe = tk.Frame(root)
        tk.Canvas(startframe, width=1280, height=800)
        startframe.pack()
        self.Canvas1.pack()
        root.bg_image = bg_image
        self.Canvas1.create_image((0, 0), image=bg_image, anchor='nw')
        w = bg_image.width()
        h = bg_image.height()
        top.geometry('%dx%d+0+10' % (w,h))
        top.overrideredirect(True)
        top.title("New Toplevel")
        top.configure(background="#000000")
        self.Canvas1.place(relx=-0.004, rely=-0.006, relheight=1.016, relwidth=1.003)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=1203)
        self.Canvas1.create_text(290, 320, fill="#42f5d7", text="MPH", font=("Arial", 12))
        self.Canvas1.create_text(750, 320, fill="#42f5d7", text="RPM", font=("Arial", 12))



        

        #Battery
        def Battery(Battery_: int = 0):
            Battery_ = int(Battery_)
            self.Canvas1.delete("tag2")
            self.Canvas1.create_text (570, 345, text=Battery_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag2")

       
        self.Scale2 = tk.Scale(top,command=drive_rangee, from_=0.0, to=99.0)
        self.Scale2.place(relx=0.420, rely=0.831, relwidth=0.08, relheight=0.0
                , height=41, bordermode='ignore')
        self.Scale2.configure(activebackground="#39ede1")
        self.Scale2.configure(background="#000000")
        self.Scale2.configure(borderwidth="0")
        self.Scale2.configure(font="TkTextFont")
        self.Scale2.configure(foreground="#ffffff")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="black")
        self.Scale2.configure(highlightthickness="0")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(troughcolor="#200fbc")
        self.Scale2.configure(width=8)
        Battery_:object = self.Scale2.get()
        
        #Battery remained LABEL
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.320, rely=0.838, height=31, width=110)
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''BATTERY REMAINED''')

        #rpm
        def rpm(rpm_: int = 0):
            rpm_ = int(rpm_)
            self.Canvas1.delete("tag3")
            self.Canvas1.create_text (710, 260, text=rpm_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag3")
        self.Scale3 = tk.Scale(top,command=rpm, from_=0.0, to=720.0)
        self.Scale3.place(relx=0.650, rely=0.780, relwidth=0.078, relheight=0.0
                , height=37, bordermode='ignore')
        self.Scale3.configure(activebackground="#39ede1")
        self.Scale3.configure(background="#000000")
        self.Scale3.configure(borderwidth="0")
        self.Scale3.configure(font="TkTextFont")
        self.Scale3.configure(foreground="#ffffff")
        self.Scale3.configure(highlightbackground="#000000")
        self.Scale3.configure(highlightcolor="black")
        self.Scale3.configure(highlightthickness="0")
        self.Scale3.configure(orient="horizontal")
        self.Scale3.configure(troughcolor="#200fbc")
        self.Scale3.configure(width=8)
        rpm_:object = self.Scale3.get()
        # CRANK SPPED LABEL
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.550, rely=0.785, height=31, width=119)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''CRANK SPEED''')

        #mph
        def mph(mph_: int = 0):
            mph_ = int(mph_)
            self.Canvas1.delete("tag4")
            self.Canvas1.create_text (260, 260, text=mph_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag4")
        self.Scale3_1 = tk.Scale(top,command=mph, from_=0.0, to=35.0)
        self.Scale3_1.place(relx=0.173, rely=0.782, relwidth=0.078, relheight=0.0, height=37, bordermode='ignore')
        self.Scale3_1.configure(activebackground="#39ede1")
        self.Scale3_1.configure(background="#000000")
        self.Scale3_1.configure(borderwidth="0")
        self.Scale3_1.configure(font="TkTextFont")
        self.Scale3_1.configure(foreground="#ffffff")
        self.Scale3_1.configure(highlightbackground="#000000")
        self.Scale3_1.configure(highlightcolor="black")
        self.Scale3_1.configure(highlightthickness="0")
        self.Scale3_1.configure(orient="horizontal")
        self.Scale3_1.configure(troughcolor="#200fbc")
        self.Scale3_1.configure(width=8)
        mph_:object = self.Scale3_1.get()
         #VECHILE SPEED LABEL
        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.05, rely=0.790, height=31, width=139)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#000000")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#ffffff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''VEHICLE SPEED''')
        self.Label1_3.configure(width=139)

        # Time label
        self.Label0 = tk.Label(top)
        self.Label0.place(relx=0.312, rely=0.100, height=30, width=250)
        self.Label0.configure(activebackground="#39ede1")
        self.Label0.configure(activeforeground="#000000")
        self.Label0.configure(background="#ffffff")
        self.Label0.configure(disabledforeground="#a3a3a3")
        self.Label0.configure(foreground="#ffffff")
        self.Label0.configure(highlightbackground="#79c8d8")
        self.Label0.configure(highlightcolor="black")
        self.Label0.configure(text= (datetime.datetime.today()),font=("Arial", 12),fg="#000000")

       
if __name__ == '__main__':

    vp_start_gui()





