
import json





def record_data_txt(first_name, last_name, phone_number):
    data = [first_name, last_name, phone_number]
    with open('Directory.txt', 'a', encoding='cp1251') as text:
        text.writelines('\n')
        text.writelines(data)
        print('Данные успешно сохранены в "Directory.txt"')



