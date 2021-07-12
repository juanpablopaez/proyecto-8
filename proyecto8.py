##proyecto 8 Javier Rivera,Juan Pablo Paez 
import matplotlib.pyplot as plt #se importa la libreria matplotlib que con ella podemos hacer graficos
import pandas as pd #se importa pandas que nos ayuda a analisas datos y leer archivos
 #se crea una variable que leea el documento CasosNuevosSinSintomas.csv mediante un link 
x=pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto27/CasosNuevosSinSintomas.csv')
#funcion que hace mostrar todos los nombre de cada region por consola al usuario 
def MostarRegiones():
    print('1.- Arica y Parinacota')
    print('2.- Tarapacá')
    print('3.- Antofagasta')
    print('4.- Atacama')
    print('5.- Coquimbo')
    print('6.- Valparaíso')
    print('7.- Metropolitana')
    print("8.- O'Higgins")
    print('9.- Maule')
    print('10.- Ñuble')
    print('11.- Biobío')
    print('12.- Araucanía')
    print('13.- Los Ríos')
    print('14.- Los lagos')
    print('15.- Aysén')
    print('16.- Magallanes')
#muestra codigo de cada region al usuario 
def MostrarCodigo():
    print('Arica y Parinacota = 15')
    print('Tarapacá = 01')
    print('Antofagasta = 02')
    print('Atacama = 03')
    print('Coquimbo = 04')
    print('Valparaíso = 05')
    print('Metropolitana = 13')
    print("O'Higgins = 06")
    print('Maule = 07')
    print('Ñuble = 084')
    print('Biobío = 08')
    print('Araucanía = 09')
    print('Los Ríos =14')
    print('Los lagos = 10')
    print('Aysén = 11')
    print('Magallanes = 12')
#funcion que compara que region pidio el usuario o numero de region para mostar su grafico     
def IngresarRegion():
    nombre=input('ingrese: ')

    if nombre == 'Arica y Parinacota' or nombre=='arica y parinacota' or nombre=='15':
        Arica=x[0:1]
        print(Arica)
        ax=Arica.plot.bar()
        plt.show()
    elif nombre == 'Tarapacá' or nombre=='tarapacá' or nombre=='01' :
        Tarapacá=x[1:2]
        print(Tarapacá)
        ax=Tarapacá.plot.bar()
        plt.show()

    elif nombre == 'Antofagasta' or nombre=='antofagasta' or nombre=='02':
        Antofagasta=x[2:3]
        print(Antofagasta)
        ax=Antofagasta.plot.bar()
        plt.show()

    elif nombre== 'atacama' or nombre=='Atacama' or nombre=='03':
        Atacama=x[3:4]
        print(Atacama)
        ax=Atacama.plot.bar()
        plt.show()

    elif nombre== 'coquimbo' or nombre=='Coquimbo' or nombre=='04':
        Coquimbo=x[4:5]
        print(Coquimbo)
        ax=Coquimbo.plot.bar()
        plt.show()

    elif nombre== 'valparaíso' or nombre=='Valparaíso' or nombre=='05':
        Valparaíso=x[5:6]
        print(Valparaíso)
        ax=Valparaíso.plot.bar()
        plt.show()

    elif nombre=='Metropolitana' or nombre=='metropolitana' or nombre=='13':
        Metropolitana=x[6:7]
        print(Metropolitana)
        ax=Metropolitana.plot.bar()
        plt.show()

    elif nombre=="O'Higgins" or nombre=="o'higgins" or nombre=='06':
        OHiggins=x[7:8]
        print(OHiggins)
        ax=OHiggins.plot.bar()
        plt.show()

    elif nombre=='Maule' or nombre=='maule' or nombre=='07':
        Maule=x[8:9]
        print(Maule)
        ax=Maule.plot.bar()
        plt.show()

    elif nombre=='Ñuble' or nombre=='ñuble' or nombre=='084':
        Ñuble=x[9:10]
        print(Ñuble)
        ax=Ñuble.plot.bar()
        plt.show()

    elif nombre=='Biobío' or nombre=='biobío' or nombre=='08':
        Biobío=x[10:11]
        print(Biobío)
        ax=Biobío.plot.bar()
        plt.show()

    elif nombre=='Araucanía' or nombre=='araucanía' or nombre=='09':
        Araucanía=x[11:12]
        print(Araucanía)
        ax=Araucanía.plot.bar()
        plt.show()

    elif nombre=='Los Ríos' or nombre=='los ríos' or nombre=='14':
        Los_Ríos=x[12:13]
        print(Los_Ríos)
        ax=Los_Ríos.plot.bar()
        plt.show()

    elif nombre=='Los lagos' or nombre=='los lagos' or nombre=='10':
        Los_lagos=x[13:14]
        print(Los_lagos)
        ax=Los_lagos.plot.bar()
        plt.show()

    elif nombre=='Aysén' or nombre=='aysén' or nombre=='11':
        Aysén=x[14:15]
        print(Aysén)
        ax=Aysén.plot.bar()
        plt.show()

    elif nombre=='Magallanes' or nombre=='magallanes' or nombre=='12':
        Magallanes=x[15:16]
        print(Magallanes)
        ax=Magallanes.plot.bar()
        plt.show()
    else:
        print('ingrese nuevamente la region.')
        print('revise la ortografia(tildes, mayusculas, minusculas, etc.')
#grafica todas las regiones 
def AnalizarDatos():
    print('analizando todos los datos')
    ax=x.plot.bar()
    plt.show()

def CodigoRegion():#Llamamos a ingresarRegion para no escribir todo el código otra vez
    IngresarRegion()

def masYmenosContagios():
 print('region con mas contagios')
    Metropolitana=x[6:7]
    print(Metropolitana)
    ax=Metropolitana.plot.bar()
    plt.show()
    print('region con menos contagios')
    Aysén=x[14:15]
    print(Aysén)
    ax=Aysén.plot.bar()
    plt.show() 

       

def Salir():
    print('saliendo del programa')
def menu():
    opc=0
    salir=7
#creamos un  menu interactivo con un ciclo 
    while opc !=salir:
        #mostrar el menu
        print('===='*18)
        print('Menú')
        print ("1.- mostrar lista de regiones. ")
        print ("2.- mostrar el codigo de cada region.")
        print ("3.- ingresar una region. ")
        print ("4.- mostrar un grafico para todas las regiones. ")
        print ("5.- ingresar el codigo de la region ")
        print ("6.- para saber cual es la region con mas contagios y cual es que tiene menos contagios ")
        print ("7.- salir")
        opc=input("Digitar la opción: ")
        print('===='*18)


        if opc == '1':
            MostarRegiones()
        elif opc=='2':
            MostrarCodigo()
        elif opc=='3':
            IngresarRegion()
        elif opc=='4':
            AnalizarDatos()
        elif opc=='5':
            CodigoRegion()
        elif opc=='6':
            masYmenosContagios()
        elif opc=='7':
            Salir()
#hacemos un break para terminar el while del menu y asi terminar el programa
            break
menu()
