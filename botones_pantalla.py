from botones import (
    boton1, boton2, boton3, boton4, boton5,
    boton6, boton7, boton8, boton9, boton0,
    boton_borrar, boton_parantesisIz, boton_parantesisDer, boton_punto,
    boton_div, boton_mult, boton_sum, boton_rest, boton_igualdad
)

#Agregando botones en pantalla.
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5, sticky="nsew")
boton_parantesisIz.grid(row = 1, column = 1, padx = 5, pady = 5, sticky="nsew")
boton_parantesisDer.grid(row = 1, column = 2, padx = 5, pady = 5, sticky="nsew")
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5, sticky="nsew")

boton7.grid(row = 2, column = 0, padx = 5, pady = 5, sticky="nsew")
boton8.grid(row = 2, column = 1, padx = 5, pady = 5, sticky="nsew")
boton9.grid(row = 2, column = 2, padx = 5, pady = 5, sticky="nsew")
boton_mult .grid(row = 2, column = 3, padx = 5, pady = 5, sticky="nsew")

boton4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="nsew")
boton5.grid(row = 3, column = 1, padx = 5, pady = 5, sticky="nsew")
boton6.grid(row = 3, column = 2, padx = 5, pady = 5, sticky="nsew")
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5, sticky="nsew")

boton1.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="nsew")
boton2.grid(row = 4, column = 1, padx = 5, pady = 5, sticky="nsew")
boton3.grid(row = 4, column = 2, padx = 5, pady = 5, sticky="nsew")
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5,sticky="nsew")

boton0.grid(row = 5, column = 0, columnspan= 2, padx= 5, pady = 5, sticky="nsew")
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5, sticky="nsew")
boton_igualdad.grid(row = 5, column = 3, padx = 5, pady = 5, sticky="nsew")
