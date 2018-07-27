clothes = ['T-Shirt', 'Sweater']
option = ''

while option != 'E':
    option = input('Welcome to shop, what do you want (C, R, U, D)? ')
    if option == 'C' or option == 'c':
        clothes.append(input('Enter new item: '))
        print('Our items: ', end = '')
        print(*clothes, sep = ', ')
    elif option == 'R' or option == 'r':
        print('Our items: ', end = '')
        print(*clothes, sep = ', ')
    elif option == 'U' or option == 'U':
        up_pos = int(input('Update position? '))
        while up_pos - 1 > len(clothes) or up_pos - 1 < 0:
            print('Index not in clothes.')
            up_pos = int(input('Update position? '))
        new = input('New item? ')
        clothes[up_pos - 1] = new
        print('Our items: ', end = '')
        print(*clothes, sep = ', ')
    elif option == 'D' or option == 'D':
        del_pos = int(input('Delete position? '))
        while del_pos - 1 > len(clothes) or del_pos - 1< 0:
            print('Index not in clothes.')
            del_pos = int(input('Delete position? '))
        del clothes[del_pos - 1]
        print('Our items: ', end = '')
        print(*clothes, sep = ', ')
