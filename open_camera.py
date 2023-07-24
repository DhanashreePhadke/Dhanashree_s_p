from tkinter import *
import tkinter
import tkinter as tk
import cv2



def open_cam():
    vid = cv2.VideoCapture(0)


    while(True):

        ret, tk.Frame = vid.read()


        pt1 = (80,400)       # HORIZANTAL RED LEFT
        pt2 = (520,400)      # HORIZANTAL RED RIGHT
        pt3 = (45,480)       # VERTICAL RED LOWER LEFT
        pt4 = (560,480)      # VERTICAL RED LOWER RIGHT
        pt5 = (140,300)      # HORIZANTAL YELLOW LEFT
        pt6 = (470,300)      # HORIZANTAL YELLOW RIGHT
        pt7 = (200,200)      # HORIZANTAL GREEN LEFT
        pt8 = (410,200)      # HORIZANTAL GREEN RIGHT
        color = (0,0,255)
        color1 =(0,255,0)
        color2 = (0,165,255)
        cv2.line(tk.Frame,pt1,pt2,color,thickness=2,lineType=8)
        cv2.line(tk.Frame,pt3,pt1,color,thickness=2)
        cv2.line(tk.Frame,pt4,pt2,color,thickness=2)
        cv2.line(tk.Frame,pt5,pt6,color2,thickness=2)
        cv2.line(tk.Frame,pt1,pt5,color2,thickness=2)
        cv2.line(tk.Frame,pt2,pt6,color2,thickness=2)
        cv2.line(tk.Frame,pt7,pt8,color1,thickness=2)
        cv2.line(tk.Frame,pt5,pt7,color1,thickness=2)
        cv2.line(tk.Frame, pt6, pt8, color1, thickness=2)


        cv2.imshow('frame', tk.Frame)

        if cv2.waitKey(1) & 0xFF == ord('f'):
            break

# After the loop release the cap object
    vid.release()
   
# Destroy all the windows
cv2.destroyAllWindows()


open_cam()



