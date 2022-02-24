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
        apples_to_sell = int(input(f"How many apples do you want to sell? You currently have {apples_available} apples:"))

        if apples_to_sell > apples_available:
            print("\nYou don't have enough apples :(")
        else:
            apples_available -= apples_to_sell
            balance += apples_to_sell * fruit_price

            apple_containers[apples_pointer] -= apples_to_sell

            if apple_containers[apples_pointer] <= 0 and (apples_pointer + 1) >= len(apple_containers):
                apple_containers[apples_pointer] = 0
            elif apple_containers[apples_pointer] <= 0:
                while apple_containers[apples_pointer] <= 0:
                    apples_pointer += 1
                    apple_containers[apples_pointer] += apple_containers[apples_pointer - 1]
                    apple_containers[apples_pointer - 1] = 0

        print_containers()
        print_menu()
    elif menu_option == '2':
        oranges_to_sell = int(input(f"How many oranges do you want to sell? You currently have {oranges_available} oranges:"))

        if oranges_to_sell > oranges_available:
            print("\nYou don't have enough oranges :(")
        else:
            oranges_available -= oranges_to_sell
            balance += oranges_to_sell * fruit_price

            orange_containers[oranges_pointer] -= oranges_to_sell

            if orange_containers[oranges_pointer] <= 0 and (oranges_pointer + 1) >= len(orange_containers):
                orange_containers[oranges_pointer] = 0
            elif orange_containers[oranges_pointer] <= 0:
                while orange_containers[oranges_pointer] <= 0:
                    oranges_pointer += 1
                    orange_containers[oranges_pointer] += orange_containers[oranges_pointer - 1]
                    orange_containers[oranges_pointer - 1] = 0

                    apple_containers[oranges_pointer - 1] = fruits_container
                    apples_available += fruits_container

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