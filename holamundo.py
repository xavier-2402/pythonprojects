numero = 7
numero =  10

persona1 = {
    "nombre":"Juan",
    "apellido":"Velez",
    "edad":32,
    "cedula":"512653718",
    "direccion":{
        "provincia":"Azuay",
        "canton":"Cuenca",
        "parroquia":"Ricaurte",
        "calle principal ":"Julia Bernal",
        "calle secundaria":"S/N",
        "numero casa":12
    }
}

persona2 = {
    "nombre":"Marco",
    "apellido":"Caja",
    "edad":32,
    "cedula":"5123784289",
    "soltero":False,
    "direccion":{
        "provincia":"Azuay",
        "canton":"Cuenca",
        "parroquia":"Ricaurte",
        "calle principal ":"Julia Bernal",
        "calle secundaria":"S/N"
    }
}

ListaPersona = [persona1,persona2]

nombre= persona1["direccion"]

##print (nombre)

'''for persona in ListaPersona:
    print(persona["nombre"])'''

persona3 = {
    "nombre":"Carlos",
    "apellido":"Villa",
    "edad":19,
    "cedula":"51237623",
    "soltero":  True,
    "direccion":{
        "provincia":"Azuay",
        "canton":"Cuenca",
        "parroquia":"Ricaurte",
        "calle principal ":"Julia Bernal",
    }
}

"""ListaPersona.append(persona3)

persona2['apellido']='Cueva'
ListaPersona.pop(1)"""
#print(ListaPersona)

'''for i in range(0,len(ListaPersona)):
    print(ListaPersona[i])'''

#print("persona1 actualizada")

persona1['nombres']='Andres'
#print(persona1)

arregloNumerico1=[1,2,3,4,5,6,7,8,9,10]
arregloNumerico2=[1,3,5,7,11,13,17,19]

def EliminarValoresDuplicados(arreglo1,arreglo2):
    a=set(arreglo1)
    b=set(arreglo2)

    sin_repetidos = a-b;
    return sin_repetidos


resultado =EliminarValoresDuplicados(arregloNumerico1,arregloNumerico2)
print(resultado)


arregloLetras=['a','b','c','d','a','e']
def contarDuplicados(arregloDatos):
    diccionarioLetras = {}
    for letras in arregloDatos:
        contador = arregloDatos.count(letras)
        print(diccionarioLetras.keys())
        if(letras in diccionarioLetras.keys()):
            print('valor duplicado ', letras)
            return diccionarioLetras
        else: 
            diccionarioLetras[letras]=contador

print(contarDuplicados(arregloLetras))


listaNumeros=[0,1,2,3,4,5,6,7,8,9,10,11,12]

def BuscarPares(lista):
    ListaPares =[]
    ListaImpares=[]

    for elemento in lista:
        if elemento%2 == 0 :
            ListaPares.append(elemento)
        else:
            ListaImpares.append(elemento)
    return ListaPares , ListaImpares

pares,impares = BuscarPares(listaNumeros)
print(pares)
print(impares)


ListaComprehension = [elemento for elemento in range (0,20)  if elemento%2==0] 
diccionarioDuplicado = {letra: arregloLetras.count(letra) for letra in arregloLetras}
print(ListaComprehension)
print(diccionarioDuplicado)


lugar ="el mundo"
lenguaje = "Python"
atributo =" el más rápido"

print(lenguaje+"es uno de los lenguajes mas utilizadosen "+lugar+" y es "+atributo)

print(f'{lenguaje} es uno de los lenguajes mas utilizadosen {lugar} y es {atributo} y 2+2 = {2+2}')

#FUNCIONES LAMBDA
incrementar = lambda x: x+1

print(incrementar(2))

imprimirtexto = lambda texto1,texto2 : f"{texto1 } es mayor que {texto2}"

print(imprimirtexto("Pedro","Juan"))

