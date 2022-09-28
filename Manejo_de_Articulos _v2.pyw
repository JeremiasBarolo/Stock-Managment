#Programa creado por Jeremias Barolo.


#Invocaciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
#root.geometry("500x500")
root.minsize(500, 500)
root.title("Manejo de Articulos")
root.resizable(0,0)

# Pantallas

#Pantalla Home
def home():

    
    homelabel.config(
        fg="White",
        bg="Black",
        font= ("Arial", 30),
        padx=210,
        pady=20
    )
    homelabel.grid(row=0, column=0)

    #productosbox.grid(row=1)
    productostable.grid(row=2)

    #listar productos
    for producto in productos:
        if len(producto)== 3:
            producto.append("Añadido")
            productostable.insert("", 0, text=producto[0], values=producto[1],)


    addlabel.grid_remove()
    infolabel.grid_remove()
    datalabel.grid_remove()
    addframe.grid_remove()

    return True

#Pantalla Informacion
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
    #productosbox.grid_remove()
    productostable.grid_remove()

    return True

#Pantalla Productos
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
    #productosbox.grid_remove()
    productostable.grid_remove()

    #Campos de formulario 
    addframe.grid(row=1)


    addnamelabel.grid(row=2, column=0, padx=5, pady=5)
    addnameentry.grid(row=2, column=1, padx=5, pady=5,sticky=E)
    addpricelabel.grid(row=3, column=0, padx=5, pady=5)
    addpriceentry.grid(row=3, column=1, padx=5, pady=5,sticky=E)
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
productos=[]#lista donde se guardan los datos
namedata = StringVar()#nombre
pricedata= StringVar()#precio



#Definiciones de pantallas (para que reconozca a la hora de ocultar pantallas dentro de los def)
homelabel = Label(root, text="Inicio")

Label(root).grid(row=1)
productostable = ttk.Treeview(height=12, columns=3)
productostable.grid(row=1, column=0,columnspan=4)
productostable.heading("#0", text="Producto",anchor=W)
productostable.heading("#1", text="Precio",anchor=W)



#Info
infolabel = Label(root, text="Informacion")
datalabel= Label(root, text="Creado por Jeremias Barolo. -  2022")
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


#Menu

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