def click_boton(entrada, valor):
    entrada.insert("end", valor)

def borrar(entrada):
    entrada.delete(0, "end")

def operaciones(entrada):
    ecuacion = entrada.get()
    resultado = eval(ecuacion)
    entrada.delete(0, "end")
    entrada.insert(0, resultado)