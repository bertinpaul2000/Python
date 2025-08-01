import string

# user_input = []
# machine = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
# shift = input("Please enter the key (0 to 25) to use.\n> ")
# alphabets = string.ascii_uppercase
# user_message = input("Enter the message to encrypt.\n> ")
#
# def encrypt_machine():
#     encrypted_msg = ""
#     if machine.lower() == "e":
#         for item in user_message.upper():
#             if item in alphabets:
#                 index = alphabets.find(item)
#                 new_index = index + int(shift)
#                 if new_index > 25:
#                     new_index -= 26
#                 encrypted_msg += alphabets[new_index]
#
#     elif machine.lower() == "d":
#         for item in user_message.upper():
#             if item in alphabets:
#                 index = alphabets.find(item)
#                 new_index = index - int(shift)
#                 if new_index < 0:
#                     new_index += 26
#                 encrypted_msg += alphabets[new_index]
#     print(encrypted_msg)
#
# encrypt_machine()

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