from tkinter import Tk, Entry, Button

def crear_ventana():
    ventana = Tk()
    ventana.title("Calculadora KJ")
    ventana.configure(bg="black")
    return ventana

def crear_entrada(ventana):
    entrada_Txt = Entry(ventana, font=("Calibri", 30), fg="white", bg="black")
    entrada_Txt.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
    return entrada_Txt

