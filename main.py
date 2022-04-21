import tkinter


def button_clicked():
    print("I really got clicked")
    new_text = inp.get()
    my_label["text"] = new_text
    
    
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=50, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="I Am A Label")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row = 0)
my_label.config(padx=20, pady=20)


# Button
button = tkinter.Button(text="Do not click...", command=button_clicked)
# button.pack()
button.grid(column=1, row = 1)

# Entry
inp = tkinter.Entry(width=15)
# inp.pack()
inp.grid(column=2, row = 2)

# Text box
text = tkinter.Text(height=5, width=30)
text.focus() # .focus() Makes blinking cursor start here
# text.pack()


window.mainloop()