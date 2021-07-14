def run():
    palindrome = lambda string: string == string[ : : -1]

    print(palindrome('pepe'))



if __name__ == '__main__':
    run()