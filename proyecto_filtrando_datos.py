DATA = [                                   #constante
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #todos los trabajadores que trabajan en python
    all_python_dev = [i['name'] for i in DATA if i ['language'] == 'python']  #list_comprehensions
    # for i in all_python_dev:
    #     print(i)
    
    ################################################################################################

    #todos los trbajadores en platzy
    all_platzi_worker = [i['name'] for i in DATA if i ['organization'] == 'Platzi'] #list_comprehensions
    # for i in all_platzi_worker:
    #     print(i)
        
    #######################################################################################3

    #todos los adultos mayor a 18 años
    adults = list(filter(lambda i: i['age'] > 18, DATA))
    adults = list(map(lambda i: i['name'], adults))
    # for i in adults:
    #     print(i)
    
    ##############################################################################

    #crear una nueva lista de diccionarios , pero que el lugar tengamos una llave mas llamada 'old', para saber si la persona
    #es mayor a 70 años y mandar True False.

    old_people = list(map(lambda i:{ **i, **{'old': i['age'] > 70}}, DATA ))
    for i in old_people:
        print(i)




if __name__ == '__main__':
    run()