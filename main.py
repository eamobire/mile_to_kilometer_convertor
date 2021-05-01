from tkinter import *


def mile_km():
    miles = miles_entry.get()
    km = float(miles) * 1.60934
    converted_result_label.config(text=f"{round(km, 2)}")


window = Tk()
window.title("Mile to Kilometer convertor")
# window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

miles_label = Label(text="miles")
miles_label.grid(column=3, row=1)

conversion_label = Label(text="is equal to")
conversion_label .grid(column=1, row=2)

km_label = Label(text="km")
km_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=mile_km)
calculate_button.grid(column=2, row=3)

miles_entry = Entry(width=7)
miles_entry.grid(column=2, row=1)

converted_result_label = Label(text=0)
converted_result_label.grid(column=2, row=2)

window.mainloop()
