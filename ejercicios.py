#!/usr/bin/python3 
#by Marzerp
#30/10/2023
#posiciones específicas

lista = [1, 2, 3, 4, 5]
print(lista[-3]) #ejercico 23
print(lista[-5:]) #ejercicio 24
print(lista[::2]) #ejercicio 25

def promedio(lista):
        suma=0
        for i in lista:
                suma+=i
        promedio=suma/len(lista)
        return promedio 

def desv_estandar(lista):
        pr=promedio(lista)
        suma=0
        for i in lista:
                suma+=(i-pr)**2
        ds=(suma/len(lista))**(1/2)
        return ds

print(desv_estandar([1,2,3,4,5]))


