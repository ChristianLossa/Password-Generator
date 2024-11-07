import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N,", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ";", ":", ".", ">", "/", "?"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

combined_symbols = alphabet + symbols + numbers
index = 0
password = []
final_password = ""

for password_characters in combined_symbols:
    password.append(random.choice(combined_symbols))
    random.shuffle(password)
    #print(password)
    random.shuffle(password)
    index += 1
    if index > 12:
        break
    
    
final_password = ''.join(map(str, password))
print(final_password)