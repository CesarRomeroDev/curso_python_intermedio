# def run():
#     my_dict = {}

#     for i in range(1, 101):
#         my_dict[i] = i**3
    
#     print(my_dict)



# if __name__ == '__main__':
#     run()

def run():
    dic = {i: i**2 for i in range(1, 101) if i % 3 != 0}
    print(dic)




if __name__ ==  '__main__':
    run()


# def run():
#     my_list = {i: i**1.5 for i in range(1, 1001)}
#     print(my_list)



if __name__ == '__main__':
    run()