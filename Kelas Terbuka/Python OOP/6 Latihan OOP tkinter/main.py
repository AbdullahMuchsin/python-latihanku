# BELAJAR OOP TKINTER CLASS AND METHOD

import tkinter

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text="Label",)
label1 = tkinter.Label(main_window, text="Label",)

buttom = tkinter.Button(main_window, text="Click Here")
buttom2 = tkinter.Button(main_window, text="Click Here")


label.pack()
buttom.pack()

label1.pack()
buttom2.pack()

main_window.mainloop()