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

# Code written by Danielle Samaroo
def decode(encoded_password):
    decode_password = "".join([str((int(digit) - 3) % 10) for digit in encoded_password])
    return decode_password


if __name__ == '__main__':
    encoded_password = ""
    while True:
        print_menu()
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            # I changed this because the first option is not supposed to print the password only store it
            #print(encoder(password))
            encoded_password = encoder(password)
        elif option == 2:
            # I removed this because you only needed one password input for both options
            #password = input("Please enter your password to decode: ")
            print(f"The encoded password is{encoded_password}, and the original password is {password}.\n")
        elif option == 3:
            break
