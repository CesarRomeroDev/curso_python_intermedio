# Crea una lista de los 100 primeros numeros naturales

def run():
    LIMITE = 10001 
    contador = 0
    al_cuadrado = contador **2 

    while al_cuadrado < LIMITE:
        print(str(contador), str(al_cuadrado))
        contador += 1
        al_cuadrado = contador **2



if __name__ == '__main__':
    run()