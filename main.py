#Программа подбирает рандомный пароль согласно критериям введённые пользователем 

from random import *
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

num = int(input('Укажите количество паролей для генерации: '))
len_password = int(input('Укажите длину паролей (количество символов): '))
dig_on = input('Включать ли цифры 0123456789? (y/n) ')
ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if dig_on.lower() == 'y':
    chars += digits
if ABC_on.lower() == 'y':
    chars += lowercase_letters
if abc_on.lower() == 'y':
    chars += uppercase_letters
if ch_on.lower() == 'y':
    chars += punctuation
if exc_on.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')
for _ in range(num):
    print(generate_password(len_password, chars))
