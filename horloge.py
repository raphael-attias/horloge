# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#programme en-tete programme python
#version python : 
#auteur : ATTAS Raphaël
#email : raphael.attias@laplateforme.io


from tkinter import *
from time import *

# variables
vartype = True
alarmheure = ""
alarmmin = ""
pause_status = False  
last_known_time = ""

def alarme():
    global alarmheure, alarmmin
    alarmheure = saisieheure.get()
    alarmmin = saisiemin.get()

def pause_resume():
    global pause_status, last_known_time
    pause_status = not pause_status
    if not pause_status:
        last_known_time = strftime("%H:%M:%S")
    else:
        last_known_time = ""

def afficher_heure():
    if not pause_status:  
        if alarmheure == strftime("%H") and alarmmin == strftime("%M"):
            alarm = True
        else:
            alarm = False
        if alarm:
            Label_temps.config(text="|| Alarme ||")
        else:
            if vartype:
                Label_temps.config(text=strftime("%H:%M:%S"))
            else:
                Label_temps.config(text=strftime("%I:%M %p"))
    else:
        Label_temps.config(text=last_known_time) 

    Label_temps.after(200, afficher_heure)

def choix(choisit):
    global vartype
    vartype = choisit

fenetre = Tk()
fenetre.resizable(width=False, height=False)
fenetre.geometry("200x150")
fenetre.configure(background="#001F3F")
fenetre.title("Horloge")

Label_temps = Label(fenetre, font=(30), bg='white')
Label_temps.grid(row=1, column=1, columnspan=3)

btn24 = Button(fenetre, text="Fonct 24h", command=lambda: choix(True))
btn24.grid(row=2, column=1, columnspan=1)

btn12 = Button(fenetre, text="Fonct 12h", command=lambda: choix(False))
btn12.grid(row=2, column=2, columnspan=1)

btnalarm = Button(fenetre, text="Alarme", command=lambda: alarme())
btnalarm.grid(row=2, column=3, columnspan=1)

btn_pause = Button(fenetre, text="Pause/Reprendre", command=pause_resume)
btn_pause.grid(row=3, column=1, columnspan=3)

saisieheure = Entry(fenetre, bd=2, width=9, textvariable=alarmheure)
saisieheure.grid(row=4, column=1)

Label_alarmhp = Label(fenetre, font=("", 8), bg='grey', text="Heure | Min")
Label_alarmhp.grid(row=4, column=2)

saisiemin = Entry(fenetre, bd=2, width=9, textvariable=alarmmin)
saisiemin.grid(row=4, column=3)

afficher_heure()
fenetre.mainloop()
