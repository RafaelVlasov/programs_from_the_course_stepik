import string
from random import *
from openpyxl import load_workbook


def generate_password(length, selected_chars):
    """функция возвращающая рандомно
    сформированный пароль из выбранных символов chars и выбранной длинны"""
    password = ""
    for _ in range(length):
        password += choice(selected_chars)
    print(f'Ваш пароль - {password}')
    print('Он будет добавлен в Ваш список паролей')
    return password

# собираем все возможные категории букв и символов в переменные, для возможности дальнейшего выбора
digits = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuation = string.punctuation
chars = ""

# Собираем данные для связки будущего пароля с ресурсом и логином
link = input('Введите ссылку на ресурс (сайт) для которого формируется пароль: ')
login = input('Введите логин для входа на ресурс (сайт) для которого формируется пароль: ')

# Просим пользователя сформировать условия сложности пароля
len_password = int(input('Укажите длину паролей (количество символов): '))
dig_on = input('Включать ли цифры 0123456789? (y/n) ')
ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
ch_on = input('Включать ли символы ()*+,-./:;<=>?@[\]^_`{|}~ (y/n) ')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

#  Собираем получившуюся строку символов и букв из которых будем выбирать отдельные символы будущего пароля
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
        chars.replace(c, '')

# обновляем файл с паролями дозаписывая новые данные
file_name = 'pass_list.xlsx'  # файл должен находиться в папке с программой
work_book = load_workbook(file_name)  # открываем файл
work_sheet = work_book.active  # выбираем активный лист
work_sheet.append([link, login, generate_password(len_password, chars)])  # добавляем новые данные
work_book.save(file_name)
work_book.close()
