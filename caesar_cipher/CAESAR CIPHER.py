import string

def find_machine():
    machine = ""
    while machine not in ["e", "d"]:
        machine = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ").lower()
    if machine == "e":
        encrypt = True
    else:
        encrypt = False
    return encrypt

def find_shift():
    shift = input("Please enter the key (0 to 25) to use.\n> ")
    while int(shift) not in range(0,25):
        shift = input("Please enter the key (0 to 25) to use.\n> ")
    return int(shift)

def caesar_cipher_machine():
    print("Caesar Cipher, by B.P.X")
    alphabets = string.ascii_uppercase
    machine = find_machine()
    shift = find_shift()
    user_message = input("Enter the message to encrypt.\n> ")
    result = ""
    for char in user_message.upper():
        if char in alphabets:
            idx = alphabets.find(char)
            if machine:
                new_idx = (idx + shift) % 26
            else:
                new_idx = (idx - shift) % 26
            result += alphabets[new_idx]
        else:
            result += char
    return print(result)

caesar_cipher_machine()
