# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
# email : raphael.attias@laplateforme.io

from tkinter import *
from time import *

vartype = True
alarmheure = ""
alarmmin = ""
pause_status = False
last_known_time = ""

def choix(choisit):
    global vartype
    vartype = choisit

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

def afficher_heure_tuple(heure_tuple):
    global vartype

    if len(heure_tuple) >= 6:
        heures, minutes, secondes = heure_tuple[3:6]
    else:
        heures, minutes, secondes = heure_tuple[0:3]

    if vartype:
        Label_temps.config(text=f"{heures:02d}:{minutes:02d}:{secondes:02d}")
    else:
        am_pm = "am" if heures < 12 else "pm"
        heures_12h_format = heures % 12 if heures % 12 != 0 else 12
        Label_temps.config(text=f"{heures_12h_format:02d}:{minutes:02d}:{secondes:02d} {am_pm}")

def afficher_heure_manuelle(heure_str):
    heure_tuple = strptime(heure_str, "%H:%M:%S")
    afficher_heure_tuple(heure_tuple)

def regler_heure_manuelle():
    heure_manuelle = heure_manuelle_entry.get()
    afficher_heure_manuelle(heure_manuelle)

def afficher_heure():
    global alarmheure, alarmmin, pause_status, last_known_time

    if not pause_status:
        current_time_tuple = localtime()
        if (alarmheure, alarmmin) == (strftime("%H"), strftime("%M")):
            alarm = True
        else:
            alarm = False
        if alarm:
            Label_temps.config(text="|| Alarme ||")
        else:
            afficher_heure_tuple(current_time_tuple)
    else:
        afficher_heure_tuple(strptime(last_known_time, "%H:%M:%S"))

    if heure_manuelle_entry.get():
        afficher_heure_manuelle(heure_manuelle_entry.get())

    fenetre.after(1000, afficher_heure)  # Planifier l'appel à afficher_heure après 1000 ms (1 seconde)

fenetre = Tk()
fenetre.resizable(width=False, height=False)
fenetre.geometry("200x200")
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

heure_manuelle_entry = Entry(fenetre, bd=2, width=9)
heure_manuelle_entry.grid(row=5, column=1)

btn_regler_manuelle = Button(fenetre, text="Régler Manuellement", command=regler_heure_manuelle)
btn_regler_manuelle.grid(row=5, column=2, columnspan=2)

afficher_heure()

fenetre.mainloop()
