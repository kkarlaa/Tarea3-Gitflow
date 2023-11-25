from tkinter import Button
from funciones_calcu import click_boton, borrar, operaciones
from interfaz_entr_calcu import ventana
#Botones
boton1 = Button(ventana, text="1", width= 5, height= 2, command= lambda: click_boton(1), bg="#797979", activebackground="#FFFFFF", fg="white",  font=("Calibri", 20))
boton2 = Button(ventana, text="2", width= 5, height= 2, command= lambda: click_boton(2), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton3 = Button(ventana, text="3", width= 5, height= 2, command= lambda: click_boton(3), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton4 = Button(ventana, text="4", width= 5, height= 2, command= lambda: click_boton(4), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton5 = Button(ventana, text="5", width= 5, height= 2, command= lambda: click_boton(5), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton6 = Button(ventana, text="6", width= 5, height= 2, command= lambda: click_boton(6), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton7 = Button(ventana, text="7", width= 5, height=     2, command= lambda: click_boton(7), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton8 = Button(ventana, text="8", width= 5, height= 2, command= lambda: click_boton(8), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton9 = Button(ventana, text="9", width= 5, height= 2, command= lambda: click_boton(9), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton0 = Button(ventana, text="0", width= 13, height= 2, command= lambda: click_boton(0), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))


boton_borrar = Button(ventana, text="DEL", width= 5, height= 2, command= lambda: borrar(), bg="#D2D2D2", activebackground="#FFFFFF", fg="black", font=("Calibri", 20))
boton_parantesisIz = Button(ventana, text="(", width= 5, height= 2, command= lambda: click_boton("("), bg="#D2D2D2", activebackground="#FFFFFF", fg="black", font=("Calibri", 20))
boton_parantesisDer = Button(ventana, text=")", width= 5, height= 2, command= lambda: click_boton(")"), bg="#D2D2D2", activebackground="#FFFFFF", fg="black",  font=("Calibri", 20))
boton_punto = Button(ventana, text=".", width= 5, height= 2, command= lambda: click_boton("."), bg="#797979", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))

boton_div = Button(ventana, text="÷", width= 5, height= 2, command= lambda: click_boton("*"), bg="#F1C208", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton_mult = Button(ventana, text="x", width= 5, height= 2, command= lambda: click_boton("*"), bg="#F1C208", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton_sum= Button(ventana, text="+", width= 5, height= 2, command= lambda: click_boton("+"), bg="#F1C208", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton_rest = Button(ventana, text="-", width= 5, height= 2, command= lambda: click_boton("-"), bg="#F1C208", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))
boton_igualdad = Button(ventana, text="=", width= 5, height= 2, command= lambda: operaciones(), bg="#F1C208", activebackground="#FFFFFF", fg="white", font=("Calibri", 20))

ventana.mainloop()