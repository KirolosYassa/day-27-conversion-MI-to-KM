from tkinter import *
from playground import * 

# result = calculate(2, add=2, multiply=3, multiply=2)
# print(result)

window = Tk()
window.title("New Project GUI")
window.minsize(width=500, height=300)
label = Label(text="Label", font=("Arial", 24))
label.grid(row=0,column=0)

input = Entry()
input.grid(row=2,column=3)

count = 0


# def increment_count(count):
#     count += 1
#     return count + 1


def got_clicked(counts):
    # counts = increment_count(count)    
    # counts += 1
    # new_text = f"Button Got Clicked {counts}!"
    new_text = f"Button Got Clicked {input.get()}!"
    label.config(text=new_text)

button = Button(text="Button", command=got_clicked)
button.grid(row=1,column=1)

new_button = Button(text="New button", command=got_clicked)
new_button.grid(row=0,column=2)


window.mainloop()
