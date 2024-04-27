# Welcome to Project 1 python Language
# Telephone_Dictionary:
# A program that represents the phone book,
# so that it receives the phone number,
# and returns to us in the name of the owner of the number

telephone_list: dict[str, str] = {'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah',
                                  '4444444444': 'Abdullah', '5555555555': 'Rawan', '6666666666': 'Faisal',
                                  '7777777777': 'Layla'}

key_input = input('Enter Telephone number: ')

if key_input in telephone_list:
    print('This number ' + key_input + ' Belong to ' + telephone_list[key_input])

elif not (len(key_input) == 10) or not (key_input.isdigit()):
    print('This is invalid number (symbols are not accepted and should enter 10 digit')

else:
    print('Sorry, the number is not found in Telephone Dictionary')
