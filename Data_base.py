
import json
import csv


def records_data_csv(first_name, last_name, phone_number):
    with open('Directory.csv', 'a', newline='') as csvfile:
        fieldnames = ['Имя', 'Фамилия', 'Номер телефона']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'Имя': first_name,
                         'Фамилия': last_name,
                         'Номер телефона': phone_number})
        print('Данные успешно сохранены в "Directory.csv"')

def record_data_json(first_name, last_name, phone_number):
    data = {'Имя': first_name,
            'Фамилия': last_name,
            'Номер телефона': phone_number}

    with open('Directory_json.txt', 'a') as outfile:
        json.dump(data, outfile)
        print('Данные успешно сохранены в "Directory_json.txt"')


def record_data_txt(first_name, last_name, phone_number):
    data = [first_name, last_name, phone_number]
    with open('Directory.txt', 'a', encoding='cp1251') as text:
        text.writelines('\n')
        text.writelines(data)
        print('Данные успешно сохранены в "Directory.txt"')



