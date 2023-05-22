#Calcultrice scientifique graphique avec Tkinter

from tkinter import *
from math import *

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculatrice Tkinter")

        #Initialisation :
        self.textvar=StringVar()
        self.operation = ""

        #Affichage :
        self.outpout = Entry(width=15, textvar=self.textvar,bg="powder blue", borderwidth=10, font=("Courier New",35,'bold'))
        self.outpout.grid(row=1,column=1,columnspan=5)
        #Placement du curseur sur la fenetre d'entrée
        self.outpout.focus()
        
        #Clear :
        self.boutonclear = Button(padx=14,pady=14, text="C", font=("Courier New",12,'bold') , command=self.clearbutton, background="light gray")
        self.boutonclear.grid(row=6,column=3, columnspan=1)

        #Chiffres :
        self.bouton0 = Button(padx=14,pady=14, text="0", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(0), background="light gray")
        self.bouton0.grid(row=5,column=2, columnspan=1)

        self.bouton1 = Button(padx=14,pady=14, text="1", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(1), background="light gray")
        self.bouton1.grid(row=4,column=3, columnspan=1)

        self.bouton2 = Button(padx=14,pady=14, text="2", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(2), background="light gray")
        self.bouton2.grid(row=4,column=2, columnspan=1)

        self.bouton3 = Button(padx=14,pady=14, text="3", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(3), background="light gray")
        self.bouton3.grid(row=4,column=1, columnspan=1)

        self.bouton4 = Button(padx=14,pady=14, text="4", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(4), background="light gray")
        self.bouton4.grid(row=3,column=1, columnspan=1)

        self.bouton5 = Button(padx=14,pady=14, text="5", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(5), background="light gray")
        self.bouton5.grid(row=3,column=2, columnspan=1)

        self.bouton6 = Button(padx=14,pady=14, text="6", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(6), background="light gray")
        self.bouton6.grid(row=3,column=3, columnspan=1)

        self.bouton7 = Button(padx=14,pady=14, text="7", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(7), background="light gray")
        self.bouton7.grid(row=2,column=1, columnspan=1)

        self.bouton8 = Button(padx=14,pady=14, text="8", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(8), background="light gray")
        self.bouton8.grid(row=2,column=2, columnspan=1)

        self.bouton9 = Button(padx=14,pady=14, text="9", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(9), background="light gray")
        self.bouton9.grid(row=2,column=3, columnspan=1)

        self.boutonpi = Button(padx=14,pady=14, text="π", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("pi"), background="light gray")
        self.boutonpi.grid(row=6,column=1, columnspan=1)

        #Opérateurs :
        self.boutonadd = Button(padx=14,pady=14, text="+", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("+"), background="light gray")
        self.boutonadd.grid(row=2,column=4, columnspan=1)

        self.boutonsub = Button(padx=14,pady=14, text="-", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("-"), background="light gray")
        self.boutonsub.grid(row=3,column=4, columnspan=1)

        self.boutonmult = Button(padx=14,pady=14, text="*", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("*"), background="light gray")
        self.boutonmult.grid(row=4,column=4, columnspan=1)

        self.boutondiv = Button(padx=14,pady=14, text="/", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("/"), background="light gray")
        self.boutondiv.grid(row=5,column=4, columnspan=1)

        self.boutonequal = Button(padx=14,pady=14, text="=", font=("Courier New",12,'bold') , command=self.equalbutton, background="light gray")
        self.boutonequal.grid(row=6,column=2, columnspan=1)
        #La touche "=" est relié à la touche Entrée du clavier
        self.bind("<Return>", self.touche_entree_clavier) 

        self.boutondecimal = Button(padx=14,pady=14, text=".", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("."), background="light gray")
        self.boutondecimal.grid(row=6,column=4, columnspan=1)
        

        #Fonctions :
        self.boutonsqrt = Button(padx=14,pady=14, text=" √ ", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("sqrt("), background="light gray")
        self.boutonsqrt.grid(row=2,column=5, columnspan=1)

        self.boutonsin = Button(padx=14,pady=14, text="sin", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("sin("), background="light gray")
        self.boutonsin.grid(row=4,column=5, columnspan=1)

        self.boutoncos = Button(padx=14,pady=14, text="cos", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("cos("), background="light gray")
        self.boutoncos.grid(row=5,column=5, columnspan=1)

        self.boutontan = Button(padx=14,pady=14, text="tan", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("tan("), background="light gray")
        self.boutontan.grid(row=6,column=5, columnspan=1)

        self.boutonpar1 = Button(padx=14,pady=14, text="(", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("("), background="light gray")
        self.boutonpar1.grid(row=5,column=1, columnspan=1)

        self.boutonpar2 = Button(padx=14,pady=14, text=")", font=("Courier New",12,'bold') , command=lambda:self.clickbutton(")"), background="light gray")
        self.boutonpar2.grid(row=5,column=3, columnspan=1)

        self.boutonsquare = Button(padx=14,pady=14, text=" ² ", font=("Courier New",12,'bold') , command=lambda:self.clickbutton("**2"), background="light gray")
        self.boutonsquare.grid(row=3,column=5, columnspan=1)
        
    #Bouttons
    def clearbutton(self):
        self.operation=""
        self.textvar.set("")
     
    def clickbutton(self, number):
        #Recupération des données si l'utilisateur à écrit au clavier
        self.operation=str(self.outpout.get())
        #Si la dernière opération était une erreur, on réinitialise
        if self.operation=="Error":
            self.operation=""
        #Recupération des données du bouton
        self.operation += str(number)
        self.textvar.set(self.operation)

    def equalbutton(self):
        try :
            #Si il n'y a aucun calcul à faire, on affiche 0
            if self.operation=="":
                self.textvar.set(str(0))
            #Recuperation des données si l'utilisateur à écrit au clavier
            self.operation=str(self.outpout.get())
            self.textvar.set(self.operation)
            #Calcul du résultat
            self.result=str(eval(self.operation))
            self.textvar.set(self.result)
            self.operation=self.result
        except :
            #Si le calcul est impossible :
            self.textvar.set("Error")

    def touche_entree_clavier(self, event):
        #Si la touche entrée à été presser, on appelle la fonction equalbutton
        self.equalbutton()

def main():
    maFenetre=Fenetre()
    maFenetre.mainloop()

if __name__ == '__main__':
    main()
    