import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_char(s):
    idx = random.randint(0, len(s) - 1)
    return s[idx]

pwd_len = int(input("Length of the password: "))
digits_num = int(input("How many digits: "))
symbols_num = int(input("How many symbols: "))

letters_num = pwd_len - digits_num - symbols_num

result = ""
while letters_num or digits_num or symbols_num:
    rem_types = []
    if letters_num > 0:
        rem_types.append('l')
    if digits_num > 0:
        rem_types.append('d')
    if symbols_num > 0:
        rem_types.append('s')
    
    type_idx = random.randint(0, len(rem_types) - 1)

    if rem_types[type_idx] == 'l':
        letters_num -= 1
        result += generate_char(letters)
    elif rem_types[type_idx] == 'd':
        digits_num -= 1
        result += generate_char(digits)
    else:
        symbols_num -= 1
        result += generate_char(symbols)

print(result)

# alternative
# letter = random.choice(letters)
# random.shuffle(password_list)