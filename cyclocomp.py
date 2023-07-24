from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import webbrowser
from tkinter import filedialog
import pygame


import glenn01_support

def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.attributes('-fullscreen', True) 

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

image_file = resource_path("one.gif")
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height, width=width, bg="black")
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

root.after(1, root.destroy)
root.mainloop()

def webPage():
    webbrowser.open("https://teamachillesefficycle.in/")
def youTube():
    webbrowser.open("https://www.youtube.com/channel/UCyZxb9mtrkIakqtIv2WpFnw")
def showmap():
    webbrowser.open("https://www.google.com/maps")













def add_song():
    file = filedialog.askopenfilename(initialdir="./", title="Select Song", filetypes=(("MP3 Files", "*.mp3"),))
    if file:
        playlist.append(file)  

# function to play the next song in the playlist
def play_next_song():
    global playlist_index
    playlist_index += 1
    if playlist_index >= len(playlist):
        playlist_index = 0
    pygame.mixer.music.load(playlist[playlist_index])
    pygame.mixer.music.play()
    update_current_song_label()

# function to play the previous song in the playlist
def play_previous_song():
    global playlist_index
    playlist_index -= 1
    if playlist_index < 0:
        playlist_index = len(playlist) - 1
    pygame.mixer.music.load(playlist[playlist_index])
    pygame.mixer.music.play()
    update_current_song_label()

# function to update the current song label
def update_current_song_label():
    current_song = playlist[playlist_index]
    current_song_label.config(text="Now playing: " + current_song)

#DRIVING RANGE CALCULATION

def calculate_range():
    battery_capacity = 100  # Battery capacity in kilowatt-hours (kWh)
    efficiency = 0.65       # Efficiency (0.65 = 65%)
    voltage = 48            # Voltage in volts
    energy_consumption_rate = 0.2  # Energy consumption rate in kWh per mile

    # Convert voltage from volts to kilowatts
    voltage_kw = voltage / 1000

    # Get the remaining battery power from the entry field
    remaining_battery = float(entry_battery.get())

    # Calculate the available energy in the battery
    available_energy = battery_capacity * efficiency

    # Calculate the driving range in miles
    driving_range_miles = (available_energy * remaining_battery) / (energy_consumption_rate * voltage_kw)

    result_label.configure(text="Driving Range: {:.2f} miles".format(driving_range_miles))

# Create the GUI window
window = tk.Tk()
window.title("Driving Range Calculator")

# Battery power input field
label_battery = tk.Label(window, text="Remaining Battery Power (%):")
label_battery.pack()
entry_battery = tk.Entry(window)
entry_battery.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_range)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()


def button1():
   
    imagelist = ["oh01.gif","oh02.gif","oh03.gif",
             "oh04.gif","oh05.gif","oh06.gif","oh07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button2():
   
    imagelist = ["sp01.gif","sp02.gif","sp03.gif",
             "sp04.gif","sp05.gif","sp06.gif","sp07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button3():
   
    imagelist = ["sgl01.gif","sgl02.gif","sgl03.gif",
             "sgl04.gif","sgl05.gif","sgl06.gif","sgl07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button4():
   
    imagelist = ["lth01.gif","lth02.gif","lth03.gif",
             "lth04.gif","lth05.gif","lth06.gif","lth07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button5():
   
    imagelist = ["term01.gif","term02.gif","term03.gif",
             "term04.gif","term05.gif","term06.gif","term07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button6():
   
    imagelist = ["hr01.gif","hr02.gif","hr03.gif",
             "hr04.gif","hr05.gif","hr06.gif","hr07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    

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
    def _init_(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        fname =file=resource_path("1227.jpeg")#"1226.png"
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

        self.Canvas1.create_text(540, 215, fill="#42f5d7", text=" °C", font=("Arial", 9))
        self.Canvas1.create_text(530, 335, fill="#42f5d7", text="BATTERY", font=("Arial", 9))
       
        
        self.Canvas1.create_text(290, 320, fill="#42f5d7", text="kPH", font=("Arial", 12))
        self.Canvas1.create_text(750, 320, fill="#42f5d7", text="RPM", font=("Arial", 12))
     
       

        def BATTERY(BATTERY_: int = 0):
            BATTERY_ = int(BATTERY_) 
            self.Canvas1.delete("tag2")
            self.Canvas1.create_text (500, 345, text=BATTERY_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag2")
           
        self.Scale2 = tk.Scale(top,command=BATTERY, from_=0.0, to=100)
        self.Scale2.place(relx=0.008, rely=0.92, relwidth=0.08, relheight=0.0
                , height=50, bordermode='ignore')
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
        BATTERY_:object = self.Scale2.get()

        def rpm(rpm_: int = 0):
            rpm_ = int(rpm_) 
            self.Canvas1.delete("tag3")
            self.Canvas1.create_text (710, 260, text=rpm_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag3")
           
        self.Scale3 = tk.Scale(top,command=rpm, from_=0.0, to=9000.0)
        self.Scale3.place(relx=0.008, rely=0.813, relwidth=0.078, relheight=0.0
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

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.09, rely=0.826, height=31, width=119)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''CRANK SPEED''')

        
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.098, rely=0.931, height=31, width=82)
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''BATTERY TEMP''')

        def mph(mph_: int = 0):
            mph_ = int(mph_) 
            self.Canvas1.delete("tag4")
            self.Canvas1.create_text (260, 260, text=mph_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag4")
           
        self.Scale3_1 = tk.Scale(top,command=mph, from_=0.0, to=210.0)
        self.Scale3_1.place(relx=0.273, rely=0.813, relwidth=0.078, relheight=0.0, height=37, bordermode='ignore')
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

        def amb(amb_: int = 0):
            amb_ = int(amb_) 
            self.Canvas1.delete("amb")
            self.Canvas1.create_text (515, 205, text=amb_, fill="#42f5d7", anchor='nw', font=("Arial", 12),tag="amb")
           
        
        self.Scale3_2 = tk.Scale(top,command=amb, from_=0.0, to=50.0)
        self.Scale3_2.place(relx=0.523, rely=0.813, relwidth=0.078, relheight=0.0
                , height=37, bordermode='ignore')
        self.Scale3_2.configure(activebackground="#39ede1")
        self.Scale3_2.configure(background="#000000")
        self.Scale3_2.configure(borderwidth="0")
        self.Scale3_2.configure(font="TkTextFont")
        self.Scale3_2.configure(foreground="#ffffff")
        self.Scale3_2.configure(highlightbackground="#000000")
        self.Scale3_2.configure(highlightcolor="black")
        self.Scale3_2.configure(highlightthickness="0")
        self.Scale3_2.configure(orient="horizontal")
        self.Scale3_2.configure(troughcolor="#200fbc")
        self.Scale3_2.configure(width=8)
        amb_:object = self.Scale3_2.get()

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.355, rely=0.833, height=31, width=139)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#000000")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#ffffff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''CAR SPEED''')
        self.Label1_3.configure(width=139)
       
        

        def parkOn():
            self.Canvas1.delete("parkOff")
            
        self.Button1_6 = tk.Button(top,command = parkOn)
        self.Button1_6.place(relx=0.523, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''ON''')
        self.Button1_6.configure(width=98)

        def parkOff():
            self.Canvas1.delete("parkOn")
            self.Canvas1.create_rectangle(510, 410, 555, 435, fill='black',tag="parkOff")
            
            
        self.Button1_6 = tk.Button(top,command = parkOff)
        self.Button1_6.place(relx=0.57, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''OFF''')
        self.Button1_6.configure(width=98)

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.833, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''AMBIENT TEMP''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.889, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''PARKING BRAKE''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.605, rely=0.938, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''DOOR LOCKS''')

        doorOpen = ('Doors Unlocked')
        def DoorOpen(do_: int = 50):
            rpm_ = int(do_) 
            self.Canvas1.delete("tagclosed","tagopen")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorOpen, font=("Arial", 12),tag="tagopen")
            
        self.Button1_6 = tk.Button(top,command=DoorOpen)
        self.Button1_6.place(relx=0.523, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''O''')
        
        doorClosed = ('Doors Locked')
        def DoorClosed(dc_: int = 12):
            rpm_ = int(dc_) 
            self.Canvas1.delete("tagopen","tagclosed")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorClosed, font=("Arial", 12),tag="tagclosed")
            
        self.Button1_6 = tk.Button(top,command=DoorClosed)
        self.Button1_6.place(relx=0.57, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''C''')

        
        
        

        self.Button1_9 = tk.Button(top,command=webPage)
        self.Button1_9.place(relx=0.814, rely=0.014, height=32, width=98)
        self.Button1_9.configure(activebackground="#39ede1")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#092bd8")
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(foreground="#ffffff")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''Info''')

        self.Button2_9 = tk.Button(top,command=youTube)
        self.Button2_9.place(relx=0.714, rely=0.014, height=32, width=98)
        self.Button2_9.configure(activebackground="#39ede1")
        self.Button2_9.configure(activeforeground="#000000")
        self.Button2_9.configure(background="#092bd8")
        self.Button2_9.configure(disabledforeground="#a3a3a3")
        self.Button2_9.configure(foreground="#ffffff")
        self.Button2_9.configure(highlightbackground="#d9d9d9")
        self.Button2_9.configure(highlightcolor="black")
        self.Button2_9.configure(pady="0")
        self.Button2_9.configure(text='''YouTube''')

        
        #SEAT BELT SYSTEM
        
        SEATBELTWEAR = ('NO NEED TO ALERT')
        def SEATBELTWEAR(NO_ALERT_: int = 50):
            rpm_ = int(NO_ALERT_) 
            self.Canvas1.delete("tagclosed","tagopen")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=NO_ALERT, font=("Arial", 12),tag="tagopen")
           
        self.Button1_6 = tk.Button(top,command=DoorOpen)
        self.Button1_6.place(relx=0.8, rely=0.15, height=32, width=60)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''NO ALERT''')
        
        SEATBELT_NOTWEAR = ('ALERT')
        def SEATBELT_NOTWEAR(ALERT_: int = 12):
            rpm_ = int(ALERT_) 
            self.Canvas1.delete("tagopen","tagclosed")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=ALERT, font=("Arial", 12),tag="tagclosed")
           
            
        self.Button1_6 = tk.Button(top,command=SEATBELT_NOTWEAR)
        self.Button1_6.place(relx=0.9, rely=0.15, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''ALERT''')

        

        #NAVIGATION

        self.Button3_8 = tk.Button(top,command=showmap)
        self.Button3_8.place(relx=0.9, rely=0.67, anchor=tk.E, height=32, width=98)
        self.Button3_8.configure(activebackground="#39ede1")
        self.Button3_8.configure(activeforeground="#000000")
        self.Button3_8.configure(background="#092bd8")
        self.Button3_8.configure(disabledforeground="#a3a3a3")
        self.Button3_8.configure(foreground="#ffffff")
        self.Button3_8.configure(highlightbackground="#d9d9d9")
        self.Button3_8.configure(highlightcolor="black")
        self.Button3_8.configure(pady="0")
        self.Button3_8.configure(text='''SHOW MAP''')
         
        
        self.Button3_8 = tk.Button(top,command=calculate_range)
        self.Button3_8.place(relx=0.9, rely=0.82, anchor=tk.E, height=32, width=98)
        self.Button3_8.configure(activebackground="#39ede1")
        self.Button3_8.configure(activeforeground="#000000")
        self.Button3_8.configure(background="#092bd8")
        self.Button3_8.configure(disabledforeground="#a3a3a3")
        self.Button3_8.configure(foreground="#ffffff")
        self.Button3_8.configure(highlightbackground="#d9d9d9")
        self.Button3_8.configure(highlightcolor="black")
        self.Button3_8.configure(pady="0")
        self.Button3_8.configure(text='''DRIVING RANGE''')
         





        #REVERSE PARKING

        self.Button2_8 = tk.Button(top,command=button6)
        self.Button2_8.place(relx=0.9, rely=0.95, anchor=tk.E, height=32, width=98)
        self.Button2_8.configure(activebackground="#39ede1")
        self.Button2_8.configure(activeforeground="#000000")
        self.Button2_8.configure(background="#092bd8")
        self.Button2_8.configure(disabledforeground="#a3a3a3")
        self.Button2_8.configure(foreground="#ffffff")
        self.Button2_8.configure(highlightbackground="#d9d9d9")
        self.Button2_8.configure(highlightcolor="black")
        self.Button2_8.configure(pady="0")
        self.Button2_8.configure(text='''RPS''')
           

        #MUSIC SYSTEM
        self.Button2_8 = tk.Button(top,command=add_song)
        self.Button2_8.place(relx=0.9, rely=0.33, anchor=tk.E, height=32, width=98)
        self.Button2_8.configure(activebackground="#39ede1")
        self.Button2_8.configure(activeforeground="#000000")
        self.Button2_8.configure(background="#092bd8")
        self.Button2_8.configure(disabledforeground="#a3a3a3")
        self.Button2_8.configure(foreground="#ffffff")
        self.Button2_8.configure(highlightbackground="#d9d9d9")
        self.Button2_8.configure(highlightcolor="black")
        self.Button2_8.configure(pady="0")
        self.Button2_8.configure(text='''PLAY SONG''')
        

        self.Button2_9 = tk.Button(top,command=play_previous_song)
        self.Button2_9.place(relx=0.9, rely=0.43, anchor=tk.E, height=32, width=98)
        self.Button2_9.configure(activebackground="#39ede1")
        self.Button2_9.configure(activeforeground="#000000")
        self.Button2_9.configure(background="#092bd8")
        self.Button2_9.configure(disabledforeground="#a3a3a3")
        self.Button2_9.configure(foreground="#ffffff")
        self.Button2_9.configure(highlightbackground="#d9d9d9")
        self.Button2_9.configure(highlightcolor="black")
        self.Button2_9.configure(pady="0")
        self.Button2_9.configure(text='''PREVIOUS SONG''')
        

        self.Button2_9 = tk.Button(top,command=play_next_song)
        self.Button2_9.place(relx=0.9, rely=0.53, anchor=tk.E, height=32, width=98)
        self.Button2_9.configure(activebackground="#39ede1")
        self.Button2_9.configure(activeforeground="#000000")
        self.Button2_9.configure(background="#092bd8")
        self.Button2_9.configure(disabledforeground="#a3a3a3")
        self.Button2_9.configure(foreground="#ffffff")
        self.Button2_9.configure(highlightbackground="#d9d9d9")
        self.Button2_9.configure(highlightcolor="black")
        self.Button2_9.configure(pady="0")
        self.Button2_9.configure(text='''NEXT SONG''')
        


        self.Button1_7 = tk.Button(top, command=root.destroy)
        self.Button1_7.place(relx=0.914, rely=0.014, height=32, width=98)
        self.Button1_7.configure(activebackground="#39ede1")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#092bd8")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#79c8d8")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''EXIT''')

if _name_ == '_main_':

    vp_start_gui()