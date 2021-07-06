# def run():
#     squares = []                #creamos una lista bacia 
#     for i in range(1, 101):     #creamos un ciclo for de i al rango de 1 al 101
#         if i % 3 != 0:          #si a cada buelta el numero elavado a las 2 es divisible ante 3 y es diferente o igual a cero
#             squares.append(i**2) #vamos a gregar a la lista cada buelta a cada numero elevado a la 2 

#     print(squares)



# if __name__ == '__main__':
    #run()

def run():
    squares = [i**2 for i in range(1, 101) if i % 3 != 0] # Para cada i en el rango que va de 1 a 101 , voy a guardar esa i elevada al cuadrado, solamente si la i modulo 3 es distinto de 0 
    print(squares)



if __name__ == '__main__':
    run()

# def run():
#     squares = [i for i in range(1, 101) if i % 3 == 0 and  i % 6 == 0 and i % 9 == 0]
#     print(squares)



if __name__ == '__main__':
    run()
