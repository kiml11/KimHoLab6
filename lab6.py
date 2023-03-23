def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
# creates and prints the menu


def encoder(password):
    encoded_password = " "
    for x in password:
        temp_pass = int(x)
        temp_pass = int(temp_pass + 3) % 10
        encoded_password = encoded_password + str(temp_pass)
    return encoded_password


if __name__ == '__main__':
    while True:
        print_menu()
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            print(encoder(password))
        elif option == 2:
            password = input("Please enter your password to decode: ")
            print("The encoded password is, and the original password is \n")
        elif option == 3:
            break
