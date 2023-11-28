from tkinter import Tk, Canvas, Button, Label
import time
import math

class HorlogeDigitale:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Horloge Digitale")
        self.fenetre.geometry("400x400")
        self.fenetre.resizable(0, 0)

        self.canvas = Canvas(self.fenetre, width=400, height=400, bg='white')
        self.canvas.pack()

        # Créer un cercle autour de l'affichage numérique
        self.canvas.create_oval(50, 50, 350, 350, outline='black', width=2)

        self.label_heure = Label(self.fenetre, font=('Helvetica', 24), bg='white', fg='black')
        self.label_heure.place(relx=0.5, rely=0.5, anchor='center')

        self.bouton_quitter = Button(self.fenetre, text='Quitter', command=self.fenetre.quit)
        self.bouton_quitter.pack()

        self.afficher_heure()

    def afficher_heure(self):
        temps_actuel = time.localtime()
        heure = temps_actuel.tm_hour
        minute = temps_actuel.tm_min
        seconde = temps_actuel.tm_sec

        texte_heure = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)
        self.label_heure.config(text=texte_heure)

        self.fenetre.after(1000, self.afficher_heure)

if __name__ == "__main__":
    fenetre = Tk()
    horloge = HorlogeDigitale(fenetre)
    fenetre.mainloop()

# Boutons pour régler l'heure
bouton_heures_plus = Button(app_window, text="+", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("heures", 1))
bouton_heures_plus.grid(row=1, column=0)

bouton_heures_moins = Button(app_window, text="-", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("heures", -1))
bouton_heures_moins.grid(row=1, column=2)

bouton_minutes_plus = Button(app_window, text="+", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("minutes", 1))
bouton_minutes_plus.grid(row=2, column=0)

bouton_minutes_moins = Button(app_window, text="-", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("minutes", -1))
bouton_minutes_moins.grid(row=2, column=2)

bouton_secondes_plus = Button(app_window, text="+", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("secondes", 1))
bouton_secondes_plus.grid(row=3, column=0)

bouton_secondes_moins = Button(app_window, text="-", font=("Boulder", 14, 'bold'), command=lambda: regler_heure("secondes", -1))
bouton_secondes_moins.grid(row=3, column=2)