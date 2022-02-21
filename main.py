import sys

number_containers = int(input("Please, insert number of containers: "))
fruits_container = int(input("Please, insert the number of fruits per container: "))
fruit_price = int(input("Please, insert orange price: "))

balance = 0
oranges_available = number_containers * fruits_container
apples_available = 0

orange_containers = [fruits_container for _ in range(0, number_containers)]
apple_containers = [0 for _ in range(0, number_containers)]

oranges_pointer = 0
apples_pointer = 0

def print_containers():
    global number_containers
    global fruits_container
    global oranges_available
    global apples_available
    global orange_containers
    global apple_containers
    global oranges_pointer
    global apples_pointer

    for i, oranges in enumerate(orange_containers):
        apples = apple_containers[i]
        print(f'Container {i + 1}: {oranges} oranges and {apples} apples')

def print_menu():
    global number_containers
    global fruits_container
    global fruit_price
    global balance
    global oranges_available
    global apples_available
    global orange_containers
    global apple_containers
    global oranges_pointer
    global apples_pointer
    
    print('\n \nORANGE SHOP MENU\n1 - Sell Apples \n2 - Sell Oranges\n3 - Show current balance\n4 - Show fruits available\n5 - Exit program')

    menu_option = input("Please, choose your option: ")

    if menu_option == '1':
        print_containers()
        print_menu()
    elif menu_option == '2':
        print_containers()
        print_menu()
    elif menu_option == '3':
        print(f'\nCurrent balance: ${balance} dollars')
        print_menu()
    elif menu_option == '4':
        print_containers()
        print_menu()
    elif menu_option == '5':
        sys.exit()
    else:
        print('Option invalid, please try again!')
        print_menu()

print_menu()