import tkinter as tk
import os
from math import sqrt
master = tk.Tk()
master.title("Meniu de variabile")
variable = tk.StringVar(master)
variable.set("Pulsatia oscilatiilor propii")
pi=3.14
def get_values():
   with open('fisiere/test.txt') as f:
    content = f.readlines()
    li = [x.strip() for x in content]
    re=float(li[0])
    imp=float(li[1])
    cap=float(li[2])
    vol=float(li[3])
    her=float(li[4])
   return re,imp,cap,vol,her
def ok():
    os.remove("fisiere/enunt.txt")
    f = open("fisiere/enunt.txt", "a")
    if(variable.get()=="Pulsatia oscilatiilor propii"):
     R,I,C,S,H=get_values()
     G=1/sqrt(I*C)
     G=round(G,3)
    if(variable.get()=="Frecventa oscilatiilor propii"):
     R,I,C,S,H=get_values()
     G=1/(2*pi*sqrt(I*C))
     G=round(G,3)
    if(variable.get()=="Perioada oscilatiilor propii"):
     R,I,C,S,H=get_values()  
     G=2*pi*sqrt(I*C)
     G=round(G,3)
    if(variable.get()=="Coeficientul de amortizare"):
     R,I,C,S,H=get_values()  
     G=R/(2*I)
     G=round(G,3)
    if(variable.get()=="Timpul de injumatatire"):
     R,I,C,S,H=get_values()  
     G=0.693*((2*float(I))/float(R))
     G=round(G,3)
    if(variable.get()=="Factorul de calitate"):
     R,I,C,S,H=get_values()  
     G=sqrt(4*I-R*R*C)/(2*R*sqrt(C))
     G=round(G,3)
    if(variable.get()=="Timpul de relaxare"):
     R,I,C,S,H=get_values()  
     G=2*I/R
     G=round(G,3)
    if(variable.get()=="Oscilatii efectuate in timpul t"):
     R,I,C,S,H=get_values()  
     G=sqrt(4*I-R*R*C)/(2*pi*R*sqrt(C))
     G=round(G,3)
    if(variable.get()=="Decrementul logaritmic"):
     R,I,C,S,H=get_values()  
     G=2*pi*R*sqrt(C)/(sqrt(4*I-R*R*C))
     G=round(G,3)
    f.write(variable.get()+" este "+str(G)) 
    f.close()
    master.destroy()
def nott():
    os.remove("fisiere/enunt.txt")
    f = open("fisiere/enunt.txt", "a")
    f.write('')
    f.close()
    master.destroy()
    os.system("game.exe")
w = tk.OptionMenu(master, variable, "Pulsatia oscilatiilor propii", "Frecventa oscilatiilor propii", "Perioada oscilatiilor propii","Coeficientul de amortizare","Timpul de injumatatire","Factorul de calitate","Decrementul logaritmic","Oscilatii efectuate in timpul t","Timpul de relaxare")
w.pack()
exit_button = tk.Button(master, text="Exit", command=nott)
exit_button.pack(pady=2)
ok_button = tk.Button(master, text="Calculeaza", command=ok)
ok_button.pack(pady=2)
tk.mainloop()

