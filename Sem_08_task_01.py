# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
#---------------------------------------------------------------------
# def show_menu() -> int:
# print("\nВыберите необходимое действие:\n"
# "1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")
# choice = int(input())
# return choice
#-------------------------

import csv

def display_all_records():
    for row in reader:
        print(f' Фамилия: {row[0]}\n Имя: {row[1]}\n Номер телефона: {row[2]}\n Комментарий: {row[3]}\n')
def find_last_name(reader):
    last_name = input('Введите фамилию: ')
    for elem in filter(lambda x: x[0] == last_name, reader):
        print(f' Фамилия: {elem[0]}\n Имя: {elem[1]}\n Номер телефона: {elem[2]}\n Комментарий: {elem[3]}\n')
def find_phone_number(reader):
    phone = input('Введите номер телефона: ')
    for elem in filter(lambda x: x[2] == phone, reader):
        print(f' Фамилия: {elem[0]}\n Имя: {elem[1]}\n Номер телефона: {elem[2]}\n Комментарий: {elem[3]}\n')
def add_abonent():
    with open('Sem_08_phonebook.csv', 'a', encoding='utf-8', newline='') as out_file:
        info = input('Введите данные абонента: ').split()
        csv.writer(out_file).writerow(info)

for elem in iter(input, '6'):
    with open('Sem_08_phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        if elem == '1':
            display_all_records()

        elif elem == '2':
            find_last_name(reader)

        elif elem == '3':
            find_phone_number(reader)

        elif elem == '4':
            add_abonent()

        elif elem == '8':
            print('Завершение работы!')



