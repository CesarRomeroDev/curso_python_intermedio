def run():

    # def palindrome(string):
    #     return string == string[ : :-1]
    # print(palindrome(1))

##try_except:
    def palindrome(string):
        return string == string[ : :-1]
    
    try:
        print(palindrome(1))
    except TypeError:           ##si sucede un typeError, vamos a ejecutar lo siguiente
        print('Solo Se Puede Ingresar Texto')  #un print : solo se pueden ingresar string
        
##try_except con funciones anonimas Lambda

    # palindrome = lambda string: string == string[ : :-1]
    # try:
    #     print(palindrome(1))
    # except TypeError:
    #     print('solo escribe texto :)')


if __name__ == '__main__':
    run()