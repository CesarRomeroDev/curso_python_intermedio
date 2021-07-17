# def run():
#     my_list = [1, 2, 3, 4, 5]

#     for i in my_list:
#         i = i**2
#         print(i)



# if __name__ == '__main__':
#     run()
##############################################################################
# def run():
#     my_list = [1, 2, 3, 4, 5]

#     squares = [i**2 for i in my_list]

#     print(squares)



# if __name__ == '__main__':
#     run()
###############################################################################

def run():

    my_list = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, my_list))
    print(squares)



if __name__ == '__main__':
    run()