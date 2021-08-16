def divisors(num):
    try:
        if num < 0:
            raise ValueError('No Debes Ingresar Numeros Negativos')
        divisors = [ i for i in range(1, num +1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input('ingresa un numero: '))
        print(divisors(num))
        print('termino mi programa')
    except ValueError:
        print('¡¡Solo Debes Ingresar numeros!!')



if __name__ == '__main__':
    run()