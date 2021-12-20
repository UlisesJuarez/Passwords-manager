from tkinter import*
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genera_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letras= [choice(letters) for l in range(nr_letters)]
    simbolos=[choice(symbols) for s in range(nr_symbols)]
    numeros=[choice(numbers) for n in range(nr_numbers)]

    password_final=letras+simbolos+numeros
    shuffle(password_final)
    password = "".join(password_final)
    passEntrada.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def guardar():
    
    web=webEntrada.get()
    email=emailEntrada.get()
    pw=passEntrada.get()
    nuevo_dato={web:{
        "email":email,
        "password":pw,
    }}
    
    if len(web)==0 or len(pw)==0 or len(email)==0:
        messagebox.showinfo(title="Lo siento :(",message="Debes llenar todos los campos")
    else:
        try:
            with open("day 29 password manager/datos.json","r") as archivo_datos:
                #lee el dato anterior
                data=json.load(archivo_datos)
        except FileNotFoundError:
            with open("day 29 password manager/datos.json","w") as archivo_datos:
                json.dump(nuevo_dato,archivo_datos,indent=4)
        else:
            #actualiza ese dato
            data.update(nuevo_dato)
            with open("day 29 password manager/datos.json","w") as archivo_datos:
                #guarda ese dato
                json.dump(data,archivo_datos,indent=4)
        finally:
            webEntrada.delete(0,END)
            emailEntrada.delete(0,END)
            passEntrada.delete(0,END)
#----------------------------BUSCA PASSWORD-----------------------------#
def busca_pass():
    criterio=webEntrada.get()
    if len(criterio)==0:
        messagebox.showinfo(title="Error",message="Debes ingresar la web")
    else:
        try:
            with open("day 29 password manager/datos.json","r") as archivo_datos:
                data=json.load(archivo_datos)
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="El archivo de datos no existe")
        else:
            if criterio in data:
                email=data[criterio]["email"]
                password=data[criterio]["password"]
                messagebox.showinfo(title=criterio,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error",message=f"No tienes datos para '{criterio}' guardados")
# ---------------------------- UI SETUP ------------------------------- #


ventana=Tk()
ventana.title("Password manager")
ventana.minsize(width=400,height=400)
ventana.config(padx=20)
ventana.resizable(0,0)

canva=Canvas(width=200,height=250,highlightthickness=0)
passImage=PhotoImage(file="day 29 password manager/logo.png")
canva.create_image(125,125,image=passImage)
canva.grid(column=1,row=0,sticky="w")


webLabel=Label(text="Website:")
webLabel.grid(column=0,row=1)

webEntrada=Entry(width=30)
webEntrada.grid(column=1,row=1,sticky="w")
webEntrada.focus()

buscarBtn=Button(text="Buscar",command=busca_pass)
buscarBtn.grid(column=2,row=1,sticky="w")

emailLabel=Label(text="Email/Username:")
emailLabel.grid(column=0,row=2)

emailEntrada=Entry(width=30)
emailEntrada.grid(column=1,row=2,sticky="w")
emailEntrada.insert(0,"ulises@email.com")

passLabel=Label(text="Password:")
passLabel.grid(column=0,row=3)

passEntrada=Entry(width=30)
passEntrada.grid(column=1,row=3,sticky="w")

btnGeneraP=Button(text="Generate Password",command=genera_pw)
btnGeneraP.grid(column=2,row=3,sticky="w")

btnAgregar=Button(width=20, text="Add",command=guardar)
btnAgregar.grid(column=1, row=4)


ventana.mainloop()