#asd
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

print(menu('Menú Calculadora',['Sumar','Restar','Multiplicar','Dividir']))