#Programa creado por Jeremias Barolo.

#Invocaciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Root
root = Tk()
root.minsize(500, 500)
root.title("Manejo de Articulos")
root.resizable(0,0)

# Pantallas


def home():

    
    homelabel.config(
        fg="White",
        bg="Black",
        font= ("Arial", 30),
        padx=210,
        pady=20
    )
    homelabel.grid(row=0, column=0)

    productosbox.grid(row=1)

     #listar productos
    for producto in productos:
        if len(producto)== 3:
            producto.append("Añadido")
            Label(productosbox, text=producto[0]).grid()
            Label(productosbox, text=producto[1]).grid()
            Label(productosbox, text=producto[2]).grid()
            Label(productosbox, text="--------").grid()


    addlabel.grid_remove()
    infolabel.grid_remove()
    datalabel.grid_remove()
    addframe.grid_remove()

    return True











def info():
    
    infolabel.config(
        fg="White",
        bg="Black",
        font= ("Arial", 30),
        padx=150,
        pady=20
    )
    infolabel.grid(row=0, column=0)
    datalabel.grid(row=1, column=0)

    #ocultar
    addlabel.grid_remove()
    homelabel.grid_remove()
    addframe.grid_remove()
    productosbox.grid_remove()
    return True













def add():
    #Encabezado
    addlabel.config(
        fg="White",
        bg="Black",
        font= ("Arial", 30),
        padx=108,
        pady=20
    )
    addlabel.grid(row=0, column=0, columnspan=4)

    homelabel.grid_remove()
    infolabel.grid_remove()
    datalabel.grid_remove()
    productosbox.grid_remove()
    
    #Campos de formulario 
    addframe.grid(row=1)


    addnamelabel.grid(row=1, column=0, padx=5, pady=5,)
    addnameentry.grid(row=1, column=1, padx=5, pady=5,sticky=W)
    addpricelabel.grid(row=2, column=0, padx=5, pady=5)
    addpriceentry.grid(row=2, column=1, padx=5, pady=5,sticky=W)
    add_description_label.grid(row=3, column=0, padx=5, pady=5)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5,sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        padx=5,
        pady=5
    )
    boton.grid(row=5,column=1, sticky=NW)
    boton.config(
        bg="grey",
        fg="white",
        

    )
    return True



def addproduct():
    productos.append([
        namedata.get(),
        pricedata.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    
    print(productos)

    namedata.set("")
    pricedata.set("")
    add_description_entry.delete("1.0", END)

    home()











#Variables importantes para "Campos de Formulario"
productos=[]
namedata = StringVar()
pricedata= StringVar()


#Definiciones de pantallas (para que reconozca a la hora de ocultar pantallas dentro de los def)
homelabel = Label(root, text="Inicio")
productosbox = Frame(root, width=250)

#Info
infolabel = Label(root, text="Informacion")
datalabel= Label(root, text="Creado por Jeremias acompañado de Natalia. -  2022")
#add
addlabel = Label(root, text="Añadir Productos")

#Campos del Formulario
addframe = Frame(root)

addnamelabel= Label(addframe,text="Nombre del Producto:")
addnameentry = Entry(addframe, textvariable=namedata)

addpricelabel= Label(addframe,text="Precio del producto:")
addpriceentry = Entry(addframe, textvariable=pricedata)

add_description_label= Label(addframe, text="Descripcion:")
add_description_entry= Text(addframe)

boton = Button(addframe, text="Guardar", command= addproduct)
home()



def salir():
    resultado= messagebox.askquestion("Salir", "Desea salir del programa?")

    if resultado != "no":
        root.destroy()

mimenu= Menu(root)
mimenu.add_command(label= "Inicio", command=home)
mimenu.add_cascade(label= "Añadir",command=add)
mimenu.add_command(label= "Informacion",command=info)
mimenu.add_command(label= "Salir", command=salir)
root.config(menu=mimenu)


root.mainloop()

#Programa creado por Jeremias Barolo.

