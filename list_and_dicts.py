def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Julio', 'lastname': 'Romero'}

    super_list = [
        {'firstname': 'Julio', 'lastname': 'Romero'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Rodelo'},
        {'firstname': 'Susana', 'lastname': 'Martinez'},
        {'firstname': 'Jose', 'lastname': 'Testo'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'float_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print('-'.join())




if __name__ == '__main__':
    run()