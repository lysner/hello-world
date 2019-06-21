from array import *
from time import sleep as slp
import sys

# ======================== main menu ========================

def menu():
    print(' 1. Display\n 2. Add/Insert\n 3. Remove/Delete\n 4. Update\n')
    c = int(input('>>> '))
    if c == 1:
        return display()
    elif c == 2:
        return insert()
    elif c == 3:
        return delete()
    else:
        return update()

def loop():
    q = input('\nModify ur array?(y/n): ')
    if q == 'y' or q == 'Y':
        print()
        return menu()
    else:
        print('\nThank you!')
        print('Exiting please wait...\n\n')
        slp(3)
        sys.exit()
        sleep


# ======================== operations ========================

def display():
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    return loop()

def insert():
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    print('\nChoices:\n 1. Add element\n 2. Add elements\n')
    q = input('>>> ')
    if q == '1':
        vals = []
        idx = int(input('\nEnter location/index: '))
    for i in range(size):
        nums = int(input('Enter element: '))
        vals.append(nums)
    lst.insert(idx, vals)
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    return loop()

def delete():
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    print('\nChoices:\n 1. Remove an entire row\n 2. Remove an element\n 3. Remove all\n')
    c = int(input('>>> '))
    if c == 1:
        idx = int(input('Enter location of element: '))
        lst.pop(idx)
    elif c == 2:
        row = int(input('\nEnter row: '))
        col = int(input('Enter column: '))
        del lst[row][col]
    else:
        q = input('\nAre you sure?(y/n): ')
        if q == 'y' or q == 'Y':
            lst.clear()
            print('\nYour current array:\n')
            print('\tNone\n\n')
            sys.exit()
        else:
            return loop()
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    return loop()
        

def update():
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    row = int(input('\nEnter row: '))
    col = int(input('Enter column: '))
    val = int(input('Enter the element: '))
    lst[row][col] = val
    print('\nYour current array:\n')
    for i in lst:
        print('  ',i)
    return loop()

# ======================== inputs ========================

size = int(input('\n\nEnter row size: '))

if size > 4:
    print('\nSize must be 4 or less only.')
    raise IndexError

else:
    lst = []
    x, a, y = 0, 1, 1
    col = int(input('Enter column size: '))
    if col > 4:
      print('Invalid! size of elements must be 4 or less. ')
      raise IndexError
    for i in range(size):
        arr = []
        print(f'\nInput elements in array {y}:')
        for j in range(col):
            num = int(input(f'Enter element {a}: '))
            arr.append(num)
            a += 1
        lst.append(arr)
        a = 1
        x += 1
        y += 1
    print('\nHere\'s what you can do with your array.\n')
    menu()




    
    
