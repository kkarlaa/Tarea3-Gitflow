from botones import (
    boton1, boton2, boton3, boton4, boton5,
    boton6, boton7, boton8, boton9, boton0,
    boton_borrar, boton_parantesisIz, boton_parantesisDer, boton_punto,
    boton_div, boton_mult, boton_sum, boton_rest, boton_igualdad
)
from interfaz_entr_calcu import ventana

# Configuración de los botones para expandirse automáticamente
botones = [
    boton1, boton2, boton3, boton4, boton5,
    boton6, boton7, boton8, boton9, boton0,
    boton_borrar, boton_parantesisIz, boton_parantesisDer, boton_punto,
    boton_div, boton_mult, boton_sum, boton_rest, boton_igualdad
]

for i, boton in enumerate(botones):
    boton.grid(row=(i // 4) + 1, column=i % 4, sticky="nsew")  # Utiliza el método grid con sticky

# Configuración de la geometría para que los botones se expandan con la ventana
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1, uniform='equal')
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)