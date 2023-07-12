# BELAJAR MEMBUAT GUI TKINTER

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def tombol_click():
    pesan = f"Hai {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} kamu gantengg abizz"
    showinfo(title="Urgen For U", message=pesan)


window = tk.Tk()
window.geometry("500x400")
window.configure(background="gray")
window.resizable(False,False)
window.title("Matematika")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


# Input Frame
frame_window = ttk.Frame(window)
frame_window.pack(pady="20", padx="20", fill="x", expand=True)

# Label Nama Depan
label_depan = ttk.Label(frame_window, text="Masukan Nama Depan : ")
label_depan.configure(background="orange")
label_depan.pack(pady="10", padx="10", fill="x", expand=True)

# Enntry Nama Depan
label_depan = ttk.Entry(frame_window, textvariable=NAMA_DEPAN)
label_depan.pack(pady="10", padx="10", fill="x", expand=True)

# Label Nama belakang
label_belakang = ttk.Label(frame_window, text="Masukan Nama Belakang: ")
label_belakang.configure(background="orange")
label_belakang.pack(pady="10", padx="10", fill="x", expand=True)

# Enntry Nama belakang
label_belakang = ttk.Entry(frame_window, textvariable=NAMA_BELAKANG)
label_belakang.pack(pady="10", padx="10", fill="x", expand=True)

# Label Button
label_button = ttk.Button(frame_window, text = "Sapa", command=tombol_click)
label_button.pack(pady="10", padx="10", fill="x", expand=True)


window.mainloop()

