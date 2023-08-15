from cgitb import text
from openpyxl import *
from tkinter import *
 
def focus1(event):
    fecha_field.focus_set()
 
def focus2(event):
    edad_field.focus_set()
 
 
def focus3(event):
    tipodeoperacion_field.focus_set()
 
 
def focus4(event):
    Especialidad_field.focus_set()
 
 
def focus5(event):
    dia_field.focus_set()
 
def clear():
    fecha_field.delete(0, END)
    edad_field.delete(0, END)
    tipodeoperacion_field.delete(0, END)
    Especialidad_field.delete(0, END)
    dia_field.delete(0, END)
 
 

if __name__ == "__main__":
     
    root = Tk()
 
    root.configure(background='light green')
 
    root.title("registration form")
 
    root.geometry("500x300")
 
    heading = Label(root, text="Form", bg="light green")
 
    fecha = Label(root, text="Mes", bg="light green")
 
    edad = Label(root, text="Edad", bg="light green")
 
    tipodeoperacion = Label(root, text="Tipo de operación", bg="light green")
 
    Especialidad = Label(root, text="Especiliadad", bg="light green")
 
    dia = Label(root, text="Dia", bg="light green")
    
    resultadO =  Label(root, text="La probabilidad de que la operacion se realice", bg="light green")
 
    heading.grid(row=0, column=1)
    fecha.grid(row=1, column=0)
    edad.grid(row=2, column=0)
    tipodeoperacion.grid(row=3, column=0)
    Especialidad.grid(row=4, column=0)
    dia.grid(row=5, column=0)
    resultadO.grid(row=6, column=0)
   

    fecha_field = Entry(root)
    edad_field = Entry(root)
    tipodeoperacion_field = Entry(root)
    Especialidad_field = Entry(root)
    dia_field = Entry(root)
   
    fecha_field.bind("<Return>", focus1)
 
    edad_field.bind("<Return>", focus2)
 
    tipodeoperacion_field.bind("<Return>", focus3)

    Especialidad_field.bind("<Return>", focus4)

    dia_field.bind("<Return>", focus5)

    fecha_field.grid(row=1, column=1, ipadx="100")
    edad_field.grid(row=2, column=1, ipadx="100")
    tipodeoperacion_field.grid(row=3, column=1, ipadx="100")
    Especialidad_field.grid(row=4, column=1, ipadx="100")
    dia_field.grid(row=5, column=1, ipadx="100")

    info = []
    def button():
        info.clear()
        b0= 0.475120243
        b1=-0.000479802 #edad
        #dias
        b2=0
        b3=0.021509141
        b4=-0.074438055
        b5=0
        b6=0.016468207
        #meses
        b7=0
        b8=0.075159754
        b9=0.197875711
        b10=0.211726879
        b11=0.070344553
        b12=0.127336666
        b13=-0.093381745
        b14=0.104026792
        b15=0.200258782
        b16=0.165570556
        b17=-0.007438625
        b18=-0.013919735


        info.append(fecha_field.get())
        info.append(edad_field.get())
        info.append(tipodeoperacion_field.get())
        info.append(Especialidad_field.get())
        info.append(dia_field.get())

        x1=int(edad_field.get())

        a= str(dia_field.get())

        if a=='lunes':
            print('estoy en dia')
            x2,x3,x4,x5,x6=0,0,0,0,0
        else:
            print('no es lunes')
            
        if a=='martes':
            x3=1 
            x2,x4,x5,x6=0,0,0,0
        else:
            print('no es martes')
            
        if a=='miercoles':
            x4=1
            x2,x3,x5,x6=0,0,0,0
        else:
            print('no es miercoles')
            
        
        if a=='jueves':
            x5=1
            x2,x3,x4,x6=0,0,0,0
        else:
            print('no es jueves')
            
            
        if a=='viernes':
            x6=1
            x2,x3,x4,x5=0,0,0,0
        else: 
            print("no es un dia de la semana")
        
        b = str(fecha_field.get())
        
        if b=='enero':
            x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0,0
        else: 
            print('')
            
        if b=='febrero':
            x8=1
            x7,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")
            
        if b=='marzo':
            x9=1
            x7,x8,x10,x11,x12,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")
            
        if b=='abril':
            x10=1
            x7,x8,x9,x11,x12,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")      
        if b=='mayo':
            x11=1
            x7,x8,x9,x10,x12,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")               
        
        if b=='junio':
            x12=1        
            x7,x8,x9,x10,x11,x13,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")  
                        
        if b=='julio':
            x13=1         
            x7,x8,x9,x10,x11,x12,x14,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")               
                  
        if b=='agosto':
           x14=1        
           x7,x8,x9,x10,x11,x12,x13,x15,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")
                      
        if b=='septiembre':
            x15=1
            x7,x8,x9,x10,x11,x12,x13,x14,x16,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")       
               
        if b=='octubre':
            x16=1    
            x7,x8,x9,x10,x11,x12,x13,x14,x15,x17,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")            
                    
        if b=='noviembre':
            x17=1       
            x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x18=0,0,0,0,0,0,0,0,0,0,0
        else: 
            print("")    
        if b=='diciembre':
            x18=1
            x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17=0,0,0,0,0,0,0,0,0,0,0            
        else: 
            print("")
    
        resultado = float(b0+b1*x1+b2*x2+b3*x3+b4*x4+b5*x5+b6*x6+b7*x7+b8*x8+b9*x9+b10*x10+b11*x11+b12*x12+b13*x13+b14*x14+b15*x15+b16*x16+b17*x17+b18*x18)
        resultado= resultado*100
        if x18==1 or x9==1 or x15==1:
            resultado = str(resultado) +"% " + "El mejor dia para programar esta cirugia es el dia Martes"
            mylabel = Label(root, text = resultado).grid(row = 6, column =1)
        elif x8==1 or x11==1 or x12==1 or x13==1 or x14==1:
            resultado = str(resultado) +"% " + "El mejor dia para programar esta cirugia es el dia Miercoles"
            mylabel = Label(root, text = resultado).grid(row = 6, column =1)
        elif x16==1 or x17==1:
            resultado = str(resultado) +"% " + "El mejor dia para programar esta cirugia es el dia Viernes"
            mylabel = Label(root, text = resultado).grid(row = 6, column =1)
        elif x10==1:
            resultado = str(resultado) +"% " +"El mejor dia para programar esta cirugia es el dia Lunes"
            mylabel = Label(root, text = resultado).grid(row = 6, column =1)
        else: 
            resultado=str(resultado) +"% "
            mylabel = Label(root, text = resultado).grid(row = 6, column =1)


    
    resultado = StringVar()
    C = ""
    Submit = Button(root, text = "Submit", command = lambda: C==button())

    Submit.grid(row=8, column=1)

    root.mainloop()