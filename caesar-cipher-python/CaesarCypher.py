#---------------------Variables or User InputHel
usr_input = input('Input the text to encrypt: ')
usr_input2 = input('Input the shift of alphabet: ')
usr_input3 = input('Encrypt or Decrypt: ')

#---------------------MainCode
def caesar(text, shift, encrypt=True):
    
    if shift < 0 or shift > 25:
        return 'Shift must be between 0 to 25'
    
    if not encrypt:
        shift *= -1
    
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    trans_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    encrypted_table = text.translate(trans_table)
    return encrypted_table


def main():
    final_text = caesar(usr_input, int(usr_input2), usr_input3)
    print(final_text)


if usr_input3.lower() == 'encrypt':
    usr_input3 = True
    main()
elif usr_input3.lower() == 'decrypt':
    usr_input3 = False
    main()
else:
    print('Please check spelling or input a valid answer.')

