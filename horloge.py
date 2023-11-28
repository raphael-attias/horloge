from tkinter import *			
from time import *

#variables
vartype=True
alarmheure=""
alarmmin=""
def alarme():
    global alarmheure, alarmmin
    alarmheure= saisieheure.get()
    alarmmin= saisiemin.get()
def horaire():
    if(alarmheure==strftime("%H") and alarmmin==strftime("%M")):
        alarm=True
    else:
        alarm=False
    if alarm == True:
        Label_temps.config(text="|| Alarme ||")
    else:
        if vartype==True:
            Label_temps.config(text=strftime("%H:%M:%S"))
        else:
            Label_temps.config(text=strftime("%I:%M %p"))
    Label_temps.after(200, horaire)
def choix(choisit):
    global vartype
    vartype = choisit


fenetre = Tk()
fenetre.resizable(width=False, height=False) 
fenetre.geometry("200x100")
fenetre.configure(background="gray")
fenetre.title("Horloge")
Label_temps = Label(fenetre, font=(20), bg='white') 
Label_temps.grid(row=1, column=1, columnspan=3)
btn24 = Button(fenetre, text ="form 24h", command = lambda: choix(True))
btn24.grid(row=2, column=1, columnspan=1)
btn12 = Button(fenetre, text ="form 12h", command = lambda: choix(False))
btn12.grid(row=2, column=2, columnspan=1)
btnalarm = Button(fenetre, text ="set l'alarme", command = lambda: alarme())
btnalarm.grid(row=2, column=3, columnspan=1)
saisieheure = Entry(fenetre, bd = 2, width=9, textvariable=alarmheure)
saisieheure.grid(row=3, column=1)
Label_alarmhp = Label(fenetre, font=("",8), bg='white',text="Heure | Min") 
Label_alarmhp.grid(row=3, column=2)
saisiemin = Entry(fenetre, bd = 2, width=9,textvariable=alarmmin)
saisiemin.grid(row=3, column=3)
horaire()
fenetre.mainloop()