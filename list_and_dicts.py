def run():
    my_list = [1, 'hello', True, 4.5]     #LISTAS
    my_dict = {'firstname': 'Julio', 'lastname': 'Romero'} #DICCIONARIOS
 
    super_list = [      #LISTAS QUE GUARDAN DICCIONARIOS
    [
        {'firstname': 'Julio', 'lastname': 'Romero'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Rodelo'},
        {'firstname': 'Susana', 'lastname': 'Martinez'},
        {'firstname': 'Jose', 'lastname': 'Testo'},
    ],
    [
        {'firstname': 'Rodrigo', 'lastname': 'Zapata'},
        {'firstname': 'Sumary', 'lastname': 'Tain'},
        {'firstname': 'Porto', 'lastname': 'Robles'},
        {'firstname': 'Sastre', 'lastname': 'Merlin'},
        {'firstname': 'Jesus', 'lastname': 'Tiesto'},
    ]
    ]

    # for i in super_list:
    #     print(i)

    super_dict = {        #DICCIONARIOS QUE GUARDAN LISTAS
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)




if __name__ == '__main__':
    run()