from tkinter import *

root=Tk()
root.geometry("400x400")
root.config(bg="lightgreen")


class clase():
    def __init__(self):
        print("Vamoss a estar ocupando clases para generar elementos de dieño")
        
    def etqueta1(self):
        label_2=Label(root,text="Label creado")
        label_2.pack()
        
    def buton1(self):
        buton_1=Button(root,text="Button creado",command=self.message)
        buton1_.pack
        
    def combobox1(self):
        b=["Creaste un combobox usando clases","Hola"]
        combobox1=ttk.Combobox(root,state="readonly",values=b)
        conbobox1.plack
        
    def message(self):
        MessageBox.showinfo("Hola!")
        
    def elegir(self):
        global combobox
        c=combobox.get()
        if (c==Etiqueta()):
            self.etqueta1()
        if (c==Boton)():
            self.buton1()
        if (c==Combobox):
            self.combobox1()
            

a=["Boton","Etiqueta","Combobox"]
label_1=Label(root,text="Crea elementos de diseños utilizando clases")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
combobox=ttk.Combobox(root,state="readonly",values=a)
combobox.place(relx=0.5,rely=0.3,anchor=CENTER)
button_1=Button(root,text="Dame lick para generar el elemento de diseño deseado",command=clase)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()