from tkinter import *


FONT = ("Arial", 14)
PADDING = 20
window = Tk()
window.title("Miles to KM Conversion")
window.minsize(width=100, height=100)
window.config(padx=PADDING, pady=PADDING)


def convert_from_miles_to_km():
    conversion = float(input.get()) * 1.61
    result.config(text=str(round(conversion, 3)))


miles = Label(text="Miles", font=FONT)
miles.grid(row=0,column=2)

equal = Label(text="is equal to", font=FONT)
equal.grid(row=1,column=0)

result = Label(text="0", font=FONT)
result.grid(row=1,column=1)

km = Label(text="KM", font=FONT)
km.grid(row=1,column=2)

input = Entry(textvariable=0)
input.grid(row=0,column=1)


button = Button(text="Calculate", command=convert_from_miles_to_km)
button.grid(row=2,column=1)


window.mainloop()
