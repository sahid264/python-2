from tkinter import *

window = Tk()
window.title("GUI PROGRAM")
window.minsize(width= 500, height= 300)
window.config(padx=100,pady=200)

# label

my_label = Label(text= "i am a label", font=("Arial",24))
# my_label.pack()

my_label.config(text="New text")
my_label.grid(column=0, row=0)



# button
def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text= new_text)


button = Button(text = "click me", command= button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# entry

input = Entry(width=50)
# input.pack()
print(input.get())
input.grid(column=3, row=2)





window.mainloop()