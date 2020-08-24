from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        value = float(pies.get())
        metros.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

raiz = Tk()
raiz.title("Pies a Metros")

FramePrincipal = ttk.Frame(raiz, padding="3 3 12 12")

FramePrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) ## Vamos a usar Grid
raiz.columnconfigure(0, weight=1) ## En qué columna se va a encontrar
raiz.rowconfigure(0, weight=1)

pies = StringVar()  ## Estos son Cajones de texto, donde voy a insertar mi información
metros = StringVar()

LabelPies = ttk.Entry(FramePrincipal, width=7, textvariable=pies)
LabelPies.grid(column=2, row=1, sticky=(W, E)) 

ttk.Label(FramePrincipal, textvariable=metros).grid(column=2, row=2, sticky=(W, E))
ttk.Button(FramePrincipal, text="Calcula", command=calcular).grid(column=3, row=3, sticky=W)

ttk.Label(FramePrincipal, text="Pies").grid(column=3, row=1, sticky=W)
ttk.Label(FramePrincipal, text="es equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(FramePrincipal, text="metros").grid(column=3, row=2, sticky=W)

for hijo in FramePrincipal.winfo_children(): 
    hijo.grid_configure(padx=5, pady=5)

LabelPies.focus()

raiz.bind('<Return>', calcular)

raiz.mainloop()