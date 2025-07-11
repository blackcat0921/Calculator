#CALCULADORA por Xiaxian
"""este programa es para aprender interfaces graficas de python y programar una aplicación calculador"""

import tkinter as tk #libreria: codigo programado por otra persona (interface gáfica)
#imporar tkinter i poner un mote, normalmente inicial de nombre de libreria.
#as para decir que utilizamos tk para referirnos a tkinter

###Funciones
def pulsar_tecla(tecla):
    actual=expresion.get()

    if actual=="¯\_(ツ)_/¯   " or actual=="404 Not found :(":
        actual=""
    elif actual == "0" and tecla in("1","2","3","4","5","6","7","8","9","0"):
        actual = ""
    elif actual[-1] in ("+","-","*","/") and tecla in ("+","-","*","/"):
        actual=actual[:-1]
    actual=actual+tecla
    expresion.set(actual)

def pulsar_igual():
    actual=expresion.get()
    try:
        resultado=eval(actual)
    except ZeroDivisionError:
        resultado="404 Not found :("
    except:
        resultado="¯\_(ツ)_/¯   "
    expresion.set(resultado)

def pulsar_limpiar():
    expresion.set("0")

###VENTANA PRINCIPAL
ventana_principal=tk.Tk() #tk crea una variable que almacena la ventana principal
ventana_principal.title("Calculadora") #Variable.title, para poner nombre a la ventana
#ventana_principal.geometry(f"{400}x{600}") #.geometry para modificar la medida base i altura, unidad pixeles
#(f"¨{base}x¨{altura}")

###Variables
marco=tk.Frame(ventana_principal)
expresion=tk.StringVar()
expresion.set("0")


###Etiqueta de pantalla
pantalla=tk.Label(marco, textvariable=expresion, font="Serif 25 bold",anchor="e")
#.label=etiqueta, font=tipo de letra
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5) #grid ubica dentro de la ventana 
#row=fila, columnspan=columnas que ocupa, sticky=siempre misma escala 比例, pady=separación

###Botón número 1
bot_1=tk.Button(marco, text="1", font="Serif 22", bg="white", command=lambda: pulsar_tecla("1"))
bot_1.grid(row=1, column=0, sticky="nsew", ipadx=5)#ipadx separacion de texto y marco, padx/pady separación botón

###Botón número 2
bot_2=tk.Button(marco, text="2", font="Serif 22", bg="white", command=lambda: pulsar_tecla("2"))
bot_2.grid(row=1, column=1, sticky="nsew", ipadx=5)

###Botón número 3
bot_3=tk.Button(marco, text="3", font="Serif 22", bg="white", command=lambda: pulsar_tecla("3"))
bot_3.grid(row=1, column=2, sticky="nsew", ipadx=5)

###Botón número 4
bot_4=tk.Button(marco, text="4", font="Serif 22", bg="white", command=lambda: pulsar_tecla("4"))
bot_4.grid(row=2, column=0, sticky="nsew", ipadx=5)

###Botón número 5
bot_5=tk.Button(marco, text="5", font="Serif 22", bg="white", command=lambda: pulsar_tecla("5"))
bot_5.grid(row=2, column=1, sticky="nsew", ipadx=5)

###Botón número 6
bot_6=tk.Button(marco, text="6", font="Serif 22", bg="white", command=lambda: pulsar_tecla("6"))
bot_6.grid(row=2, column=2, sticky="nsew", ipadx=5)

###Botón número 7
bot_7=tk.Button(marco, text="7", font="Serif 22", bg="white", command=lambda: pulsar_tecla("7"))
bot_7.grid(row=3, column=0, sticky="nsew", ipadx=5)#

###Botón número 8
bot_8=tk.Button(marco, text="8", font="Serif 22", bg="white", command=lambda: pulsar_tecla("8"))
bot_8.grid(row=3, column=1, sticky="nsew", ipadx=5)

###Botón número 9
bot_9=tk.Button(marco, text="9", font="Serif 22", bg="white", command=lambda: pulsar_tecla("9"))
bot_9.grid(row=3, column=2, sticky="nsew", ipadx=5)

###Botón número 0
bot_0=tk.Button(marco, text="0", font="Serif 22", bg="white", command=lambda: pulsar_tecla("0"))
bot_0.grid(row=4, column=1, sticky="nsew", ipadx=5)

###Botón borrar
bot_C=tk.Button(marco, text="C", font="Serif 22", bg="pink", command=pulsar_limpiar)
bot_C.grid(row=4, column=0, sticky="nsew", ipadx=5)

###Botón =
bot_ig=tk.Button(marco, text="=", font="Serif 22", bg="orchid2", command=pulsar_igual)
bot_ig.grid(row=4, column=2, sticky="nsew", ipadx=5)

###Botón +
bot_mas=tk.Button(marco, text="+", font="Serif 22", bg="SeaGreen1", command=lambda: pulsar_tecla("+"))
bot_mas.grid(row=1, column=3, sticky="nsew", ipadx=5)

###Botón -
bot_men=tk.Button(marco, text="-", font="Serif 22", bg="coral", command=lambda: pulsar_tecla("-"))
bot_men.grid(row=2, column=3, sticky="nsew", ipadx=5)

###Botón *
bot_mult=tk.Button(marco, text="*", font="Serif 22", bg="light sky blue", command=lambda: pulsar_tecla("*"))
bot_mult.grid(row=3, column=3, sticky="nsew", ipadx=5)

###Botón /
bot_div=tk.Button(marco, text="/", font="Serif 22", bg="khaki1", command=lambda: pulsar_tecla("/"))
bot_div.grid(row=4, column=3, sticky="nsew", ipadx=5)

marco.pack()
ventana_principal.mainloop() #abre la ventana y ejecutara el codigo en bucle, .mainloop=para siempre
