from tkinter import *
from tkinter import ttk

def convertir():
    number = float(enter_number.get())
    sliding1 = sliding_option.get()
    sliding2 = sliding_option2.get()
    if sliding1 == "Celsius" and sliding2 == "Fahrenheit":
        fahrenheit = (number * 9 / 5) + 32
        label_resultado.config(text=f"Resultado: {fahrenheit} Fahrenheit")
    elif sliding2 == "Fahrenheit" and sliding1 == "Celsius":
        celsius = (number - 32) * 5 / 9
        label_resultado.config(text=f"Resultado: {celsius} Celcius")
    else:
        label_resultado.config(text=f"Resultado: {number}")

    enter_number.delete(0, END)


# iniciar Tkinter
app = Tk()
app.geometry('220x300')
app.resizable(False, False)
app.title('Conversor de Unidades')

# label
label_valor = Label(app, text="\n\n\nValor:")
label_valor.pack()

# ingresar número
enter_number = Entry(app, width=20)
enter_number.pack()

label_de = Label(app, text="De:")
label_de.pack()

# opción deslizable
sliding_option = ttk.Combobox(app, values=["Celsius", "Fahrenheit"])
sliding_option.pack()
sliding_option.current(0)

label_a = Label(app, text="A:")
label_a.pack()

# opción deslizable
convertions = ["Celsius", "Fahrenheit"]
sliding_option2 = ttk.Combobox(app, values=convertions)
sliding_option2.pack()
sliding_option2.current(1)


# boton convertir
convert = Button(app, text="Convertir", command=convertir)
convert.pack()


label_resultado = Label(app, text="Resultado:")
label_resultado.pack()

# cerrar tkinter
app.mainloop()