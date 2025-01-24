def decode(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha():
            new_char = alphabet[(alphabet.index(char.lower()) - shift) % 26]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

encoded_message = "L qph bfpdetzyd zy esp xtoepcx htww cpbftcp jzf ez hctep dszce atpnpd zq nzop."

for shift in range(1, 26):
    decoded_message = decode(encoded_message, shift)
    print(f"Shift {shift}: {decoded_message}")

#Caesar cipher decryption
#Shift 11: A few questions on the midterm will require you to write short pieces of code.