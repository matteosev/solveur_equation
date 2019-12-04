from tkinter import *
from tkinter.messagebox import *
from math import *

def resoudre():
    a = eval(tk_a.get())
    b = eval(tk_b.get())
    c = eval(tk_c.get())
    discriminant = b ** 2 - 4 * a * c
    texte = "discriminant = " + str(discriminant)
    tk_discriminant.set(texte)
    if a == 0:
        x1 = (-c) / b
    else:
        if discriminant > 0:
            x1 = (- b - sqrt(discriminant)) / (2 * a)
            x2 = (- b + sqrt(discriminant)) / (2 * a)
            facto = "factorisation => (x - " + str(x1) + ")(x - " + str(x2) + ")"
        elif discriminant == 0:
            x1 = (- b) / (2 * a)
            x2 = "1 seule racine"
            facto = "factorisation => " + str(a) + "(x - " + str(x1) + ")²"
        else:
            x1 = "pas de racine"
            x2 = "pas de racine"
            facto = "pas de factorisation possible"
    txt_x1 = "x1 = " +str(x1)
    tk_x1.set(txt_x1)
    txt_x2 = "x2 = " +str(x2)
    tk_x2.set(txt_x2)
    tk_facto.set(facto)
    
def open_help():
    showinfo("Aide","Vous pouvez entrez les coefficients d'un trinome sous sa forme developpee comme ceci 'ax² + bx + c'\nPour utiliser pi tapez 'pi', pour la racine carree d'un nombre 'sqrt(nombre)', sous forme de fraction '1/2' etc... toutes les fonctions du module math sont disponibles.\nL'algorithme utilise repose sur l'etude du signe du discriminant de l'équation.")

root = Tk()
root.title("Resolution d'une equation du 1er ou 2nd degre")
tk_a = StringVar()
tk_b = StringVar()
tk_c = StringVar()
tk_discriminant = StringVar()
tk_x1 = StringVar()
tk_x2 = StringVar()
tk_facto = StringVar()

menu = Menu(root)
menu.add_command(label = "Besoin d'aide ?", command = open_help)
root.config(menu = menu)

# entree des coefficients du trinome
top_frame = Frame(root, bd = 2, relief = "raised")
top_frame.grid(row = 0,padx = 10,pady = (10,0))

in_top_frame = Frame(top_frame)
in_top_frame.grid(padx = 5, pady = 5)

entry_a = Entry(in_top_frame, width = 5, textvariable = tk_a)
entry_a.grid(row = 0,column = 0)

lab_a = Label(in_top_frame, text = "x² + ")
lab_a.grid(row = 0,column = 1)

entry_b = Entry(in_top_frame, width = 5, textvariable = tk_b)
entry_b.grid(row = 0,column = 2)

lab_b = Label(in_top_frame, text = "x + ")
lab_b.grid(row = 0,column = 3)

entry_c = Entry(in_top_frame, width = 5, textvariable = tk_c)
entry_c.grid(row = 0,column = 4)

button_conv = Button(in_top_frame, text = "résoudre", command = resoudre)
button_conv.grid(row = 0, column = 5,padx = (10,0))
#====================================
# affichage des resultats
bot_frame = Frame(root, bd = 2, relief = "raised")
bot_frame.grid(row = 1, padx = 10, pady = 10)

in_bot_frame = Frame(bot_frame)
in_bot_frame.grid(padx = 5, pady = 5)

lab_discriminant = Label(in_bot_frame,textvariable = tk_discriminant)
lab_discriminant.grid(row = 1, column = 0)

lab_x1 = Label(in_bot_frame,textvariable = tk_x1)
lab_x1.grid(row = 2, column = 0)

lab_x2 = Label(in_bot_frame,textvariable = tk_x2)
lab_x2.grid(row = 3, column = 0)

lab_facto = Label(in_bot_frame,textvariable = tk_facto)
lab_facto.grid(row = 4, column = 0)
#====================================

root.mainloop()
