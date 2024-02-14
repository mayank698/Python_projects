from caesar_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, cipher_direction, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(end_text)


print(logo)
should_continue = True
while should_continue == True:
    direction = input("Enter Encode or Decode: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the number of shifting: "))
    shift = shift % 26
    caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
    result = input("Type yes to continue and no to exit: ")
    if result == 'no':
        should_continue = False
        print("Goodbye!")
