#AKJDKJSAD
def menu(titulo,opciones):
    i=1
    print(titulo)
    print('==================')
    for opc in opciones:
        print(i,'.-',opc)
        i+=1
    print(i,'.-','Salir')
    opcion=input('Ingrese Opción: ')
    return opcion

def suma(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1+op2
    except:
        return None
def resta(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1-op2
    except:
        return None
def multiplicacion(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1*op2
    except:
        return None
def division(a,b):
    try:
        op1=int(a)
        op2=int(b)
        if op2==0:
            return None
        return op1/op2
    except:
        return None
    
def leernum(msg):
    num=int(input(msg))
    return num

while True:
    opc=menu('Menú Calculadora',['Sumar','Restar','Multiplicar','Dividir'])
    op1=leernum('Ingrese Operando 1')
    op2=leernum('Ingrese Operando 2')
    if opc=='1':
        print(suma(op1,op2))
    elif opc=='2':
        print(resta(op1,op2))
    elif opc=='3':
        print(multiplicacion(op1,op2))
    elif opc=='4':
        print(division(op1,op2))
    elif opc=='5':
        print('Hasta la vista Baby.....')
        break
    else:
        print('Opción Incorrecta')