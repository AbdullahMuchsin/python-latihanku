''' Belajar Membuat Kalkulator Dengan tkinter '''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def hasil():
    angka1 = int(ANGKA1.get())
    angka2 = int(ANGKA2.get())
    operator = OPERATOR.get()

    if operator == "+":
        hasil = angka1 + angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    elif operator == "-":
        hasil = angka1 - angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    elif operator == "*":
        hasil = angka1 * angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    elif operator == "/":
        hasil = angka1 / angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    elif operator == "%":
        hasil = angka1 % angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    elif operator == "//":
        hasil = angka1 // angka2
        showinfo(title=f"hasil", message=f"{hasil}")
    else:
        hasil = "Maaf Operator tidak ditemuka"
        showinfo(title=f"hasil", message=f"{hasil}")

window = tk.Tk()
window.configure(bg="white")
window.geometry("500x500") # 250,000
window.title("Matematika")
window.minsize(400,500)
window.maxsize(400,500)

ANGKA1 = tk.StringVar()
ANGKA2 = tk.StringVar()
OPERATOR = tk.StringVar()

# Windwo Frame
window_frame = ttk.Frame(window)
window_frame.pack(pady="10",padx="10", expand=True, fill="x")

# Nama Label
nama_label = ttk.Label(window_frame, text="KALKULATOR SEDERHANA", anchor="center")
nama_label.pack(pady="10",padx="10", expand=True, fill="x")

# Nama Label pertama
nama_pertama = ttk.Label(window_frame, text="Masukan Angka pertama : ")
nama_pertama.pack(pady="10",padx="10", expand=True, fill="x")
# Entry Label pertama
entry_pertama = ttk.Entry(window_frame, textvariable=ANGKA1)
entry_pertama.pack(pady="10",padx="10", expand=True, fill="x")
# Nama Label kedua
nama_kedua = ttk.Label(window_frame, text="Masukan Angka kedua : ")
nama_kedua.pack(pady="10",padx="10", expand=True, fill="x")
# Nama Label kedua
nama_kedua = ttk.Entry(window_frame, textvariable=ANGKA2)
nama_kedua.pack(pady="10",padx="10", expand=True, fill="x")
# Nama Label operator
nama_operator = ttk.Label(window_frame, text="Masukan operator yang ingin digunaka (+,-,*,/,%,//)", anchor="center")
nama_operator.pack(pady="10",padx="10", expand=True, fill="x")
# Entry Label operator
nama_operator = ttk.Entry(window_frame, textvariable=OPERATOR)
nama_operator.pack(pady="10",padx="180", expand=True, fill="x")

# Button Hasil
enter_hasil = ttk.Button(window_frame, text="Hasil", command=hasil)
enter_hasil.pack(pady="10",padx="10", expand=True, fill="x")

window.mainloop(False)