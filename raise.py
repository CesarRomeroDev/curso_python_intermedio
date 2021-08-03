def run():
#Cadena vacia
    # def palindrome(string):
    #     return string == string[: :-1]
    # try:
    #     print(palindrome(""))
    # except:
    #     print('solo texto')

#raise
    def palindrome(string):
        try:
            if len(string) == 0:      #si la longitud(len) del string es cero(si es una cadena vacia)
                raise ValueError('No se puede ingresar una cadena vacia')  #raise eleva el error 
            return string == string[: :-1]
        except ValueError as ve:  #except = si sucede un ValueError (as ve:)solo le damos un nombre al error (ve significa ValueError)
            print(ve)
            return False
    
    try:
        print(palindrome(''))
    except TypeError:
        print('Solo se puede ingresar texto')



if __name__ == '__main__':
    run()