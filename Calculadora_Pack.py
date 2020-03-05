import tkinter as tk

ventanaC = tk.Tk()
ventanaC.title("Prueba posicionamiento con PLACE")
ventanaC.geometry('200x250')
def btnClik(num):
    global operador
    operador=operador+str(num)
    pan.set(operador)
def clear():
    global operador
    operador=("")
    pan.set("0")


def operacion():
    global operador
    try:
        opera=str(eval(operador))
    except:
        clear()
        opera=("ERROR")
    pan.set(opera)




pan= tk.IntVar()
operador=""
clear()

txtTitulo= tk.Label(ventanaC,text= "-----Calculadora------",bg="blue",fg="white")

txtTitulo.pack()
cajaMantisa = tk.Entry(ventanaC,textvariable=pan)
cajaMantisa.pack(fill=tk.X)





panel= tk.Frame(ventanaC, bg='grey',width=350,height=50)
panel.pack()


btnLimpiarMemoria = tk.Button(panel, text= "MC")
btnLimpiarMemoria.pack(side=tk.LEFT, ipadx=2,ipady=2)

btnMR = tk.Button(panel, text= "MR")
btnMR.pack(side=tk.LEFT, ipadx=2,ipady=2)

btnMemoriaSumar = tk.Button(panel, text= "M +")
btnMemoriaSumar.pack(side=tk.LEFT, ipadx=2,ipady=2)

btnMemoriaRestar = tk.Button(panel, text= "M - ")
btnMemoriaRestar.pack(side=tk.LEFT, ipadx=2,ipady=2)

btnMS = tk.Button(panel, text= "MS")
btnMS.pack(side=tk.LEFT, ipadx=2,ipady=2)

btnMv = tk.Button(panel, text= "Mv")
btnMv.pack(side=tk.LEFT, ipadx=2,ipady=2)


panel1= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel1.pack()

btnPorciento = tk.Button(panel1, text= "  %  ",command= lambda:btnClik("%"))
btnPorciento.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnRaiz = tk.Button(panel1, text= "  CE  ",command= lambda:clear())
btnRaiz.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnPtencia = tk.Button(panel1, text= " C ",command= lambda:clear())
btnPtencia.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnResiproco = tk.Button(panel1, text= "  <X|  ",command= lambda:clear())
btnResiproco.pack(side=tk.LEFT, ipadx=2,ipady=2)

##=======================================

panel2= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel2.pack()
btnIgual = tk.Button(panel2, text= "  1/x  ")
btnIgual.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnPunto = tk.Button(panel2, text= "  x^2  ",command= lambda:btnClik("**"))
btnPunto.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn0 = tk.Button(panel2, text= "  SQRT  ",command= lambda:btnClik(btnClik("sqrt(")))
btn0.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnMM = tk.Button(panel2, text= "  /  ",command= lambda:btnClik("/"))
btnMM.pack(side=tk.LEFT, ipadx=2,ipady=2)

##===================
panel3= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel3.pack()
btn1 = tk.Button(panel3, text= "  7  ",command= lambda:btnClik(7))
btn1.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn2 = tk.Button(panel3, text= "  8  ",command= lambda:btnClik(8))
btn2.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn3 = tk.Button(panel3, text= "  9  ",command= lambda:btnClik(9))
btn3.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnMas = tk.Button(panel3, text= "  X  ",command= lambda:btnClik("*"))
btnMas.pack(side=tk.LEFT, ipadx=2,ipady=2)

panel4= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel4.pack()
btn1 = tk.Button(panel4, text= "  4  ",command= lambda:btnClik(4))
btn1.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn2 = tk.Button(panel4, text= "  5  ",command= lambda:btnClik(5))
btn2.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn3 = tk.Button(panel4, text= "  6  ",command= lambda:btnClik(6))
btn3.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnMas = tk.Button(panel4, text= "  -  ",command= lambda:btnClik("-"))
btnMas.pack(side=tk.LEFT, ipadx=2,ipady=2)

panel5= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel5.pack()
btn1 = tk.Button(panel5, text= "  1  ",command= lambda:btnClik(1))
btn1.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn2 = tk.Button(panel5, text= "  2  ",command= lambda:btnClik(2))
btn2.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn3 = tk.Button(panel5, text= "  3  ",command= lambda:btnClik(3))
btn3.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnMas = tk.Button(panel5, text= "  +  ",command= lambda:btnClik("+"))
btnMas.pack(side=tk.LEFT, ipadx=2,ipady=2)


panel6= tk.Frame(ventanaC, bg='cyan',width=350,height=50)
panel6.pack()
btn1 = tk.Button(panel6, text= "  +/-  ",command= lambda:btnClik("-"))
btn1.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn2 = tk.Button(panel6, text= "  0  ",command= lambda:btnClik(0))
btn2.pack(side=tk.LEFT, ipadx=2,ipady=2)
btn3 = tk.Button(panel6, text= "  .  ",command= lambda:btnClik("."))
btn3.pack(side=tk.LEFT, ipadx=2,ipady=2)
btnMas = tk.Button(panel6, text= "  =  ",command= lambda:operacion())
btnMas.pack(side=tk.LEFT, ipadx=2,ipady=2)


ventanaC.mainloop()