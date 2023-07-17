import tkinter as tk
import os
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
def show_entry_fields():
    a1=float(e1.get())
    a2=float(e2.get())
    a3=float(e3.get())
    a4=float(e4.get())
    a5=float(e5.get())
    os.remove("fisiere/test.txt")
    f = open("fisiere/test.txt", "a")
    f.write(str(a1)+'\n')
    f.write(str(a2)+'\n')
    f.write(str(a3)+'\n')
    f.write(str(a4)+'\n')
    f.write(str(a5)+'\n')
    f.close()
    os.remove("fisiere/enunt.txt")
    f1 = open("fisiere/enunt.txt", "a")
    f1.write('')
    f1.close()
    master.destroy()
def nott():
     os.remove("fisiere/enunt.txt")
     f = open("fisiere/enunt.txt", "a")
     f.write('')
     f.close()
     master.destroy()
R,I,C,S,H=get_values()
master = tk.Tk()
master.title("RLC serie")
tk.Label(master,text="Rezistenta:").grid(row=0)
tk.Label(master, text="Inductanta Bobinei:").grid(row=1)
tk.Label(master,text="Capacitatea Electrica:").grid(row=2)
tk.Label(master,text="Tensiunea Electrica a Sursei:").grid(row=3)
tk.Label(master,text="Frecventa Tensiunii Electrice:").grid(row=4)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4=tk.Entry(master)
e5=tk.Entry(master)
e1.insert(tk.END,R)
e2.insert(tk.END,I)
e3.insert(tk.END,C)
e4.insert(tk.END,S)
e5.insert(tk.END,H)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4,column=1)
tk.Button(master, text='Iesire',command=nott).grid(row=5, column=0,sticky=tk.W, pady=4)
tk.Button(master,text='START!',command=show_entry_fields).grid(row=6, column=1, sticky=tk.W, pady=4)
tk.mainloop()
