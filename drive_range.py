from tkinter import *
import tkinter
import tkinter as tk



#DRIVING RANGE CALCULATION

def calculate_range():
    efficiency = 0.65       # Efficiency (0.65 = 65%)
    battery_voltage = float(entry.get())           # Voltage in volts
    energy_consumption_rate = 0.2  # Energy consumption rate in kWh per mile
    battery_current = 50   #in Amph
    # Calculate the driving range in miles
    driving_range_miles = (battery_voltage*battery_current)
    result_label.configure(text="Driving Range: {:.2f} miles".format(driving_range_miles))

# Create the GUI window
root = tk.Tk()
root.title("Driving Range Calculator")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))
#Create an Integer Variable to set the initial value of Scale
var = IntVar(value=10)

#Create an Entry widget
entry = tk.Entry(root,width= 45,textvariable=var)
scale = Scale(root, from_=10, to=200, width= 20, orient="horizontal", variable=var)

entry.place(relx= .5, rely= .5, anchor= CENTER)
scale.place(relx= .5, rely= .6, anchor = CENTER)


# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_range)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Start the GUI event loop
root.mainloop()









