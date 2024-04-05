import tkinter as tk
###############################################################################
# DONE: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")

window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1, minsize=50)
window.rowconfigure([0, 1], weight=1, minsize=50)

frame1 = tk.Frame(master=window)
frame2 = tk.Frame(master=window)
frame3 = tk.Frame(master=window)
frame4 = tk.Frame(master=window)
frame5 = tk.Frame(master=window)
frame6 = tk.Frame(master=window)
frame7 = tk.Frame(master=window)
frame8 = tk.Frame(master=window)

frame_button = tk.Frame(master=window)



label1 = tk.Label(
    master=frame1, 
    text="Name",
    foreground="white",
    background="blue")

label2 = tk.Label(
    master=frame2, 
    text="Address Line 1",
    foreground="white",
    background="green")

label3 = tk.Label(
    master=frame3, 
    text="Address Line 2",
    foreground="white",
    background="teal")

label4 = tk.Label(
    master=frame4, 
    text="City",
    foreground="white",
    background="purple")

label5 = tk.Label(
    master=frame5, 
    text="State",
    foreground="black",
    background="cyan")

label6 = tk.Label(
    master=frame6, 
    text="Zip Code",
    foreground="white",
    background="red")

label7 = tk.Label(
    master=frame7, 
    text="Phone Number",
    foreground="white",
    background="orange")

label8 = tk.Label(
    master=frame8, 
    text="Email Address",
    foreground="black",
    background="yellow")

button = tk.Button(
    master=frame_button, 
    text="Submit",
    fg="black",
    bg="white")

frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

frame4.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

frame5.grid(row=0, column=5, sticky="nsew", padx=5, pady=5)

frame6.grid(row=0, column=6, sticky="nsew", padx=5, pady=5)

frame7.grid(row=0, column=7, sticky="nsew", padx=5, pady=5)

frame8.grid(row=0, column=8, sticky="nsew", padx=5, pady=5)

frame_button.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)



entry1 = tk.Entry(master=frame1)
entry2 = tk.Entry(master=frame2)
entry3 = tk.Entry(master=frame3)
entry4 = tk.Entry(master=frame4)
entry5 = tk.Entry(master=frame5)
entry6 = tk.Entry(master=frame6)
entry7 = tk.Entry(master=frame7)
entry8 = tk.Entry(master=frame8)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
label5.pack()
entry5.pack()
label6.pack()
entry6.pack()
label7.pack()
entry7.pack()
label8.pack()
entry8.pack()
button.pack()

window.mainloop()