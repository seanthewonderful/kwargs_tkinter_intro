import tkinter


def click():
    pass


def mi_to_km():
    miles = float(miles_inp.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to KM Converter")
# window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

miles_inp = tkinter.Entry(width=7)
miles_inp.grid(column=1, row =0)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row =0)

eq_label = tkinter.Label(text="is equal to")
eq_label.grid(column=0, row =1)

km_result = tkinter.Label(text="0")
km_result.grid(column= 1, row =1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row =1)

calculate_button = tkinter.Button(text="Calculate", command=mi_to_km)
calculate_button.grid(column=1, row =2)




window.mainloop()